import os
import streamlit as st
import pandas as pd


def home():
    st.sidebar.success("选择一个页面")

    st.markdown(
        """
        小马为您带来最通俗易懂的GPT课程，大家一起学习，一起加油！  

        👈 从左边菜单栏选您要使用的功能。

        ### 基础知识

        + Python 基础语法

        ### 面向对象

        + 初学者
        + 中级者

        ### 开发工具

        + VSCode
        + Google Colab
        + nano
        + Streamlit
        
        ### 小马技术
        
        - 综合技术(https://komavideo.com)
        - 深学AWS(https://deeplearnaws.com)
        - Github(https://github.com/komavideo)
    """
    )