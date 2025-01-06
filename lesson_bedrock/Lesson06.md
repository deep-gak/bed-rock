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
  h5 {
    color: #6272a4;
    margin-top: 0;
  }
  a {
    font-size: 26px;
  }
</style>

# :books: 列出所有可用模型

使用Lambda函数(boto3)列出当前AWS区域所有可用模型。

##### :white_check_mark: boto3文档
https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock.html

##### :white_check_mark: bedrock文档
https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-bedrock.html

---
<style scoped>
  h3 {
    margin-top: 0;
    color: #ffb86c;
  }
</style>
## 课堂实验

### Lambda函数

```py
import json
import boto3

def main(event, context):
    response_body = listAvailableModels(event, context)
    return {
        'statusCode': 200,
        'body': json.dumps(response_body)
    }
def listAvailableModels(event, context):
    # 定义bedrock客户端对象
    client_bedrock = boto3.client('bedrock')
    # 列出全部可用模型
    response = client_bedrock.list_foundation_models()
    # response = client_bedrock.list_foundation_models(byProvider="Anthropic")
    response_body = []
    for summary in response["modelSummaries"]:
        response_body.append({summary["providerName"]: summary["modelId"]})
    return response_body
```

---
### 执行脚本

```bash
# Terraform工程
cd terraform_main

# 更新Lambda函数代码
nano lambdas/my_lambda/index.py

# 部署Lambda函数
terraform init
terraform apply
terraform destroy

# 使用AWS CLI列出基础模型
aws bedrock list-foundation-models
aws bedrock list-foundation-models --query 'modelSummaries[*].modelId' --output json --region ap-northeast-1
aws bedrock list-foundation-models --query 'modelSummaries[*].{Name:modelName, Id:modelId}' --output json --region ap-northeast-1
aws bedrock list-foundation-models --query 'modelSummaries[*].modelId' --output json --region us-east-1
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

