import requests
import re
import csv
from bs4 import BeautifulSoup

def get_postal_code(text):
    ans = []
    grs = re.findall(r'[\u4e00-\u9fa5:：]\s*(\d{6})\D', text)
    for gr in grs:
        ans.append(gr)
    ans = list(set(ans))
    return ans


def get_bs(company):
    url = 'http://www.baidu.com/s?ie=utf-8&wd={}%20%E9%82%AE%E7%BC%96'.format(company)
    req = requests.get(url)
    be = BeautifulSoup(req.text, 'html.parser')
    return be

companylist = []
with open('sample.csv') as f:
    reader = csv.reader(f)
    for row in reader:
        companylist.append(row[1])

for company in companylist:
    print(company)
    ans = []
    be = get_bs(company)
    ls = be.find_all('div', 'result c-container ')
    for i in ls:
        ans.extend(get_postal_code(i.text))
    ans = list(set(ans))
    if ans.__len__() > 1:
        ans = []
        for i in ls:
            if i.text.find('北京') != -1:
                ans.extend(get_postal_code(i.text))
        ans = list(set(ans))
        if ans.__len__() != 1:
            print("error")
            continue
    if ans.__len__() < 1:
        print("error")
        continue
    print(ans[0])



