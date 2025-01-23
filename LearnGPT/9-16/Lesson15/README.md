LlamaIndex - 编写自己的知识库
===========================

## 知识点

* 使用 LlamaIndex 编写自己的知识库

## 官网

https://www.llamaindex.ai/

## 实战演习/说明讲解

>画面演示

+ 制作我们的知识库文档
+ 利用 LlamaIndex 编写向量索引库
+ 通过索引库回答用户的问题

## 操作步骤

### 制作我们的知识库文档

*三国演义.txt*

https://www.guishuji.com/ertong/4734/

+ 替换内容
  - 刘备 -> 小马

### 利用 LlamaIndex 编写向量索引库

*使用Colab制作知识库向量索引*

```bash
# 安装 openai 库
!pip install openai
!pip install llama-index
# 保存 key.txt 密钥文件
!echo "sk-123456789012345678901234567890123456789012345678" > key.txt
```

```py
import openai
from llama_index import VectorStoreIndex, SimpleDirectoryReader

# 读取 api key 密钥
deeplearnopenai_api_key = open("key.txt").read().strip()
# print(deeplearnopenai_api_key)

# 设置 api key 密钥
openai.api_key = deeplearnopenai_api_key

# 读取 data 文件夹获取 *.txt 文件，并进行向量化
documents = SimpleDirectoryReader('data').load_data()
index = VectorStoreIndex.from_documents(documents)

# 提问
query_engine = index.as_query_engine()
response = query_engine.query("请问桃园结义是几个人？都是谁？")
print(response)
```

### 通过索引库回答用户的问题

```prompt
请问桃园结义是几个人？都是谁？
```

```prompt
董卓是好人吗？
```

```prompt
虎牢关谁打败了吕布？
```

```prompt
小马三顾茅庐请出的人是谁？
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

