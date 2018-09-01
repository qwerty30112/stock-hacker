import requests
import os
import json
import twstock

d=twstock.codes

h={}

for k in d:
    info=d[k]
    if info.type!="股票":continue
    #print (k,info.name,info.type)
    h[k]=info.name



s=open("stock.json").read()
j=json.loads(s)

for k in j:
    #print (k,j[k])
    h[k]=j[k]


i=0




for k in h:
    i+=1
    print (i,len(h))
    print (k,h[k])
    print ("")
    if os.path.isfile("wantgoo/%s.json"%k):
        print ('aaaa')
        continue
    #r=requests.post("http://pchome.megatime.com.tw/stock/sto0/ock3/sid%s.html"%k,data={"is_check":"1"})
    #r.encoding="utf8"
    while True:
        s=os.popen("curl 'https://api.wantgoo.com/%E8%A1%8C%E5%8B%95%E7%89%88%E6%9C%AC_%E8%82%A1%E7%A5%A8/%E5%80%8B%E8%82%A1%E7%B7%9A%E5%9C%96/%E5%8D%B3%E6%99%82%E7%B7%9A%E5%9C%96%E8%B3%87%E6%96%99?StockNo="+k+"&type=2&days=5' -H 'Origin: https://www.wantgoo.com' -H 'Accept-Encoding: gzip, deflate, br' -H 'Accept-Language: en-US,en;q=0.9,zh-TW;q=0.8,zh;q=0.7' -H 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.117 Safari/537.36' -H 'Accept: */*' -H 'Referer: https://www.wantgoo.com/stock/00637l' -H 'Connection: keep-alive' --compressed").read()
        if len(s)>0:break
    f=open("wantgoo/%s.json"%k,"w")
    f.write(s)
    f.close()