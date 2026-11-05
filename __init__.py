from openai import OpenAI
import os
from dotenv import load_dotenv
load_dotenv(os.path.join(os.path.dirname(__file__), ".env"))
client = OpenAI(
    api_key=os.getenv("DEEPSEEK_API_KEY"),
    base_url="https://api.deepseek.com"
)


def start_chat():
    # 初始化对话历史，写在包里面，main不用管
    messages = [
        {"role": "system", "content": "You are a helpful assistant"}
    ]
    print("开始对话吧（输入 '退出' 结束）：")

    while True:
        user_input = input("\n你：")
        if user_input == "退出":
            print("对话结束")
            return

        messages.append({"role": "user", "content": user_input})

        response = client.chat.completions.create(
            model="deepseek-flash",
            messages=messages,
            stream=False,
            reasoning_effort="high",
            extra_body={"thinking": {"type": "enabled"}}
        )

        reply = response.choices[0].message.content
        print(f"AI：{reply}")
        messages.append({"role": "assistant", "content": reply})

start_chat()