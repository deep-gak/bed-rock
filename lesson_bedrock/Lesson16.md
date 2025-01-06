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

# :books: Lambda 函数调用知识库 RAG

通过编程的方式调用知识库，完成 RAG 应用程序。

---
<style scoped>
  h1 {
    font-size: 64px;
    color: #f8f8f2;
    margin: 0;
  }
  section {
    align-items: center;
    justify-content: center;
  }
  img {
    border-radius: 2%;
    margin: 0;
  }
</style>

# 系统架构

![width:924px](./images/Lesson14a.png)

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
### 执行脚本

```bash
# Terraform工程
cd terraform_main
# 修改 aws provider 配置
nano 00-main.tf
# 修改 aws region 配置(@弗吉尼亚区)
nano 01-variables.tf

# 更新Lambda函数代码
nano lambdas/my_lambda/index.py

# 部署Lambda函数
terraform init
terraform apply

# 测试Lambda函数
# - 虎牢关谁打败了吕布？
# - 小马三顾茅庐请出的人是谁？
curl -X POST -d "请问桃园结义是几个人？都是谁？" \
    https://xxx.execute-api.us-east-1.amazonaws.com/dev/lambda

# 删除云资源
terraform destroy
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
import time
import pprint

client_bedrock = boto3.client("bedrock-runtime")
client_bedrock_knowledgebase = boto3.client("bedrock-agent-runtime")


def main(event, context):

    start_time = time.time()  # 获取开始时间

    result = "No Body"
    http_method = event["httpMethod"]
    client_body = event["body"]
    if client_body and http_method and http_method == "POST":
        result = generateTextCompletion(client_body)
    else:
        result = "No body({})".format(http_method)

    end_time = time.time()  # 获取结束时间
    execution_time = "(程序运行时间：%.2f 秒)" % (
        end_time - start_time
    )  # 计算程序运行时间
    print(execution_time)

    return {
        "statusCode": 200,
        "body": "{}\n\n{}".format(execution_time, result),
        "headers": {"Content-Type": "text/plain"},
    }


def generateTextCompletion(client_prompt):

    prompt = """
Human: {}
Assistant:
""".format(
        client_prompt
    )
    print(prompt)

    # https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agent-runtime.html
    # 命令行获取 model ARN
    # aws bedrock get-foundation-model --model-identifier 'anthropic.claude-v2:1' --profile deeplearnaws --region=us-east-1
    client_knowledgebase = client_bedrock_knowledgebase.retrieve_and_generate(
        input={"text": prompt},
        retrieveAndGenerateConfiguration={
            "type": "KNOWLEDGE_BASE",
            "knowledgeBaseConfiguration": {
                "knowledgeBaseId": "XXXXXXXXXX",
                "modelArn": "arn:aws:bedrock:us-east-1::foundation-model/anthropic.claude-v2:1",
            },
        },
    )
    pprint.pprint(client_knowledgebase)

    response_kbase_final = client_knowledgebase["output"]["text"]

    return response_kbase_final
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

