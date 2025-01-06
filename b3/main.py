import time
from langchain_aws import ChatBedrock
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage


def main(event, context):

    start_time = time.time()  # 获取开始时间

    messages = [
        SystemMessage("你是一语言专辑，精通英语和中文。"),
        HumanMessage("可以帮我翻译一些英文成中文吗？"),
        AIMessage("当然可以！请告诉我你需要翻译的英文内容，我会尽力帮你翻译成中文。"),
        HumanMessage("book"),
    ]

    model = ChatBedrock(
        model_id="anthropic.claude-3-haiku-20240307-v1:0",
        model_kwargs={
            "max_tokens": 512,
            "temperature": 0,
            "top_p": 1.0,
        },
    )

    result = model.invoke(messages)
    print(result.content)

    end_time = time.time()  # 获取结束时间
    execution_time = "(程序运行时间：%.2f 秒)" % (
        end_time - start_time
    )  # 计算程序运行时间
    print(execution_time)

    return {
        "statusCode": 200,
        "body": "{}\n\n{}".format(execution_time, result.content),
        "headers": {"Content-Type": "text/plain"},
    }