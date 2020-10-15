import requests
from bs4 import BeautifulSoup
from time import sleep
import json

def getHtml(url):
    try:
        return requests.get('http://www.mca.gov.cn//article/sj/xzqh/2020/2020/2020092500801.html')
        pass
    except expression as identifier:
        return getHtml(url)
        pass

r = getHtml('http://www.mca.gov.cn//article/sj/xzqh/2020/2020/2020092500801.html')
soup = BeautifulSoup(r.content, 'html.parser').body
table = soup.div.table
provinceNow = []  # 当前所处的省
cityNow = []      # 当前所处的市
allCity = []      # 所有的城市


for city in table.find_all('tr',height = '19'):
    # 拆解城市
    # 如果是省 则更新当前省 如果是市 则更新当前市 如果是区 则加入表
    # 后四位为0的就是省 后两位为0的是市
    td = city.find_all('td')
    if td[1].string[-4:] == '0000':
        provinceNow = [td[2].text, td[1].text]
        cityNow = []  #清空city 防止出现直辖市导致的错误
        # print(provinceNow)
    elif td[1].string[-2:] == '00':
        cityNow = [td[2].text[1:], td[1].text]
        # print(cityNow)
    else: 
        districNow = td[2].text[3:]
        if cityNow == []:
            district = {'代码': td[1].text,
                        '名称': provinceNow[0] + districNow,
                        '省级代码': provinceNow[1],
                        '市级代码': td[1].text,
                        '县级代码': td[1].text
            }
            pass
        else:
            district = {'代码': td[1].text,
                        '名称': provinceNow[0] + cityNow[0] + districNow,
                        '省级代码': provinceNow[1],
                        '市级代码': cityNow[1],
                        '县级代码': td[1].text
            }
            pass
        # print(district)
        allCity.append(district)
        # sleep(5)
jsonArr = json.dumps(allCity, ensure_ascii=False)
print(jsonArr)

f = open('city.json', 'w', encoding='utf-8')
f.write(jsonArr)
f.close()