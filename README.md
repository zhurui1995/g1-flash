# g1-flash
g1-flash: Using glm-4-flash to Create O1-like Reasoning Chains


# g1-flash: Using glm-4-flash to Create O1-like Reasoning Chains

g1-flash is an early prototype that utilizes prompting techniques to generate O1-like reasoning chains, aiming to improve the accuracy of AI-generated outputs. Powered by the **glm-4-flash** model from ZhipuAI, this application provides fast and detailed reasoning steps to user queries through an interactive web interface built with Gradio.

This project is a fork of the open-source [g1 repository](https://github.com/bklieger-groq/g1), modified by Zhu Rui to integrate glm-4-flash as the underlying language model.

## Features

- **Step-by-Step Reasoning**: Generates detailed reasoning steps to provide comprehensive answers.
- **Fast Processing**: Leverages glm-4-flash for quick response times.
- **Interactive Interface**: User-friendly web interface built with Gradio.
- **Customizable Steps**: Allows users to set the maximum number of reasoning steps.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Example](#example)
- [License](#license)
- [Acknowledgments](#acknowledgments)

## Installation

### Prerequisites

- Python 3.7 or higher
- An API key for **glm-4-flash** from [ZhipuAI](https://www.zhipuai.cn/)

### Clone the Repository

```bash
git clone https://github.com/yourusername/g1-flash.git
cd g1-flash
```

### Install Dependencies

Install the required Python packages using pip:

```bash
pip install -r requirements.txt
```

**Dependencies include:**

- `gradio`
- `zhipuai`
- `json`

## Usage

1. **Obtain an API Key**: Sign up on [ZhipuAI](https://www.zhipuai.cn/) to get your glm-4-flash API key.

2. **Run the Application**:

   ```bash
   python app.py
   ```

3. **Access the Interface**: Open your web browser and navigate to the URL provided in the terminal (e.g., `http://127.0.0.1:7860`).

4. **Enter Your API Key**: Input your glm-4-flash API key in the designated field.

5. **Submit a Query**:

   - Enter your question or prompt in the "Enter your query" textbox.
   - Adjust the "Max steps" slider to set the desired number of reasoning steps.
   - Click on the **Generate Response** button.

6. **View the Results**: The application will display the reasoning steps and the final answer. Each step includes:

   - **Title**: A brief description of the step.
   - **Content**: Detailed reasoning for that step.
   - **Thinking Time**: Time taken to generate the step.

## Example

**Sample Query**:

```
How many 'R's are in the word strawberry?
```

**Steps Generated**:

1. **Step 1: Analyzing the Word**
   - Content: Break down the word "strawberry" to identify each letter.
   - Thinking Time: 0.5 seconds

2. **Step 2: Counting the Letter 'R'**
   - Content: Count the number of times 'R' appears in "strawberry".
   - Thinking Time: 0.4 seconds

3. **Final Answer**
   - Content: There are two 'R's in the word "strawberry".

**Total Thinking Time**: 1.2 seconds

![g1-flash e1](examples/strawberry2.png)

![g1-flash e2](examples/Turing_completeness.png)


## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgments

- **Original Author**: [bklieger-groq](https://github.com/bklieger-groq/g1)
- **Modifier**: Zhu Rui
- **Powered By**: [glm-4-flash](https://www.zhipuai.cn/) from ZhipuAI
- **Built With**: [Gradio](https://gradio.app/)

---

Feel free to contribute to the project by submitting issues or pull requests. For major changes, please open an issue first to discuss what you would like to change.

For any questions or feedback, please issue.

---

# g1-flash

g1-flash：使用 **glm-4-flash** 创建类似 O1 的推理链

## 简介

g1-flash 是一个早期的原型，它利用提示技术来生成类似 O1 的推理链，旨在提高 AI 生成输出的准确性。该应用由 ZhipuAI 的 **glm-4-flash** 模型驱动，通过 Gradio 构建的交互式网页界面，为用户的查询提供快速而详细的推理步骤。

该项目是开源 [g1 仓库](https://github.com/bklieger-groq/g1) 的一个分支，由Zhu Rui修改，集成了 glm-4-flash 作为底层语言模型。

## 功能特性

- **逐步推理**：生成详细的推理步骤，提供全面的答案。
- **快速处理**：利用 glm-4-flash，实现快速的响应时间。
- **交互式界面**：采用 Gradio 构建的用户友好型网页界面。
- **可定制步骤**：允许用户设置推理步骤的最大数量。

## 目录

- [安装](#安装)
  - [先决条件](#先决条件)
  - [克隆仓库](#克隆仓库)
  - [安装依赖](#安装依赖)
- [使用方法](#使用方法)
- [示例](#示例)
- [许可证](#许可证)
- [致谢](#致谢)

## 安装

### 先决条件

- Python 3.7 或更高版本
- 从 [智谱 AI](https://www.zhipuai.cn/) 获取的 **glm-4-flash** API 密钥

### 克隆仓库

```bash
git clone https://github.com/yourusername/g1-flash.git
cd g1-flash
```

### 安装依赖

使用 pip 安装所需的 Python 包：

```bash
pip install -r requirements.txt
```

**依赖项包括：**

- `gradio`
- `zhipuai`
- `json`

## 使用方法

1. **获取 API 密钥**：在 [智谱 AI](https://www.zhipuai.cn/) 注册，获取你的 glm-4-flash API 密钥。

2. **运行应用程序**：

   ```bash
   python app.py
   ```

3. **访问界面**：打开你的网页浏览器，导航到终端中提供的 URL（例如，`http://127.0.0.1:7860`）。

4. **输入 API 密钥**：在指定字段中输入你的 glm-4-flash API 密钥。

5. **提交查询**：

   - 在“输入你的查询”文本框中输入你的问题或提示。
   - 调整“最大步骤”滑块，设置所需的推理步骤数量。
   - 点击 **“生成响应”** 按钮。

6. **查看结果**：应用程序将显示推理步骤和最终答案。每个步骤包括：

   - **标题**：步骤的简要描述。
   - **内容**：该步骤的详细推理。
   - **思考时间**：生成该步骤所花费的时间。

## 示例

**示例查询**：

```
单词 "strawberry" 中有多少个字母 'R'？
```

**生成的步骤**：

1. **步骤 1：分析单词**
   - 内容：将单词 "strawberry" 分解，识别每个字母。
   - 思考时间：0.5 秒

2. **步骤 2：计数字母 'R'**
   - 内容：计算 "strawberry" 中出现 'R' 的次数。
   - 思考时间：0.4 秒

3. **最终答案**
   - 内容：单词 "strawberry" 中有两个字母 'R'。

**总思考时间**：1.2 秒

![g1-flash 示例1](examples/strawberry2.png)

![g1-flash 示例2](examples/Turing_completeness.png)

## 许可证

本项目采用 [MIT 许可证](LICENSE) 。

## 致谢

- **原作者**： [bklieger-groq](https://github.com/bklieger-groq/g1)
- **修改者**：zhurui
- **技术支持**：来自智谱 AI 的 [glm-4-flash](https://www.zhipuai.cn/)
- **构建工具**： [Gradio](https://gradio.app/)

---

欢迎通过提交问题或拉取请求来为本项目做出贡献。对于重大更改，请先打开一个问题进行讨论。

如有任何问题或反馈，请在项目中提交 Issue。
