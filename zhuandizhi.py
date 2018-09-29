import csv
import requests
import json
import re
a=[]
b=[]
tag=0
column=['ids','fenlei_id','name','lawstatus','operationDesc','lawStatusDate','gongkai_riqi','gongkai_num','zhuanli_status','shenqing_riqi','faming_person','shenqing_person','adds','zhaiyao','g_lat','g_lng','lat','lng','address','province','city','district']
gaode='http://restapi.amap.com/v3/geocode/geo?address={}&output=json&key=dd0bd86982932cc1a7a337cc15d415fc'
pattern=re.compile(r'\d{6}(.*)')
# with open(r'E:\python\网易云数据分析\专利爬取\example.csv','r') as f:
#     r=csv.reader(f)
#     for i in r:
#         s=i[12].split(' ')
#         if len(s)==2:
#             a.append(s[1])
#         else:
#             continue
with open(r'test.csv','r',encoding='utf-8') as file:
    rows=csv.reader(file)
    with open('test2.csv','a+',newline='',encoding='utf-8-sig')as f:
        writer=csv.writer(f)
        for row in rows:
            if tag==0:
                writer.writerow(column)
            try:
                s=row[12]
                if s[0].isdigit():
                    address=pattern.findall(s)[0]
                    r=json.loads(requests.get(gaode.format(address)).text)
                    location=r["geocodes"][0]
                    province = location['province']
                    city = location['city']
                    district=location['district']
                    row.append(address)
                    row.append(province)
                    row.append(city)
                    row.append(district)
                    writer.writerow(row)
                    print('插入成功')
                else:
                    r = json.loads(requests.get(gaode.format(address)).text)
                    location = r["geocodes"][0]
                    province = location['province']
                    city = location['city']
                    district = location['district']
                    row.append(province)
                    row.append(city)
                    row.append(district)
                    writer.writerow(row)
                    print('插入成功')
            except:
                print('error')
            tag=tag+1
        # for  i in a:
        #     b=[]
        #     r=json.loads(requests.get(gaode.format(i)).text)
        #     location=r["geocodes"][0]['location'].split(',')
        #     lng=location[0]
        #     lat=location[1]

