import requests
import time
import json
import sys
import threading


userAgent = "Mozilla/5.0 (iphone x Build/MXB48T; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/WIFI Language/zh_CN"
header = {
    'User-Agent': userAgent,
}
tomorrow = time.strftime("%Y-%m-%d", time.localtime(86400 + time.time()))
LogIn_URL = "http://seat1.lib.hlju.edu.cn/libseat-ibeacon/wechatIndex?type=index&"
Book_URL = "http://seat1.lib.hlju.edu.cn/libseat-ibeacon/saveBook?"
def BookSeat(stu):
    print("正在为 %s 预约 %s" % (stu['nickname'], stu['seat']))
    session = requests.session()
    session.get(LogIn_URL+stu['url'])
    data = "seatId="+str(stu['seat'])+"&date="+tomorrow+"&start="+str(stu["start"])+"&end="+str(stu["end"])+"&type=1"
    delay = time.strftime("%M:%S", time.localtime(time.time()))
    while delay<"30:05":
        time.sleep(0.01)
        delay = time.strftime("%M:%S", time.localtime(time.time()))
    flag = True
    while flag:
        try:
            resp = session.get(Book_URL+data)
            flag = False
        except Exception:
            
            time.sleep(0.1)
    res_json = resp.json()
    Push = json.loads(res_json)
    status = Push["status"]
    mes = Push["message"]
    print(stu['nickname'],status, mes)
    temp ="##### "+str(stu['nickname'])+"   "+status+" "+mes+"<br>"
    Mes.append(temp)
    end = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
    print("-----------", stu['nickname'], end +'-----End---------' )


if __name__ == '__main__':
    filename = "new.json"
    start = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
    print('         '+start)
    f = open(sys.path[0] + '/' + filename, 'r', encoding='utf8')
    info = json.load(f)
    list = []
    for i in info['stu']:
        task =threading.Thread(target=BookSeat,args=(i,))
        task.start()
        list.append(task)

    Mes = []
    two = True
    while(two):
        count = len(list)
        for j in list:
            if j.isAlive():
                pass
            else:
                count = count - 1
        if count == 0:
            two = False
        time.sleep(0.5)
    time.sleep(3)
    Push_str = ""
    count = 0
    for i in Mes:
        Push_str = Push_str+i
        if "success" in i:
            count = count+1
    data = {
        "text": "seat "+"__"+str(count),
        "desp":Push_str
    }
    #Push_URL = "https://sc.ftqq.com/SCU66440T1cc7ecd62f761dec84d80955b51e85955dcd677c491b9.send?text=www"
    #requests.post(Push_URL, data)
