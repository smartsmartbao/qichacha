import requests
from openpyxl import *
import json
import csv
GAODE_API='http://restapi.amap.com/v3/geocode/geo?address={}&output=json&key=2df43ae9994dfea57373568e7aca7881'
column=['address','lng','lat']
def read_excel(dir):
    wb=load_workbook(dir)
    wls=wb['Sheet0']
    address=wls['A1:A20']#有多少行写多少个
    return address
path='20171010.xlsx'

def gaode_zhuanhuan(address):
    with open('coodinrate.csv','a+',newline='',encoding='utf-8-sig') as f:
        csv_file=csv.writer(f)
        b=[]
        try:
            coordinate=json.loads(requests.get(GAODE_API.format(address)).text)
            location=coordinate["geocodes"][0]['location'].split(',')
            lng=location[0]
            lat=location[1]
            b.append(address)
            b.append(lng)
            b.append(lat)
            csv_file.writerow(b)
            print (b)
        except Exception as e:
            print(e)
if __name__ == '__main__':
    key=read_excel(path)
    for i in key:
        address=i[0].value
        gaode_zhuanhuan(address)
