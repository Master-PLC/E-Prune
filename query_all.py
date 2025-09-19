from dotenv import load_dotenv
load_dotenv()

import json
import os
import requests

# 配置API参数
url = "https://www.dmxapi.cn/v1/chat/completions"  # API端点
payload = {
    "model": "Qwen3-8B",  # 指定模型
    "messages": [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "周树人和鲁迅是兄弟吗？"},
    ],
}
headers = {
    "Accept": "application/json",
    "Authorization": os.environ['API_KEY'],  # 替换为你的API Key
    "User-Agent": "DMXAPI/1.0.0",
    "Content-Type": "application/json",
}

# 发送请求
response = requests.post(url, headers=headers, data=json.dumps(payload))
print(response.text)



# from openai import OpenAI

# # 初始化客户端
# client = OpenAI(
#     api_key=os.environ['API_KEY'],  # 替换为你的DMXAPI密钥
#     base_url="https://www.dmxapi.cn/v1",  # DMXAPI服务地址
# )

# # 创建请求
# response = client.responses.create(
#     model="gpt-4.1-mini",  # 指定使用的模型
#     input="你是谁？",  # 输入问题文本
# )

# # 打印响应结果
# print(response)