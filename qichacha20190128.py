from bs4 import BeautifulSoup
import csv
from openpyxl import *
import time
import requests
#cookie
HEADER={
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Cookie': 'QCCSESSID=7nlop1tmrmrn9op8kpafupgvj4; Hm_lvt_3456bee468c83cc63fb5147f119f1075=1548659941; zg_did=%7B%22did%22%3A%20%2216893535e3b5c8-06e919175f5cf1-b781636-e1000-16893535e3c234%22%7D; hasShow=1; _uab_collina=154865994135433871272764; saveFpTip=true; acw_tc=b4a39f4215486599414191812e476141000bb47cd9e83bb675d79d892a; zg_de1d1a35bfa24ce29bbf2c7eb17e6c4f=%7B%22sid%22%3A%201548659940929%2C%22updated%22%3A%201548659980507%2C%22info%22%3A%201548659940935%2C%22superProperty%22%3A%20%22%7B%7D%22%2C%22platform%22%3A%20%22%7B%7D%22%2C%22utm%22%3A%20%22%7B%7D%22%2C%22referrerDomain%22%3A%20%22www.baidu.com%22%2C%22cuid%22%3A%20%22e0d7c8a0c90ee72cfe063fbcb83a7b1f%22%7D; Hm_lpvt_3456bee468c83cc63fb5147f119f1075=1548659981',
    'Host': 'www.qichacha.com',
    'Pragma': 'no-cache',
    'Referer': 'https://www.qichacha.com/',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
}
#读取企业xlsx
def read_xlsx(dir,sheetname):
    wb=load_workbook(dir)
    wls=wb[sheetname]
    cs=wls['A2:A2']
    return cs
#爬取企业详情页信息
def  laoqu(key):
    url = 'https://www.qichacha.com/search?key={}'.format(key)
    try:
        response = requests.get(url, headers=HEADER).text
        soup=BeautifulSoup(response,'lxml')
        resl=soup.select('#search-result tr')[0]
        name=resl.select('a')[0].text
        href=resl.select('a')[0]['href']
        #print(href)
        with open('qiye.csv','a+',encoding='utf-8-sig',newline='') as file:
            b=[]
            csv_file=csv.writer(file)
            detail_url='https://www.qichacha.com'+href
            b.append(key)
            b.append(name)
            detail=requests.get(detail_url,headers=HEADER).text
            detail_soup=BeautifulSoup(detail,'lxml')
            zyname=detail_soup.select('#Cominfo table:nth-of-type(2) tr:nth-of-type(8) td:nth-of-type(2)')[0].text.replace('\n','').replace('                                    ','').replace('                            ','')
            tyshbm="'"+detail_soup.select('#Cominfo table:nth-of-type(2) tr:nth-of-type(3) td:nth-of-type(2)')[0].text.strip('\n                ')
            create_time=detail_soup.select('#Cominfo table:nth-of-type(2) tr:nth-of-type(2) td:nth-of-type(4)')[0].text.strip('\n                ')
            jyzc=detail_soup.select('#Cominfo table:nth-of-type(2) tr:nth-of-type(2) td:nth-of-type(2)')[0].text.strip('\n                ')
            hz_time=detail_soup.select('#Cominfo table:nth-of-type(2) tr:nth-of-type(6) td:nth-of-type(2)')[0].text.strip('\n                ')
            sshy=detail_soup.select('#Cominfo table:nth-of-type(2) tr:nth-of-type(5) td:nth-of-type(4)')[0].text.strip('\n                ')
            gslx=detail_soup.select('#Cominfo table:nth-of-type(2) tr:nth-of-type(5) td:nth-of-type(2)')[0].text.strip('\n                ')
            ssdq=detail_soup.select('#Cominfo table:nth-of-type(2) tr:nth-of-type(7) td:nth-of-type(2)')[0].text.strip('\n                ')
            qydi=detail_soup.select('#Cominfo table:nth-of-type(2) tr:nth-of-type(10)  td:nth-of-type(2)')[0].text.strip('\n                ').strip('\n                 查看地图  附近公司')
            cbrs=detail_soup.select('#Cominfo table:nth-of-type(2) tr:nth-of-type(8) td:nth-of-type(4)')[0].text.strip('\n                ')
            zczb=detail_soup.select('#Cominfo table:nth-of-type(2) tr:nth-of-type(1)  td:nth-of-type(2)')[0].text.strip('\n                ')
            b.append(zyname)
            b.append(tyshbm)
            b.append(create_time)
            b.append(jyzc)
            b.append(hz_time)
            b.append(sshy)
            b.append(gslx)
            b.append(ssdq)
            b.append(qydi)
            b.append(cbrs)
            b.append(zczb)
            csv_file.writerow(b)
            print(b)
    except Exception as e :
        print(e)

if __name__=='__main__':
    c=read_xlsx('201505.xlsx','Sheet1')
    for i in c:
        key=i[0].value
        laoqu(key)
        time.sleep(20)


