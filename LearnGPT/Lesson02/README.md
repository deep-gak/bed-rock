搭建本地 Python+OpenAI 的开发环境
===============================

## 知识点

* 搭建本地 Python+OpenAI 的开发环境

## 官网

https://platform.openai.com/docs/api-reference

## 实战演习/说明讲解

```bash
# 虚拟环境创建
python3 -V
python3 -m venv _pgpt_
source _pgpt_/bin/activate
python -m pip install --upgrade pip
python -m pip install --upgrade setuptools
pip list
python -V
# 安装库
pip install openai urllib3
pip install streamlit
pip list
# 确认安装
mkdir mygpt
cd mygpt
c
...
python main.py
```

### main.py

```python
#import warnings
#warnings.simplefilter('ignore')

import openai
import streamlit as st

print("openai:", openai.__version__)
print("streamlit", st.__version__)
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

