import requests
import time
import json
import sys
import threading
LogIn_URL = "http://seat1.lib.hlju.edu.cn/libseat-ibeacon/wechatIndex?type=index&"
Guard_URL = "http://seat1.lib.hlju.edu.cn/libseat-ibeacon/getUserBookHistory"
Check_URL = "http://seat1.lib.hlju.edu.cn/libseat-ibeacon/checkIn?bookId="
def guard(stu):
    session = requests.session()
    session.get(LogIn_URL + stu['url'])
    resp =  session.get(Guard_URL)
    res_json = resp.json()
    if res_json["params"]["history"][0]["stat"] == "AWAY":
        temp = session.get(Check_URL)
        print(stu["nickname"],temp.json()["content"])
    elif res_json["params"]["history"][1]["stat"] == "AWAY":
        temp = session.get(Check_URL)
        print(stu["nickname"], temp.json()["content"])


if __name__ == '__main__':
    filename = "new.json"
    start = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
    print('         '+start)
    f = open(sys.path[0] + '/' + filename, 'r', encoding='utf8')
    info = json.load(f)
    for i in info['stu']:
        task = threading.Thread(target=guard, args=(i,))
        task.start()

