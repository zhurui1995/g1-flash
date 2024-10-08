import gradio as gr
from zhipuai import ZhipuAI
import os
import json
import time


def format_response(content):
    if "```json" in content:
        content = content[content.find("```json")+len("```json"):]
        content = content[:content.find("```")]
    return content.strip()


def nice_format_response(res_json):
    if '"next_action"' not in res_json:
        res_dict = {"title": "STEP", "content": res_json, "next_action": "continue"}
        res_json = json.dumps(res_dict)
    else:
        if '{"title"' in res_json and "}" in res_json:
            res_json = res_json[res_json.find('{"title"'):res_json.find("}")+1]
    return res_json


def make_api_call(client, messages, max_tokens, is_final_answer=False):
    for attempt in range(3):
        try:
            response = client.chat.completions.create(
                model="glm-4-flash",
                # model="llama-3.1-70b-versatile",
                messages=messages,
                max_tokens=max_tokens,
                temperature=0.5,
                # response_format={"type": "json_object"}
            )

            if not response.choices[0].message.content:
                raise Exception("No response generated")

            res_json = format_response(response.choices[0].message.content)
            res_json = nice_format_response(res_json)
            print(res_json)
            return json.loads(res_json)
            # return json.loads(response.choices[0].message.content)
        except Exception as e:
            if attempt == 2:
                if is_final_answer:
                    return {"title": "Error", "content": f"Failed to generate final answer after 3 attempts. Error: {str(e)}"}
                else:
                    return {"title": "Error", "content": f"Failed to generate step after 3 attempts. Error: {str(e)}", "next_action": "final_answer"}
            time.sleep(1)  # Wait for 1 second before retrying


def generate_response(client, prompt, max_steps=15):
    messages = [
        {"role": "system", "content": """You are an expert AI assistant that explains your reasoning step by step. For each step, provide a title that describes what you're doing in that step, along with the content. Decide if you need another step or if you're ready to give the final answer. Respond in JSON format with 'title', 'content', and 'next_action' (either 'continue' or 'final_answer') keys. USE AS MANY REASONING STEPS AS POSSIBLE. AT LEAST 3. BE AWARE OF YOUR LIMITATIONS AS AN LLM AND WHAT YOU CAN AND CANNOT DO. IN YOUR REASONING, INCLUDE EXPLORATION OF ALTERNATIVE ANSWERS. CONSIDER YOU MAY BE WRONG, AND IF YOU ARE WRONG IN YOUR REASONING, WHERE IT WOULD BE. FULLY TEST ALL OTHER POSSIBILITIES. YOU CAN BE WRONG. WHEN YOU SAY YOU ARE RE-EXAMINING, ACTUALLY RE-EXAMINE, AND USE ANOTHER APPROACH TO DO SO. DO NOT JUST SAY YOU ARE RE-EXAMINING. USE AT LEAST 3 METHODS TO DERIVE THE ANSWER. USE BEST PRACTICES. 
        Identify the user's language habits and then answer using the user's language habits.
        Identify the user's language habits and then answer using the user's language habits.
        

Example of a valid JSON response:
```json
{
    "title": "Identifying Key Information",
    "content": "To begin solving this problem, we need to carefully examine the given information and identify the crucial elements that will guide our solution process. This involves...",
    "next_action": "continue"
}```
"""},
        {"role": "user", "content": prompt},
        {"role": "assistant", "content": "Thank you! I will now think step by step following my instructions, starting at the beginning after decomposing the problem."}
    ]

    steps = []
    step_count = 1
    total_thinking_time = 0

    while True:
        start_time = time.time()
        step_data = make_api_call(client, messages, 200)
        end_time = time.time()
        thinking_time = end_time - start_time
        total_thinking_time += thinking_time

        # Handle potential errors
        if step_data.get('title') == "Error":
            steps.append((f"Step {step_count}: {step_data.get('title')}", step_data.get('content'), thinking_time))
            break

        step_title = f"Step {step_count}: {step_data.get('title', 'No Title')}"
        step_content = step_data.get('content', 'No Content')
        steps.append((step_title, step_content, thinking_time))

        messages.append({"role": "assistant", "content": json.dumps(step_data)})

        if step_data.get('next_action') == 'final_answer':
            break

        step_count += 1

        if step_count > max_steps:
            break

    # Generate final answer
    messages.append({"role": "user", "content": "Please provide the final answer based on your reasoning above."})

    start_time = time.time()
    final_data = make_api_call(client, messages, 200, is_final_answer=True)
    end_time = time.time()
    thinking_time = end_time - start_time
    total_thinking_time += thinking_time

    if final_data.get('title') == "Error":
        steps.append(("Final Answer", final_data.get('content'), thinking_time))
    else:
        steps.append(("Final Answer", final_data.get('content', 'No Content'), thinking_time))

    return steps, total_thinking_time


def format_steps(steps, total_time):
    html_content = ""
    for title, content, thinking_time in steps:
        if title == "Final Answer":
            html_content += "<h3>{}</h3>".format(title)
            html_content += "<p>{}</p>".format(content.replace('\n', '<br>'))
        else:
            html_content += """
            <details>
                <summary><strong>{}</strong></summary>
                <p>{}</p>
                <p><em>Thinking time for this step: {:.2f} seconds</em></p>
            </details>
            <br>
            """.format(title, content.replace('\n', '<br>'), thinking_time)
    html_content += "<strong>Total thinking time: {:.2f} seconds</strong>".format(total_time)
    return html_content


def main(api_key, user_query, max_steps):
    if not api_key:
        return "Please enter your glm-4-flash API key to proceed.", ""

    if not user_query:
        return "Please enter a query to get started.", ""

    try:
        # Initialize the glm-4-flash client with the provided API key
        client = ZhipuAI(api_key=api_key)
    except Exception as e:
        return f"Failed to initialize glm-4-flash client. Error: {str(e)}", ""

    try:
        steps, total_time = generate_response(client, user_query, max_steps)
        formatted_steps = format_steps(steps, total_time)
    except Exception as e:
        return f"An error occurred during processing. Error: {str(e)}", ""

    return formatted_steps, ""


# Define the Gradio interface
with gr.Blocks() as demo:
    gr.Markdown("# g1-flash: Using glm-4-flash to Create O1-like Reasoning Chains")

    gr.Markdown("""
    This is an early prototype of using prompting to create O1-like reasoning chains to improve output accuracy. It is not perfect and accuracy has yet to be formally evaluated. It is powered by glm-4-flash so that the reasoning step is fast!
    
    Fork from open source [repository here](https://github.com/bklieger-groq/g1), modified by Zhu Rui, using glm-4-flash as the LLM.
    """)

    with gr.Row():
        with gr.Column():
            api_input = gr.Textbox(
                label="Enter your glm-4-flash API Key:",
                placeholder="Your glm-4-flash API Key",
                type="password",
            )
            user_input = gr.Textbox(
                label="Enter your query:",
                placeholder="e.g., How many 'r's are in the word strawberry?",
                lines=2
            )
            max_steps = gr.Slider(
                label="Max steps:",
                minimum=3,
                maximum=30,
                value=15,
                step=1
            )
            submit_btn = gr.Button("Generate Response")

    with gr.Row():
        with gr.Column():
            output_html = gr.HTML()

    submit_btn.click(fn=main, inputs=[api_input, user_input, max_steps], outputs=output_html)

# Launch the Gradio app
if __name__ == "__main__":
    demo.launch()
