#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  6 12:46:18 2021

@author: cenkakdeniz
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("random_forest_regression_dataset.csv", sep= ";", header=None)
x = df.iloc[:, 0].values.reshape(-1,1)
y = df.iloc[:, 1].values.reshape(-1,1)

from sklearn.ensemble import RandomForestRegressor

rf = RandomForestRegressor(n_estimators = 100, random_state = 42)


rf.fit(x,y)
print("değere karşılık gelen fiyat: ", rf.predict([[7.8]]))

x_ = np.arange(min(x), max(x), 0.01).reshape(-1,1)
y_head = rf.predict(x_)
#%%
plt.scatter(x,y,color="red")
plt.plot(x_,y_head,color="green")
plt.xlabel("tribun level") 
plt.ylabel("ucret")
plt.show()
