使用 tiktoken 计算文本的令牌数
===========================

## 知识点

* 使用 tiktoken 计算文本的令牌数

## 官网

https://github.com/openai/tiktoken

## 实战演习/说明讲解

>画面演示

+ 安装 tiktoken
+ 使用 tiktoken 计算文本的令牌数
+ 运行测试

## 操作步骤

### 安装 tiktoken

```bash
pip install -U tiktoken
```

### 使用 tiktoken 计算文本的令牌数

```py
import tiktoken

# 装在 gpt-3.5 模型
encoding = tiktoken.encoding_for_model("gpt-3.5-turbo")

# 编码文本到令牌向量
result = encoding.encode("This is a book.")
print(result, "令牌数:", len(result))

# 反向编码，从令牌到原文本
original_content = encoding.decode(result)
print("原文本:", original_content)

###############################################################################
# 长文编码和还原
# ChatGPT 国粹版: https://github.com/vastxie/Happy-ChatGPT
content = "AI 国粹版是一个基于 OpenAI GPT-3.5Turbo API 的脏话机器人 ，可以和 GPT 一起学习地道的中国话，试了一下，确实脏话挺本地化的，感兴趣的同学可以试试，仅供娱乐。可能引起不适，请谨慎对话、传播。"
result = encoding.encode(content)
print(result, "令牌数:", len(result))

# 反向编码，从令牌到原文本
original_content = encoding.decode(result)
print("原文本:", original_content)

###############################################################################
# 日本語文章
content = "誰だって「できるだけいい仕事をしたい」と考えています。その人なりに一生懸命コードを書いてプルリクエストを作っています。あなたが放つ言葉は、周りの人間の心に影響を与えます。相手のモチベーションを下げることも上げることもできます。我々は互いに「環境」なんです。誰かにとっての良い環境であってください。"
result = encoding.encode(content)
print(result, "トークン数:", len(result))

# 反向编码，从令牌到原文本
original_content = encoding.decode(result)
print("原本:", original_content)
```

### 运行测试

```bash
pythonn main.py
```

## 小马部落

https://discord.gg/VSKw72P

## 课程文件

+ 小马部落Discord专区共享(四级会员)

## 小马视频频道

https://komavideo.com

## 深学AWS

https://deeplearnaws.com

## 深学Azure

https://deeplearnazure.com/

## 深学GCP

https://deeplearngcp.com/

## Youtube

https://youtube.com/@deeplearncloud

