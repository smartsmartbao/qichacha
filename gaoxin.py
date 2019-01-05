from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re
import requests
from bs4 import BeautifulSoup
import os
url='http://www.innocom.gov.cn/gxjsqyrdw/index.shtml'
driver=webdriver.Chrome()
headers={
    'Cookie': 'yfx_c_g_u_id_10005562=_ck18112115571411575490618347741; yfx_f_l_v_t_10005562=f_t_1542787034149__r_t_1542787034149__v_t_1542787034149__r_c_0',
    'Host': 'www.innocom.gov.cn',
    'Proxy-Connection': 'keep-alive',
    'Upgrade-Insecure-Requests':'1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36'
}
def get_resource(url):
    driver.get('http://www.innocom.gov.cn/gxjsqyrdw/index.shtml')
    driver.maximize_window()
    driver.switch_to.frame(driver.find_element_by_xpath('//*[@id="con_four_1"]/iframe'))
    beijing=WebDriverWait(driver,25).until(EC.presence_of_element_located((By.XPATH,'//*[@id="tree_1_span"]')))
    beijing.click()
    resource=driver.page_source
    return resource
def get_pattern(resource):
    pattern=re.compile('var json =(.*?);')
    t=pattern.findall(resource)
    return t[0]
lst=get_pattern(get_resource(url))
pattern1=re.compile('file : (.*?),')
url_lst=pattern1.findall(lst)
def get_detail(lst):
    for i in lst:
        try:
            sum=''
            j=i.strip("'")
            req=requests.get(j,headers=headers).text
            soup=BeautifulSoup(req,'lxml')
            url=soup.select('#content a')[0]['href']
            url_detail=j.split('/')[:-1]
            url_detail.append(url)
            for j in url_detail:
                if j=='http:':
                    sum=j+'//'
                elif j=='':
                    continue
                else:
                    sum=sum+j+'/'
            url_1=sum.strip('/')
            filename=url_1.split('/')[-1]
            path=os.path.join('pdf',filename)
            content=requests.get(url_1,headers).content
            with open(path,'wb')as f:
                f.write(content)
                print('下载成功')
        except Exception as e:
            print(e)

get_detail(url_lst)

# print(get_pattern(get_resource(url)))
