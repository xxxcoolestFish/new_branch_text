print("----- streaming request -----")
# stream = client.chat.completions.create(
#     # 指定您创建的方舟推理接入点 ID，此处已帮您修改为您的推理接入点 ID
#     model="doubao-1-5-pro-32k-250115",
#     messages=[
#         {"role": "system", "content": "你是人工智能助手"},
#         {"role": "user", "content": "常见的十字花科植物有哪些？"},
#     ],
#     # 响应内容是否流式返回
#     stream=True,
# )
# for chunk in stream:
#     if not chunk.choices:
#         continue
#     print(chunk.choices[0].delta.content, end="")
# print()