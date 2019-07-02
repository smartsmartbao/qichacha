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
    'Cookie':'QCCSESSID=0hubv37u3kcmr9gmlnri2lsk37; zg_did=%7B%22did%22%3A%20%2216bac1761e5860-055beab97a01cf-e343166-e1000-16bac1761e63dc%22%7D; _uab_collina=156196034234342951222616; acw_tc=65e21c2c15619603424051128e0ea587274cbf02d66c186d8ae914d8c2; hasShow=1; Hm_lvt_3456bee468c83cc63fb5147f119f1075=1561960342,1562047884; zg_de1d1a35bfa24ce29bbf2c7eb17e6c4f=%7B%22sid%22%3A%201562053113897%2C%22updated%22%3A%201562053114454%2C%22info%22%3A%201561960341999%2C%22superProperty%22%3A%20%22%7B%7D%22%2C%22platform%22%3A%20%22%7B%7D%22%2C%22utm%22%3A%20%22%7B%7D%22%2C%22referrerDomain%22%3A%20%22www.qichacha.com%22%2C%22cuid%22%3A%20%22e0d7c8a0c90ee72cfe063fbcb83a7b1f%22%7D; Hm_lpvt_3456bee468c83cc63fb5147f119f1075=1562053115',
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
    cs=wls['A1:A1']
    return cs
#爬取企业详情页信息
def  laoqu(key):
    url = 'https://www.qichacha.com/search?key={}'.format(key)
    with open('qiye.csv', 'a+', encoding='utf-8-sig', newline='') as file:
        b = []
        fenzhi=[]
        gudong=[]
        csv_file = csv.writer(file)
        s = requests.Session()
        r=s.get(url,headers=HEADER)
        response = s.get(url, headers=HEADER).text
        if r.cookies.get_dict():
            s.cookies.update(r.cookies)
        soup = BeautifulSoup(response, 'lxml')
        resl = soup.select('#search-result tr')[0]
        name = resl.select('a')[0].text
        href = resl.select('a')[0]['href']
            # print(href)
        detail_url = 'https://www.qichacha.com' + href
        b.append(key)
        b.append(name)
        detail = requests.get(detail_url, headers=HEADER).text
        detail_soup = BeautifulSoup(detail, 'lxml')
        try:
            zyname = detail_soup.select('#Cominfo table:nth-of-type(2) tr:nth-of-type(8) td:nth-of-type(2)')[
                0].text.replace('\n', '').replace('                                    ', '').replace(
                '                            ', '')
        except:
            zyname='error'
        try:
            tyshbm = "'" + detail_soup.select('#Cominfo table:nth-of-type(2) tr:nth-of-type(3) td:nth-of-type(2)')[
                0].text.strip('\n                ')
        except:
            tyshbm='error'
        try:
            create_time = detail_soup.select('#Cominfo table:nth-of-type(2) tr:nth-of-type(2) td:nth-of-type(4)')[
                0].text.strip('\n                ')
        except:
            create_time='error'
        try:
            jyzc = detail_soup.select('#Cominfo table:nth-of-type(2) tr:nth-of-type(2) td:nth-of-type(2)')[
                0].text.strip('\n                ')
        except:
            jyzc='error'
        try:
            hz_time = detail_soup.select('#Cominfo table:nth-of-type(2) tr:nth-of-type(6) td:nth-of-type(2)')[
                0].text.strip('\n                ')
        except:
            hz_time='error'
        try:
            sshy = detail_soup.select('#Cominfo table:nth-of-type(2) tr:nth-of-type(5) td:nth-of-type(4)')[
                0].text.strip('\n                ')
        except:
            sshy='error'
        try:
            gslx = detail_soup.select('#Cominfo table:nth-of-type(2) tr:nth-of-type(5) td:nth-of-type(2)')[
                0].text.strip('\n                ')
        except:
            gslx='error'
        try:
            ssdq = detail_soup.select('#Cominfo table:nth-of-type(2) tr:nth-of-type(7) td:nth-of-type(2)')[
                0].text.strip('\n                ')
        except:
            ssdq='error'
        try:
            qydz = detail_soup.select('#Cominfo table:nth-of-type(2) tr:nth-of-type(10)  td:nth-of-type(2)')[
                0].text.strip('\n                ').strip('\n                 查看地图  附近公司').strip('\n                 查看地图  附近企业')
        except:
            qydz='error'
        try:
            cbrs = detail_soup.select('#Cominfo table:nth-of-type(2) tr:nth-of-type(8) td:nth-of-type(4)')[
                0].text.strip('\n                ')
        except:
            cbrs='error'
        try:
            zczb = detail_soup.select('#Cominfo table:nth-of-type(2) tr:nth-of-type(1)  td:nth-of-type(2)')[
                0].text.strip('\n                ')
        except:
            zczb='error'
        try:
            jgdm =detail_soup.select('#Cominfo table:nth-of-type(2) tr:nth-of-type(4) td:nth-of-type(4)')[0].text.strip('\n                ')
        except:
            jgdm='error'
        try:
            gslx =detail_soup.select('#Cominfo table:nth-of-type(2) tr:nth-of-type(5) td:nth-of-type(2)')[0].text.strip('\n                ')
        except:
            gslx='error'
        fenzhi_tr=detail_soup.select("section#Subcom table tr")
        try:
            for tr in fenzhi_tr:
                a=tr.select('a')
                for span in a:
                    name=span.text
                    fenzhi.append(name)
        except:
            fenzhi=[]
        gudong_h3=detail_soup.select("section#partnerslist table tr h3")
        try:
            for tr in gudong_h3:
                h3=tr.text
                gudong.append(h3)
            print(gudong)
        except:
            gudong=[]
        dwtz=detail_soup.select('#partnerslist .ntable ntable-odd npth nptd')
        print (dwtz)
        b.append(zyname)
        b.append(tyshbm)
        b.append(create_time)
        b.append(jyzc)
        b.append(hz_time)
        b.append(sshy)
        b.append(gslx)
        b.append(ssdq)
        b.append(qydz)
        b.append(cbrs)
        b.append(zczb)
        b.append(jgdm)
        b.append(gslx)
        b.append(fenzhi)
        b.append(gudong)
        csv_file.writerow(b)
        print(b)
        
if __name__=='__main__':
    c=read_xlsx('test.xlsx','Sheet1')
    for i in c:
        key=i[0].value
        laoqu(key)
        time.sleep(30)


