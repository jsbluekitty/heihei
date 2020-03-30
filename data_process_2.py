import pandas as pd
import re
data = pd.read_excel(r'new_51job_1.xls')
a = pd.DataFrame(data)
li3 = a['薪资']
b3 = u'万/年'
b4 = u'千/月'
b5 = u'万/月'
number = 1
for i in range(0, len(li3)):
    try:
        if b5 in li3[i]:
            a = a.drop(i, axis=0)
        elif b3 in li3[i]:
            a = a.drop(i, axis=0)
        elif b4 in li3[i]:
            a = a.drop(i, axis=0)
        else:
            print(number, li3[i])
            number += 1
    except:
        pass

a.to_excel('new_51job_2.xls',  index=False)

d = a.drop(['序号','职位','公司名称','发布时间'],axis=1)
d.to_csv('new_51job_2.csv',  index=False)

