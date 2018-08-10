from selenium import webdriver
import requests
from bs4 import BeautifulSoup
import csv
from openpyxl import *
import time
import re
headers={
    'authority': 'www.qichacha.com',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Cookie':'acw_tc=AQAAAJhyKnwckg4A1SlgesRNbqeyht9z; PHPSESSID=3kfen93csls24h21cml2joegr4; zg_did=%7B%22did%22%3A%20%22164f9f7c7dfab6-01260f1b3fffca-47e1039-e1000-164f9f7c7e01de%22%7D; Hm_lvt_3456bee468c83cc63fb5147f119f1075=1533202123; _uab_collina=153320212355925420122744; _umdata=6AF5B463492A874D9ACB30D29B178D6080F4D1C36B0C0BF7061E6240C49EC89A351B54D07EA1962ACD43AD3E795C914CB3C200DD7F76A6E92D103E125422A92A; hasShow=1; Hm_lpvt_3456bee468c83cc63fb5147f119f1075=1533202213; zg_de1d1a35bfa24ce29bbf2c7eb17e6c4f=%7B%22sid%22%3A%201533202122723%2C%22updated%22%3A%201533202226438%2C%22info%22%3A%201533202122726%2C%22superProperty%22%3A%20%22%7B%7D%22%2C%22platform%22%3A%20%22%7B%7D%22%2C%22utm%22%3A%20%22%7B%7D%22%2C%22referrerDomain%22%3A%20%22www.qichacha.com%22%2C%22cuid%22%3A%20%22ca2b7b8a0021b693099e3ef4cccb3b55%22%7D',
    'Referer': 'https://www.qichacha.com/',
    'Upgrade-Insecure-Requests':'1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36'
}
# pattern=re.compile('.*?_(.*?).html')
def read_xlsx(dir):
    wb=load_workbook(dir)
    wls=wb['Sheet1']
    cs=wls['A254:A5404']
    return cs
def laoqu(key):
    url='https://www.qichacha.com/search?key={}'.format(key)
    try:
        re1=requests.get(url,headers=headers).text
        soup=BeautifulSoup(re1,'lxml')
        result1=soup.select('#searchlist .m_srchList tbody')[0]
        r_list=result1.select('tr')
        with open(r'test_new.csv','a+',newline='',encoding='utf-8-sig') as file:
            csv_file=csv.writer(file)
            for i in r_list:
                b=[]
                name=i.select('a')[0].text
                body=i.select('.m-t-xs')[0].text.replace("\n                                                                                    ",'').replace('                                                                                    ','').replace('\n                                      ','').replace('                                                                        ','').replace('                                    ','')
                mail=i.select('.m-t-xs')[1].text.replace('\n                                     ','')
                address=i.select('.m-t-xs')[2].text.replace('\n                                     ','').replace('\n                                  ','')
                href=i.select('.ma_h1')[0]['href']
                detail_url='https://www.qichacha.com'+href
                b.append(name)
                b.append(body)
                b.append(mail)
                b.append(address)
                if name==key:
                    re2=requests.get(detail_url,headers=headers).text
                    soup2=BeautifulSoup(re2,'lxml')
                    result2=soup2.select('#Cominfo .ntable')[1].select('tr')[4]
                    hy=result2.select('td')[3].text.replace('\n                ','').replace('\n            ','')
                    b.append(hy)
                    # unique=pattern.findall(href)
                    asset=detail_url+'#assets'
                    re3=requests.get(asset,headers=headers).text
                    soup3=BeautifulSoup(re3,'lxml')
                    try:
                        zhuanli=soup3.select('a[data-pos="zhuanlilist"]')[0].select('.text-primary')[0].text
                        b.append(zhuanli)
                    except:
                        b.append(0)
                    csv_file.writerow(b)
                    print(b)
    except:
        print('error')

c=read_xlsx('new.xlsx')
for i in c:
    key=i[0].value
    laoqu(key)
    time.sleep(5)
