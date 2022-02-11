#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  4 01:17:49 2021

@author: cenkakdeniz
"""
import pandas as pd
dictionary = {"NAME":["ali","veli","kenan","hilal","ayse","evren"],
              "AGE":[15,16,17,33,45,66 ],
              "MAAS":[100,150,240,350,110,220,]}
dataFrame1 = pd.DataFrame(dictionary)

print(dataFrame1.head)
print(dataFrame1.columns)
print(dataFrame1.info())
print(dataFrame1.describe()) # numeric feature = columns(age,maas)
print(dataFrame1["NAME"])
dataFrame1["new_future"]=[-1,-2,-3,-4,-5,-6]
print(dataFrame1["new_future"])
print(dataFrame1.loc[:3, "NAME":"MAAS"])
#% %FİLTERING
filtre1 = dataFrame1.MAAS > 200
filtre2 = dataFrame1.AGE < 20
filteredData = dataFrame1[filtre1 & filtre2]
# %% LIST COMPREHENSION

mean_value = dataFrame1.MAAS.mean()
print(mean_value)
dataFrame1["maas_seviyesi"] = ["dusuk" if(mean_value > each) else "yuksek "for each in dataFrame1.MAAS]
# %% DROP AND CONCATENATING

#dataFrame1.drop(["new_future"], axis=1, inplace=True)

data1 = dataFrame1.head()
data2 = dataFrame1.tail()
#vertical
data_concat = pd.concat([data1, data2], axis=0)

#horizontal
maas = dataFrame1.MAAS
age = dataFrame1.AGE

data_horizontal_concat = pd.concat([maas,age],axis=1)

#%% TRANSFORMING DATA
dataFrame1["list_comp"] = [each*2 for each in dataFrame1.AGE]

#apply
def multiply(age):
    return age*2
dataFrame1["apply_method"] = dataFrame1.AGE.apply(multiply)