import json
import boto3
import base64
import datetime
import random

s3Bucket = "komadevops-s3"

t_delta = datetime.timedelta(hours=9)
JST = datetime.timezone(t_delta, 'JST')
now = datetime.datetime.now(JST)

def main(event, context):
    response_body = "No Body"
    client_body = event["body"]
    http_method = event["httpMethod"]
    if client_body and http_method:
        if http_method == "POST":
            response_body = generateImageBySDML(client_body)
    return {
        "statusCode": 200,
        "body": response_body,
        "headers": {"Content-Type": "text/plain"},
    }

def generateImageBySDML(client_body):
    client_bedrock = boto3.client('bedrock-runtime')
    client_s3 = boto3.client('s3')

    input_prompt = client_body  # Example: "Japanese modern female heroine"
    seed = random.randint(0, 4294967295)

    # Calling Stable Diffusion model via Bedrock
    response_bedrock = client_bedrock.invoke_model(
        contentType='application/json',
        accept='application/json',
        modelId='stability.stable-diffusion-xl-v1',
        body=json.dumps({
            "text_prompts": [{"text": input_prompt}],
            "cfg_scale": 20,
            "samples": 1,
            "steps": 30,
            "seed": seed,
            "height": 768,
            "width": 1344,
            "style_preset": "photographic",
        })
    )

    response_bedrock_byte = json.loads(response_bedrock['body'].read())
    response_bedrock_base64 = response_bedrock_byte['artifacts'][0]['base64']
    response_bedrock_finalimage = base64.b64decode(response_bedrock_base64)

    imageName = 'imageName_' + now.strftime('%Y%m%d%H%M%S') + ".png"
    response_s3 = client_s3.put_object(
        Bucket=s3Bucket,
        Body=response_bedrock_finalimage,
        Key=imageName
    )

    generate_presigned_url = client_s3.generate_presigned_url('get_object', Params={
        'Bucket': s3Bucket,
        'Key': imageName,
        'ResponseCacheControl': 'no-cache',
        'ResponseContentDisposition': 'inline',
        'ResponseContentType': 'image/png',
    }, ExpiresIn=3600)
    
    print(generate_presigned_url)

    return generate_presigned_url
