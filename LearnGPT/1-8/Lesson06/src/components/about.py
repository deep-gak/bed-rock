import os
import streamlit as st
from PIL import Image


def about():
    st.sidebar.success("感谢您支持小马课程 😉")

    st.subheader("小马 AI 有情商")
    st.write("##### 🤖 使用 OpenAI 公司的 GPT 模型开发各种智能应用程序，AI生活从此开始。")
    st.write("")

    img = Image.open(os.getcwd() + "/images/gpt.webp")
    st.image(img, width=240)
