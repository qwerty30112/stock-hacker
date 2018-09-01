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
    if os.path.isfile("cnyes/%s.html"%k):
        print ('aaaa')
        continue
    #r=requests.post("http://pchome.megatime.com.tw/stock/sto0/ock3/sid%s.html"%k,data={"is_check":"1"})
    #r.encoding="utf8"
    while True:
        s=os.popen("curl "+"https://www.cnyes.com/twstock/ps_pv_time/%s.htm"%k).read()
        if len(s)>0:break
    f=open("cnyes/%s.html"%k,"w")
    f.write(s)
    f.close()