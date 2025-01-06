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

# :books: 描述图片的内容

继续上期的架构，并使用 Claude 3.5 模型进行图片分析。

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
$ pip install boto3==1.34.140
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
import json
import boto3
import base64
import pprint


###############################################################################
# 读取图片
image_bytes = bytes
with open("image1.jpg", "rb") as image_file:
    image_bytes = base64.b64encode(image_file.read()).decode("utf-8")

###############################################################################
# 声明模型
boto3_session = boto3.Session(profile_name="deeplearnaws")
client_bedrock_runtime = boto3_session.client(
    "bedrock-runtime", region_name="us-east-1"
)

###############################################################################
# 组装提示词
client_prompt = "请用中文描述一下这张图片的内容。"
user_message = {
    "role": "user",
    "content": [
        {
            "type": "image",
            "source": {
                "type": "base64",
                "media_type": "image/jpeg",
                "data": image_bytes,
            },
        },
        {
            "type": "text",
            "text": client_prompt + "\n\n(提示: 请用yaml格式回答问题)",
        },
    ],
}
messages = [user_message]

# https://docs.aws.amazon.com/bedrock/latest/userguide/model-parameters-anthropic-claude-messages.html
body = {
    "anthropic_version": "bedrock-2023-05-31",
    "max_tokens": 4096,
    "system": "You are an image expert who can identify any picture and have your own unique insights.",
    "messages": messages,
}

###############################################################################
# 直接返回方式
response = client_bedrock_runtime.invoke_model(
    body=json.dumps(body),
    modelId="anthropic.claude-3-haiku-20240307-v1:0",
    # modelId="anthropic.claude-3-sonnet-20240229-v1:0",
    # modelId="anthropic.claude-3-5-sonnet-20240620-v1:0",
    accept="application/json",
    contentType="application/json",
)
response_body = json.loads(response.get("body").read())
print(response_body["content"][0]["text"], "\n")
print("=" * 80)
print("输入令牌:{}".format(response_body["usage"]["input_tokens"]))
print("输出令牌:{}".format(response_body["usage"]["output_tokens"]))
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

