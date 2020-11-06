# coding=utf-8

import requests
import datetime


def send(value):
    url = "https://oapi.dingtalk.com/robot/send?access_token=2f3ffa25f4d079a19b09820ffe15fe87f0eed9c0211153eb6d129fb795c9c8e3"
    now_time = datetime.datetime.now().strftime('%Y-%m-%d')
    data = {
        "msgtype": "text",
        "text": {
            "content": str(now_time) +"   "+ "资讯:\n" + value +"\n@所有人"
        }
    }
    header = {"Content-Type": "application/json"}
    r = requests.post(url, headers=header, json=data)

    print(r.text)


def getmessage():
    message = []
    url = 'https://it.sohu.com/?spm=smpc.content.nav.9.1584602783660uIFWpoR'

    r = requests.get(url)
    import re
    # 正则：匹配换行模式，re.DNTALL
    # 正则：懒惰模式?
    s = re.findall('(?s)(z-c-block-list-item-first">.*?target="_blank">)(.*?)(</a>)', r.text, re.DOTALL)
    for x in s:
        message.append(str(s.index(x) + 1) + '.' + x[1])
    return '\n'.join(message)


if __name__ == '__main__':
    message = getmessage()
    send(message)
