文字描述图片生成
===============

## 知识点

* 使用 DALL·E 引擎，通过文字描述生成图片

## 官网

https://platform.openai.com/docs/api-reference/images/create

## 价格

https://openai.com/pricing

## 实战演习/说明讲解

>画面演示

+ 编写文字生成图片 DALL·E 程序
+ 运行调试

## 操作步骤

### 编写文字生成图片 DALL·E 程序

```py
import openai
import urllib.request
# 如果下载图片时出现证明书错误，请打开下面的代码
# import ssl
# ssl._create_default_https_context = ssl._create_unverified_context

# 读取 api key 密钥
deeplearnopenai_api_key = open("key.txt").read().strip()
# print(deeplearnopenai_api_key)

# 设置 api key 密钥
openai.api_key = deeplearnopenai_api_key

###############################################################################
# a pug dog in a park
# an american shorthair in a bookstore
# 一只啄木鸟在捉虫子
# 机器人在沙滩上奔跑
# 可愛い女の子
response = openai.Image.create(
    # 图片描述
    prompt="a pug dog in a park",
    # 生成张数
    n=1,
    # 分辨率
    size="512x512",
)
image_url = response["data"][0]["url"]

print(image_url)
urllib.request.urlretrieve(image_url, "generated.png")

###############################################################################
# 图片风格变换
response = openai.Image.create_variation(
    image=open("_zelda.png", "rb"), n=1, size="512x512"
)

image_url = response["data"][0]["url"]
urllib.request.urlretrieve(image_url, "generated2.png")
```

### 运行调试

```bash
python main.py
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

