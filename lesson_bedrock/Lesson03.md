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

# :books: 价格模型

## Amazon Bedrock
https://aws.amazon.com/cn/bedrock/pricing/

## OpenAI
https://openai.com/api/pricing/

---
<style scoped>
  section {
    align-items: center;
    justify-content: top;
  }
  h1 {
    color: #f8f8f2;
    font-size: 200px;
  }
  table {
    font-size: 32px;
    color: #44475a;
  }
  td {
    text-align: right;
  }
</style>

## 模型价格 (1,000令牌)

**输入令牌**

| 服务 | Claude 3 Opus | Claude 3 Sonnet | gpt-4o |
| --- | --- | --- | --- |
| 价格 | 0.015 USD | 0.003 USD | 0.005 USD |

**输出令牌**

| 服务 | Claude 3 Opus | Claude 3 Sonnet | gpt-4o |
| --- | --- | --- | --- |
| 价格 | 0.075 USD | 0.015 USD | 0.015 USD |

使用 Amazon Bedrock，您需要为模型的推理和自定义支付费用。有两种推理定价方案供您选择： 1.按需和批量：此模式允许您按照即用即付的原则使用基础模型，无需承诺使用期限。2.预配置吞吐量：此模式允许您预先配置足够的吞吐量，以满足应用程序的性能要求，作为交换，您需要承诺使用期限。

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

