import urllib.request
import re
import urllib.parse
import requests
import xlwt
from lxml import etree
import os
header = {
    'Host': 'search.51job.com',
    'Referer': 'https://mkt.51job.com/tg/sem/pz_2018.html?from=baidupz',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) 37abc/2.0.6.16 Chrome/60.0.3112.113 Safari/537.36'
}

def getfront(page, item):
    result = urllib.parse.quote(item)
    ur1 = result+',2,' + str(page)+'.html'
    ur2 = 'http://search.51job.com/list/000000,000000,0000,00,9,99,'
    res = ur2+ur1
    a = urllib.request.urlopen(res)
    html = a.read().decode('gbk')
    return html


def getInformation(html):
    reg = re.compile(r'class="t1 ">.*? <a target="_blank" title="(.*?)" href="(.*?)".*? <span class="t2"><a target="_blank" title="(.*?)" href="(.*?)".*?<span class="t3">(.*?)</span>.*?<span class="t4">(.*?)</span>.*?<span class="t5">(.*?)</span>.*?', re.S)
    items = re.findall(reg, html)
    return items


excel1 = xlwt.Workbook()

sheet1 = excel1.add_sheet('Job', cell_overwrite_ok=True)
sheet1.write(0, 0, '序号')
sheet1.write(0, 1, '职位')
sheet1.write(0, 2, '公司名称')
sheet1.write(0, 3, '公司地点')
sheet1.write(0, 4, '薪资')
sheet1.write(0, 5, '发布时间')


number = 1
pe = input('请输入爬取页数：')
pg = int(pe) + 1
item = input('请输入关键字：')
for j in range(1, pg):
    try:
        print("正在爬取第"+str(j)+"页数据...")
        html = getfront(j, item)
        for i in getInformation(html):
            try:
                url1 = i[1]
                url2 = i[3]
                res1 = requests.get(url1).text
                res2 = requests.get(url2).text
                s1 = etree.HTML(res1)
                s2 = etree.HTML(res2)

                print(i[0], i[2], i[4], i[5], i[6])

                sheet1.write(number, 0, number)
                sheet1.write(number, 1, i[0])
                sheet1.write(number, 2, i[2])
                sheet1.write(number, 3, i[4])
                sheet1.write(number, 4, i[5])
                sheet1.write(number, 5, i[6])
                number += 1
                excel1.save("51job.xls")
            except:
                pass
    except:
        if len(i[0]) == 0:
            break

