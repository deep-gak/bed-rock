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

# :books: 建立 KnowledgeBase 知识库

在美东一区(us-east-1)建立知识库

+ 建立 S3 存储桶
+ 上传 PDF 数据文件
+ 建立知识库

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
  li {
    font-size: 24px;
  }
</style>
## 课堂实验

+ Knowledge base name
  - knowledge-base-sanguo
+ Create and use a new service role
  - AmazonBedrockExecutionRoleForKnowledgeBase_sanguo
+ Data source name
  - knowledge-base-sango-data-source
+ S3 URI
  - s3://deeplearnaws-bedrock
+ Chunking strategy
  - Default chunking strategy(300 tokens)
+ Embeddings model
  - Titan Text Embeddings v2
+ Vector database
  - Quick create a new vector store - Recommended

---
<style scoped>
  h3 {
    margin-top: 0;
  }
</style>

### 提示词

```
请问桃园结义是几个人？都是谁？

虎牢关谁打败了吕布？

小马三顾茅庐请出的人是谁？
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

