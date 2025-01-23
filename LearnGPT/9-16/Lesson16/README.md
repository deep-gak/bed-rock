LlamaIndex - 本地保存向量索引数据
===============================

## 知识点

* 将 LlamaIndex 编码的向量索引持久化(保存到本地)

## 实战演习/说明讲解

>画面演示

+ 将 LlamaIndex 编码的向量索引保存到本地
+ 读取持久化的向量数据，生成问题回答
+ 动作确认

## 操作步骤

### 将 LlamaIndex 编码的向量索引保存到本地

*makeIndex.py*

```py
import openai
from llama_index import VectorStoreIndex, SimpleDirectoryReader

# 读取 api key 密钥
deeplearnopenai_api_key = open("key.txt").read().strip()
# 设置 api key 密钥
openai.api_key = deeplearnopenai_api_key

# 读取 data 文件夹获取 *.txt 文件，并进行向量化
documents = SimpleDirectoryReader('data').load_data()
index = VectorStoreIndex.from_documents(documents)

# 保存向量模型到 ./storage 文件夹
index.storage_context.persist()

print("编码保存完成！")
```

### 读取持久化的向量数据，生成问题回答

*loadIndex.py*

```py
import openai
from llama_index import StorageContext, load_index_from_storage

# 读取 api key 密钥
deeplearnopenai_api_key = open("key.txt").read().strip()
# 设置 api key 密钥
openai.api_key = deeplearnopenai_api_key

# 读取保存的向量索引
storage_context = StorageContext.from_defaults(persist_dir="./storage")
# 装载索引
index = load_index_from_storage(storage_context)

# 提问
query_engine = index.as_query_engine()
response = query_engine.query("请问桃园结义是几个人？都是谁？")
print(response)
```

### 动作确认

```bash
# 编码向量，持久化保存
python makeIndex.py

# 确认持久化数据
ls storage

# 读取保存的向量
python loadIndex.py
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

