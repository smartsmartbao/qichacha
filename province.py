import csv
import requests
import json
import re
a=[]
b=[]
gaode='http://restapi.amap.com/v3/geocode/geo?address={}&output=json&key=2df43ae9994dfea57373568e7aca7881'
pattern=re.compile(r'\d{6}(.*)')
# with open(r'E:\python\网易云数据分析\专利爬取\test.csv','r') as f:
#     r=csv.reader(f)
#     for i in r:
#         s=i[12].split(' ')
#         if len(s)==2:
#             a.append(s[1])
#         else:
#             continue
with open(r'coodinrate.csv','r',encoding='utf-8') as file:
    rows=csv.reader(file)
    with open('test2.csv','a+',newline='',encoding='utf-8-sig')as f:
        writer=csv.writer(f)
        for row in rows:
            try:
                s=row[0]
                r=json.loads(requests.get(gaode.format(s)).text)
                location=r["geocodes"][0]
                province = location['province']
                city = location['city']
                district=location['district']
                row.append(province)
                row.append(city)
                row.append(district)
                writer.writerow(row)
                print(row)

            except Exception as e:
                print(e)
        # for  i in a:
        #     b=[]
        #     r=json.loads(requests.get(gaode.format(i)).text)
        #     location=r["geocodes"][0]['location'].split(',')
        #     lng=location[0]
        #     lat=location[1]
