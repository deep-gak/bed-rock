---
marp: true
theme: default
header: 'Amazon Bedrock 课程'
footer: '小马技术'
style: |
  header {
    color: #00ced1;
    font-weight: bold;
  }
  footer {
    color: #50fa7b;
    font-weight: bold;
  }
  h1 {
    color: #ffb86c;
    font-size: 64px;
  }
  section {
    display: flex;
    flex-direction: column;
    justify-content: flex-start;
    background-color: #232f3e;
    color: #f8f8f2;
    font-size: 24px;
    font-family: Yuanti SC;
  }
  a {
    color: #8be9fd;
  }

---
<style scoped>
  section {
    align-items: center;
    justify-content: center;
  }
  h1 {
    color: #8be9fd;
    font-size: 100px;
  }
  img {
    border-radius: 50% 20% / 10% 40%;
  }
</style>

![width:200px drop-shadow:0,5px,10px,rgba(f,f,f,.4)](../images/aws/Arch_Amazon-Bedrock_64@5x.png)

# Amazon Bedrock

---
<style scoped>
  section {
    font-size: 40px;
  }
  h1 {
    font-size: 50px;
    color: #f8f8f2;
  }
  li {
    font-family: Menlo;
    font-size: 32px;
  }
</style>

# :books: 开发一个 Token 计算工具 (Anthropic)

LLM模型使用输入输出令牌(Token)进行计费，我们需要一个工具来计算令牌数，今天就开发一个这样的工具。

---
<style scoped>
  section {
    align-items: center;
    justify-content: center;
  }
  h1 {
    color: #f8f8f2;
    font-size: 200px;
    margin: 0;
  }
  img {
    border: 10px solid #f8f8f2;
    border-radius: 20%;
    margin: 0;
  }
</style>

![width:200px](./images/step-by-step-operation.webp)

# 操作演示

---
<style scoped>
  h3 {
    margin-top: 0;
  }
</style>
## 课堂实验

### 执行脚本

```bash
$ python -V
Python 3.12.4
$ python -m venv _pvenv_
$ source _pvenv_/bin/activate
$ python -m pip install --upgrade pip
$ python -m pip install --upgrade setuptools
$ pip list
# 安装库
$ pip install anthropic==0.30.1
# 编辑程序
$ nano main.py
# 运行程序
$ python main.py
```

---
<style scoped>
  h3 {
    margin-top: 0;
  }
</style>
### Lambda函数

```python
# https://github.com/anthropics/anthropic-sdk-python
from anthropic import Anthropic

client = Anthropic()

prompt = "我想去澳洲留学，给我一些建议好吗？"
# prompt = "I want to go to Australia to study, can you give me some advice?"
# prompt = """Claude 是由 Anthropic 开发的一系列大型语言模型，旨在革新您与 AI 交互方式。
# Claude 擅长处理涉及语言、推理、分析、编码等各种任务。我们的模型功能强大，易于使用，并且可以根据您的需求进行定制。
# Claude 3 Haiku、Sonnet 和 Opus 是下一代 Claude 模型。它们是最先进的文本和视觉模型，可以根据图像和文本输入生成类似人类的文本输出。
# 凭借强大的视觉能力,它们为计算机视觉和图像理解应用开辟了令人兴奋的可能性。最强大的模型，在广泛的任务中提供无与伦比的智能、推理和创造力，
# 而 Haiku 以非常高的速度和低成本提供大量功能。Sonnet 在两者之间提供了很好的平衡。
# 通过我们的快速入门指南直接开始,并了解如何在几分钟内进行第一次API调用。
# 如果您在结合代码和有趣用例的应用示例中学习提示更好，请访问 Anthropic 手册。在那里，您将找到可复制的代码，
# 演示如何在更高级的场景中以巧妙有效的方式使用 Claude,例如上传 PDF、工具使用和函数调用、嵌入等。
# 让我们快速帮助您开始使用 Claude!在本指南中,我们将引导您完成设置环境、安装必要的库以及向 Claude 发送第一个 API 请求的过程。让我们开始吧！
# 请注意，虽然本指南使用我们的 Python SDK,但我们也维护 TypeScript SDK 并支持直接的 HTTP 集成。请参阅我们的客户端 SDK 和 API 参考文档。
# Claude 在广泛的基于文本的任务中表现出色。Claude 经过训练，可以接收代码、散文和其他自然语言输入，并提供响应的文本输出。
# 当您将数据发送到 Claude 以生成响应时，您发送的是一个”提示”，发送提示的行为称为”提示“。
# 提示最好写成自然语言查询，就像您在指导某人做某事一样，细节越多越好。您可以通过提示工程进一步改进基准提示。
# 为了充分利用 Claude 3 并增强其在特定任务中的性能，您可能需要将特定的提示工程技术应用于提示。我们的提示工程涵盖了各种策略和技巧，
# 可帮助您制定最有效的提示以优化 Claude 3 的输出。对于旧版模型，提示工程可能更有必要以发挥最大性能，而 Claude 3 模型则更易于控制和指导。
# 要查看 Claude 文本生成功能的代码示例，请查看 Anthropic 手册，其中包含一组以 Jupyter notebook 形式呈现的配方。
# 这些 notebook 提供了可复制的代码，演示了如何在更高级场景中使用 Claude,例如上传PDF、工具使用和函数调用、嵌入等。
# 有关展示 Claude 功能并帮助您开始各种任务的广泛基于文本的提示。
# 该库包含不同用例和复杂程度的提示，使您更容易找到并调整提示以满足特定需求。
# 要了解如何通过我们的 API 与 Claude 交互，请查阅我们的 API 文档。该文档提供了有关如何发送请求、处理响应和排除错误的详细信息。
# 系统提示是一种在向 Claude 提出问题或任务之前，为其提供上下文、指令和指南的方式。通过使用系统提示，您可以为对话设置舞台，
# 指定 Claude 的角色、个性、语气或任何其他相关信息，这将有助于它更好地理解和响应用户的输入。
# """

# 令牌数计算
tokens = client.count_tokens(prompt)
print(prompt)
print("----- 令牌数:{} -----".format(tokens))
```

---
<style scoped>
  section {
    align-items: center;
    justify-content: center;
  }
  h1 {
    color: #f8f8f2;
    font-size: 200px;
  }
</style>

# 下课时间

