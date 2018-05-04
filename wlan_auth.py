# coding: utf-8
# author: observer

import requests, json ,os

a = requests.session()
test_url = "http://detectportal.firefox.com/success.txt"

with open("config.json", 'rb') as f:
    user = json.load(f)
    username = user['username']
    pwd = user['pwd']

respond = a.get(test_url)


def auth(i):
    respond = a.get(test_url)
    if 'script' in respond.text:
        print("正在尝试第"+str(i)+"次认证...")
        url = '''http://172.31.20.2:8080/eportal/webGateModeV2.do?method=login&param=true&'''
        url += respond.text.split("'")[1].split("?")[1]
        a.post(url, data={"username": username, "pwd": pwd})
        if i==5:
            print("Good Game~")
            return
        auth(i+1)
    elif respond.text == 'success\n':
        print("Connect ok!")
        
auth(1)
os.system("pause")