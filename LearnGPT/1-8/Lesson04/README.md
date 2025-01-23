我的第一个 GPT 应用程序
=====================

## 知识点

* 利用 API 密钥开发第一个 GPT 应用程序

## 官网

https://platform.openai.com/docs/libraries

## 实战演习/说明讲解

+ 开发第一个 Python GPT 应用程序
+ 动作确认

## 操作步骤

### 开发第一个 Python GPT 应用程序

*key.txt*

```
sk-123456789012345678901234567890123456789012345678
```

*main.py*

```py
import os
import openai

# 读取 api key 密钥
deeplearnopenai_api_key = open("key.txt").read().strip()
# print(deeplearnopenai_api_key)

# 设置 api key 密钥
openai.api_key = deeplearnopenai_api_key

###########################################################
# 单纯的问题回答(legacy)
# https://platform.openai.com/docs/api-reference/completions/create
response = openai.Completion.create(
    model="text-davinci-003",
    prompt="给我介绍一本关于OpenAI的书,请只显示书名和出版日期。", 
    top_p=0.5, # 采样率
    max_tokens=200)
# 响应结果输出
print(response)
# 响应文本输出
print(str(response['choices'][0]['text']).encode('utf-8').decode('utf-8'))

###########################################################
# Chat方式回答问题(new)
# https://platform.openai.com/docs/api-reference/chat/create
response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo", # gpt-3.5-turbo, gpt-4(付费用户)
    messages=[{
        "role": "user",
        "content": "给我介绍一本关于OpenAI的书,请只显示书名和出版日期。"
    }])
# 响应结果输出
print(response)
# 响应文本输出
print(str(response['choices'][0]['message']['content']).encode('utf-8').decode('utf-8'))

###########################################################
# Chat方式回答问题(new)
# 添加系统角色(system)，让ChatGPT的回答满足您的偏好
response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo", # gpt-3.5-turbo, gpt-4(付费用户)
    messages=[{
        "role": "system",
        "content": "请以幽默搞笑的方式回答每一个问题",
    },{
        "role": "user",
        "content": "给我介绍一本关于OpenAI的书,请只显示书名和出版日期。"
    }])
# 响应结果输出
print(response)
# 响应文本输出
print(str(response['choices'][0]['message']['content']).encode('utf-8').decode('utf-8'))
```

### 动作确认

```bash
python main.py

# 直接命令行方式
export OPENAI_API_KEY=sk-123456789012345678901234567890123456789012345678
# gpt 3.5
openai api chat_completions.create -m gpt-3.5-turbo -g user "给我介绍一本关于OpenAI的书,请只显示书名和出版日期。"
# gpt 4(付费用户)
openai api chat_completions.create -m gpt-4 -g user "给我介绍一本关于OpenAI的书,请只显示书名和出版日期。"
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

