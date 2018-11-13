import requests
from bs4 import BeautifulSoup
import csv
from openpyxl import *
import time
headers = {
    'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cache-control': 'max-age=0',
    'cookie':'acw_tc=3af3b59d15409720232053291ecb948160d9401f65900c872f87acfb08; _uab_collina=154097202360783103187879; zg_did=%7B%22did%22%3A%20%22166cd26a270500-01427d610fedfb-b79183d-e1000-166cd26a27136f%22%7D; QCCSESSID=779aogs2dqat6fjb2d6cq8lqg6; Hm_lvt_3456bee468c83cc63fb5147f119f1075=1540972022,1541040154,1542072670; hasShow=1; zg_de1d1a35bfa24ce29bbf2c7eb17e6c4f=%7B%22sid%22%3A%201542072669369%2C%22updated%22%3A%201542072794744%2C%22info%22%3A%201542072669372%2C%22superProperty%22%3A%20%22%7B%7D%22%2C%22platform%22%3A%20%22%7B%7D%22%2C%22utm%22%3A%20%22%7B%7D%22%2C%22referrerDomain%22%3A%20%22www.baidu.com%22%2C%22cuid%22%3A%20%22e0d7c8a0c90ee72cfe063fbcb83a7b1f%22%7D; Hm_lpvt_3456bee468c83cc63fb5147f119f1075=1542072795',
    'referer': 'https://www.qichacha.com/',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'

}
def read_xlsx(dir):
    wb=load_workbook(dir)
    wls=wb['Sheet1']
    cs=wls['A1:A10']
    return cs
def laoqu(key):
    url = 'https://www.qichacha.com/search?key={}'.format(key)
    try:
        response=requests.get(url,headers=headers).text
        soup=BeautifulSoup(response,'lxml')
        res1=soup.select('.m_srchList tbody tr')
        with open(r'fz.csv','a+',newline='',encoding='utf-8-sig') as file:
            csv_file=csv.writer(file)
            for i in res1:
                b=[]
                name=i.select('a')[0].text
                href=i.select('.ma_h1')[0]['href']
                detail_url='https://www.qichacha.com'+href
                b.append(name)
                if name==key:
                    detail=requests.get(detail_url,headers=headers).text
                    detail_soup=BeautifulSoup(detail,'lxml')
                    tyshxybm=detail_soup.select('#Cominfo table:nth-of-type(2)  tr:nth-of-type(3) td:nth-of-type(2)')[0].text.strip('\n                ')
                    clrq=detail_soup.select('#Cominfo table:nth-of-type(2) tr:nth-of-type(2) td:nth-of-type(4)')[0].text.strip('\n                ')
                    sshy=detail_soup.select('#Cominfo table:nth-of-type(2) tr:nth-of-type(5) td:nth-of-type(4)')[0].text.strip('\n                ')
                    ssdq=detail_soup.select('#Cominfo table:nth-of-type(2) tr:nth-of-type(7) td:nth-of-type(2)')[0].text.strip('\n                ')
                    cbrs=detail_soup.select('#Cominfo table:nth-of-type(2) tr:nth-of-type(8) td:nth-of-type(4)')[0].text.strip('\n                ')
                    qydz=detail_soup.select('#Cominfo table:nth-of-type(2) tr:nth-of-type(10) td:nth-of-type(2)')[0].text.strip('\n                ').strip('\n                 查看地图  附近公司')
                    branch=detail_soup.select('#Subcom .ntable tr')
                    fz_list = []
                    try:
                        for i in branch:
                            fzjg=i.select('a')
                            for j in fzjg:
                                fz=j.text
                                fz_list.append(fz)
                    except:
                        fz_list.append(fz)
                    b.append(tyshxybm)
                    b.append(clrq)
                    b.append(sshy)
                    b.append(ssdq)
                    b.append(cbrs)
                    b.append(qydz)
                    b.append(fz_list)
                    csv_file.writerow(b)
                    print(b)
    except Exception as e:
        print(e)
if __name__ =="__main__":
    c=read_xlsx('new.xlsx')
    for i in c:
        key=i[0].value
        laoqu(key)
        time.sleep(5)






