from openai import OpenAI
import os

client = OpenAI(
    # 此为默认路径，您可根据业务所在地域进行配置
    base_url="https://ark.cn-beijing.volces.com/api/v3",
    # 从环境变量中获取您的 API Key
    api_key='829ae861-b492-4d3e-8443-45c276707fd2',
)

def expand_sentences(sent):
    content = "下面是一个故事："
    content+='\n'
    content += sent
    content += '\n'
    content += "原有故事的基础上，通过仅仅加入一个句子或者改写一个句子的部分内容，造成情节的反转与高潮。一定要注意，只能添加或改写一个句子！"
    content += '\n'
    content += '只需给出在最后添加的故事，无需解释。'
    completion = client.chat.completions.create(
    # 指定您创建的方舟推理接入点 ID，此处已帮您修改为您的推理接入点 ID
    model="doubao-1-5-pro-32k-250115",
    messages=[
        {"role": "system", "content": "你是一个恐怖、科幻以及悬疑短篇小说家，十分擅长在原有故事的基础上，通过加入句子或者改写部分内容，造成情节的反转与高潮。"},
        {"role": "user", "content": content},
        ],
    )
    return completion.choices[0].message.content

counter = 0
sentence = ''
while counter<=50:
    input()
    if counter == 0:
        sentence = '我今天早上吃了个包子，很好吃'
    print('迭代次数：'+str(counter))
    counter+=1
    print(sentence)
    print('\n')
    sentence = expand_sentences(sentence)