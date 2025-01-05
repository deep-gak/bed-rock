import json
import boto3

def main(event, context):
    response_body = ListAvailableModels(event, context)
    return {
        "statusCode": 200,
        "body": json.dumps(response_body)
    }

def ListAvailableModels(event, context):
    # 定义 Bedrock 客户端对象
    client_bedrock = boto3.client('bedrock')
    # 列出全部可用模型
    response = client_bedrock.list_foundation_models()
    # response = client_bedrock.list_foundation_models(byProvider="Anthropic")
    response_body = []
    for summary in response["modelSummaries"]:
        response_body.append({summary["providerName"]: summary["modelId"]})
    return response_body
