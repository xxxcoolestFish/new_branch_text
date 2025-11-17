import os
from openai import OpenAI

# 请确保您已将 API Key 存储在环境变量 ARK_API_KEY 中
# 初始化Openai客户端，从环境变量中读取您的API Key
client = OpenAI(
    # 此为默认路径，您可根据业务所在地域进行配置
    base_url="https://ark.cn-beijing.volces.com/api/v3",
    # 从环境变量中获取您的 API Key
    api_key='829ae861-b492-4d3e-8443-45c276707fd2',
)

message1 = [
        {"role": "system", "content": "那是一位浪漫的现代诗诗人，十分擅长接纳他人的意见"},
        {"role": "user", "content": "写一首歌颂大海的诗"},
    ]

# Non-streaming:
print("----- standard request -----")
# completion = client.chat.completions.create(
#     # 指定您创建的方舟推理接入点 ID，此处已帮您修改为您的推理接入点 ID
#     model="doubao-1-5-pro-32k-250115",
#     messages=[
#         {"role": "system", "content": "你是一名浪漫的现代诗诗人"},
#         {"role": "user", "content": "请你写一首描述现代人爱情的诗，不要超过 100 字"},
#     ],
# )
# print(completion.choices[0].message.content)

def get_cri(porty):
    content = "这首诗描述现代年轻人爱情的诗有哪些缺陷与不足？请分条列出"
    content+='\n'
    content+=porty
    completion = client.chat.completions.create(
    # 指定您创建的方舟推理接入点 ID，此处已帮您修改为您的推理接入点 ID
    model="doubao-1-5-pro-32k-250115",
    messages=[
        {"role": "system", "content": "你是一位专业的、浪漫的现代诗批评家和鉴赏家，擅长描写现代年轻人的爱情"},
        {"role": "user", "content": content},
        ],
    )
    return completion.choices[0].message.content

def get_porty(proty,cir):
    content = "这是之前一个人写的描述现代年轻人爱情的诗"
    content+='\n'
    content += proty
    content += '\n'
    content += "请你根据下面的评论改写这首诗，让其变得更浪漫、更好、更感人。但是要注意，不能超过 100 字，否则有失美感。"
    content += '\n'
    content += cir
    content += '\n'
    content += '只需给出改后的诗，无需解释。'
    completion = client.chat.completions.create(
    # 指定您创建的方舟推理接入点 ID，此处已帮您修改为您的推理接入点 ID
    model="doubao-1-5-pro-32k-250115",
    messages=[
        {"role": "system", "content": "你是一位专业的、浪漫的现代诗作家，擅长描写现代年轻人的爱情，擅长根据他人意见，把原来的现代诗写的更好。并且十分擅长在 100 字之内写出优美浪漫的诗篇"},
        {"role": "user", "content": content},
        ],
    )
    return completion.choices[0].message.content


counter = 0
porty = ''
cir = ''
while counter<=300:
    if counter == 0:
        porty = '# 都市恋曲\n在霓虹交织的街角，\n目光邂逅，心瞬间燃烧。\n似流星划过寂寥，\n爱如闪电，点亮喧嚣。\n\n微信里情话飘飘，\n约会时心跳如潮。\n可现实像雾绕，\n承诺在风中缥缈。\n\n我们在爱里奔跑，\n却不知能否停靠。'
    print('下面是第'+str(counter)+'次迭代')
    counter+=1
    print('-----------por------------')
    print(porty)
    with open('record.txt','a') as f:
        f.write('\n'+porty)
    cir = get_cri(porty)
    print(cir)
    print('-----------cir------------')
    porty = get_porty(porty,cir)
    print('\n')