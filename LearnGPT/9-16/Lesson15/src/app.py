import streamlit as st

from components.about import about
from components.home import home
from components.lesson06 import lesson06
from components.lesson15 import lesson15

st.set_page_config(
    # 页面窗体标题
    page_title="小马技术发表APP",
    # 页面图标
    page_icon=":secret:",
    # 宽屏显示
    layout="wide",
    # 默认展开边条
    initial_sidebar_state="expanded",
    # initial_sidebar_state="collapsed",
    menu_items={
        "About": "https://komavideo.com/",
    },
)

def main():
    # 读取 api key 密钥
    deeplearnopenai_api_key = open("key.txt").read().strip()
    if 'deeplearnopenai_api_key' not in st.session_state:
        st.session_state.deeplearnopenai_api_key = deeplearnopenai_api_key

    st.title("ChatGPT AI开发与实践")
    st.sidebar.header("🎈 系统菜单")
    menu = ["ー", "第一个GPT应用", "小马批三国", "关于"]
    choice = st.sidebar.selectbox("功能选择", menu)

    # st.header(choice)
    st.markdown("---")

    if choice == "ー":
        home()
    elif choice == "第一个GPT应用":
        lesson06()
    elif choice == "小马批三国":
        lesson15()
    elif choice == "关于":
        about()
    pass


if __name__ == "__main__":
    main()
