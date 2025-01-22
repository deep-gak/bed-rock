使用 Google Colab 开发 GPT 应用
=============================

## 知识点

* 使用 Google Colab 开发 GPT 应用

## 实战演习/说明讲解

>画面演示

+ 使用 Google Colab 开发 GPT 应用

## 操作步骤

### 使用 Google Colab 开发 GPT 应用

```bash for colab
# 安装 openai 库
!pip install openai

# 保存 key.txt 密钥文件
!echo "sk-123456789012345678901234567890123456789012345678" > key.txt
```

```py
# 确认 openai 安装版本
import openai

print("openai:", openai.__version__)

# 读取 api key 密钥
deeplearnopenai_api_key = open("key.txt").read().strip()
# print(deeplearnopenai_api_key)

# 设置 api key 密钥
openai.api_key = deeplearnopenai_api_key

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
# print(response)
# 响应文本输出
print(str(response['choices'][0]['message']['content']).encode('utf-8').decode('utf-8'))
```

Done.

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

