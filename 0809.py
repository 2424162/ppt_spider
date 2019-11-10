import requests
import urllib3
import re
def request_text(num):
    url = 'http://www.ypppt.com/p/d.php?aid=%s' % (num)
    headers ={'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': 1,
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'
    }
    http = urllib3.PoolManager()
    req = http.request("GET",url = url,headers = headers)
    return req.data.decode()
def request_url(re_return):
    try:
        patt = re.compile('<a href="(.*?.rar)">')
        re_url = re.findall(patt, re_return)
        return re_url[0]
    except:
        print("没有找到网址")
def down_ppt(url,num):
    try:
        file = requests.get(url)
        f = open(str(num)+'.rar',"wb")
        f.write(file.content)
    except:
        print("没有文件")
for i in range(33,10000):
    re_return = request_text(i)
    re_url = request_url(re_return)
    down_ppt(re_url,i)
    print(re_url)