import streamlit as st
import openai
from llama_index import VectorStoreIndex, SimpleDirectoryReader


def lesson15():
    # 设置 api key 密钥
    openai.api_key = st.session_state.deeplearnopenai_api_key

    index = None
    if "llama_index" not in st.session_state:
        # 读取 data 文件夹获取 *.txt 文件，并进行向量化
        documents = SimpleDirectoryReader('data').load_data()
        index = VectorStoreIndex.from_documents(documents)
        st.session_state.llama_index = index
    else:
        index = st.session_state.llama_index

    # 初始化聊天数组，保存到session中
    if "messages15" not in st.session_state:
        st.session_state.messages15 = []

    st.sidebar.info("第15课 LlamaIndex - 编写自己的知识库")
    col1, col2, col3 = st.sidebar.columns([1, 10, 1])

    if col2.button("清空聊天记录", use_container_width=True, type="primary"):
        st.session_state.messages15 = []

    # 显示聊天信息
    for message in st.session_state.messages15:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    if prompt := st.chat_input("小马批三国"):
        # 接受用户的输入显示到消息区
        with st.chat_message("user"):
            st.markdown(prompt)
        # 将用户输入加入到session
        st.session_state.messages15.append({"role": "user", "content": prompt})

        if index != None:
            # 提问
            query_engine = index.as_query_engine()
            response = query_engine.query(prompt)
            print(response)

            with st.chat_message("assistant"):
                st.markdown(response)

            # 将回答加入到session
            st.session_state.messages15.append(
                {"role": "assistant", "content": response}
            )
