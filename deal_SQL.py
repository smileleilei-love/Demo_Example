'''
小伙伴学习python
2023/4/13 14:31
'''

import pandas as pd
import openpyxl

df = pd.read_excel('C:\工作内容\客户\厂商型号下cpu核数不匹配/android_manufacturer_model_cpucount_white.xlsx')

# 把第一列 和 第二列是拿出来，并且放到一个list里
col1 = df.iloc[:, 0].tolist()
col2 = df.iloc[:, 1].tolist()
# 利用for 循环把数据一条一条插到sql中
for i in range(len(col1)):
    sql = """insert into dim_prop_source_experiments (`feature_index`,`dim`,`prop`,`minor`,`service_id`) value ("android_manufacturer_model_cpucount_match","%s","%s",1,"DEVICE_PROFILE");""" % (str(col1[i]), str(col2[i]))
    i = i + 1
    write = open('C:\工作内容\SQL/manufacturer_model_cpucount1.sql', 'a+')
    print(sql, file=write)
    write.close()

