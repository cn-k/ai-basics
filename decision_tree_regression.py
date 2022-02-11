#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  5 17:31:20 2021

@author: cenkakdeniz
"""
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv("decision_tree_regression_dataset.csv", sep=";", header=None)

x = df.iloc[:,0].values.reshape(-1,1)
y = df.iloc[:,1].values.reshape(-1,1)

#%% decision treee regression

from sklearn.tree import DecisionTreeRegressor

tree_reg = DecisionTreeRegressor()

tree_reg.fit(x,y)

print(tree_reg.predict([[6]]))
print(tree_reg.predict([[5.5]]))

x_ = np.arange(min(x),max(x),0.01).reshape(-1,1)
y_head = tree_reg.predict(x_)


#%% visualize

plt.scatter(x,y,color="red")
plt.plot(x_, y_head, color="green")
plt.xlabel("tribun_level")
plt.ylabel("ücret")
plt.show()

#%%
print(y_head)