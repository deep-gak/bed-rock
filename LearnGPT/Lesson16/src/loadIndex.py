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