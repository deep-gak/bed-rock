import openai
import streamlit as st
# import pandas as pd


def lesson06():
    # 设置 api key 密钥
    openai.api_key = st.session_state.deeplearnopenai_api_key

    # 初始化聊天数组，保存到session中
    if "messages" not in st.session_state:
        st.session_state.messages = []

    st.sidebar.info("第六课 使用 Streamlit 开发 GPT 应用")
    col1, col2, col3 = st.sidebar.columns([1, 10, 1])

    if col2.button("清空聊天记录", use_container_width=True, type="primary"):
        st.session_state.messages = []

    # 显示聊天信息
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    if prompt := st.chat_input("说点什么吧"):
        # 接受用户的输入显示到消息区
        with st.chat_message("user"):
            st.markdown(prompt)
        # 将用户输入加入到session
        st.session_state.messages.append({"role": "user", "content": prompt})

        # 显示GPT回答
        with st.chat_message("assistant"):
            message_placeholder = st.empty()
            #########################################################################
            # 流式输出
            full_response = ""
            for response in openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": prompt}],
                stream=True,  # 流式返回
            ):
                full_response += response.choices[0].delta.get("content", "")
                message_placeholder.markdown(full_response + "▌")
            #########################################################################
            message_placeholder.markdown(full_response)
        # 将GPT回答加入到session
        st.session_state.messages.append(
            {"role": "assistant", "content": full_response}
        )
