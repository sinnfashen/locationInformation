import requests
import re
import csv


companylist = []
with open('sample.csv') as f:
    reader = csv.reader(f)
    for row in reader:
        companylist.append(row[1])
for company in companylist:
    print(company)
    url = 'http://www.baidu.com/s?ie=utf-8&wd={}%20%E9%82%AE%E7%BC%96'.format(company)
    req = requests.get(url)
    grs = re.findall(r'<em>邮编<\/em>:(\d+)', req.text)
    print(grs.__len__())
