import pandas as pd
import re
data = pd.read_excel(r'51job.xls',sheet_name='Job')
result = pd.DataFrame(data)
#消除空信息
a = result.dropna(axis=0,how='any')
#处理职位
b = u'数据'
number = 1
li = a['职位']
for i in range(0,len(li)):
    try:
        if b in li[i]:
            print(number,li[i])
            number+=1
        else:
            a = a.drop(i,axis=0)
    except:
        pass

# 招聘地点
c = u'异地招聘'
number = 1
li = a['公司地点']
for i in range(0, len(li)):
    try:
        if c in li[i]:
            a = a.drop(i, axis=0)
        else:
            print(number, li[i])
            number += 1
    except:
        pass

#处理工资单位不统一
b3 =u'万/年'
b4 =u'千/月'
b5 =u'万/月'
l = a['序号']
li3 = a['薪资']
for i in range(1,len(l)):
    try:
        if b3 in li3[i]:
            x = re.findall(r'\d*\.?\d+',li3[i])
            min_ = format(float(x[0])/12,'.2f')
            max_ = format(float(x[1])/12,'.2f')
            li3[i] = str(min_+'-'+max_)
        if b4 in li3[i]:
            x = re.findall(r'\d*\.?\d+',li3[i])
            min_ = format(float(x[0])/10,'.2f')
            max_ = format(float(x[1])/10,'.2f')
            li3[i] = str(min_+'-'+max_)
        if b5 in li3[i]:
            x = re.findall(r'\d*\.?\d+', li3[i])
            min_ = format(float(x[0]) / 1, '.2f')
            max_ = format(float(x[1]) / 1, '.2f')
            li3[i] = str(min_ + '-' + max_)
        print(i,li3[i])
    except:
        pass


#保存新文件
a.to_excel('new_51job_1.xls',  index=False)
d = a.drop(['序号','职位','公司名称','发布时间'],axis=1)
d.to_csv('new_51job_1.csv',  index=False)


