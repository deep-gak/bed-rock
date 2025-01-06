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
    font-size: 32px;
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

# :books: 课程架构代码

### 执行脚本

```bash
# 确认 AWS CLI 配置
$ aws sts get-caller-identity

# 确认 Python 版本
$ python -V
Python 3.12.4

# 确认 Terraform 版本
$ terraform -v
Terraform v1.9.0
```

---
<style scoped>
  section {
    font-size: 32px;
  }
</style>

```bash
# 拉取 terraform 基础代码
git clone https://github.com/komavideo/terraform_main
cd terraform_main
# rm -fr .git

# 确认分支
git branch -a

# 切换分支
git checkout apigateway-lambda-python

# aws provider 配置
nano 00-main.tf
# aws region 配置
nano 01-variables.tf

# 部署代码
terraform init
terraform apply

# 确认部署
curl https://xxx.execute-api.ap-northeast-1.amazonaws.com/dev/lambda
curl -X POST -d 'Hello Bedrock' \
     https://xxx.execute-api.ap-northeast-1.amazonaws.com/dev/lambda

# 删除代码
terraform destroy
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

