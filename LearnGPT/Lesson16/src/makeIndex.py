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
