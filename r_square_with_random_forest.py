#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  6 13:14:56 2021

@author: cenkakdeniz
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("random_forest_regression_dataset.csv", sep= ";", header=None)
x = df.iloc[:, 0].values.reshape(-1,1)
y = df.iloc[:, 1].values.reshape(-1,1)

from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score

rf = RandomForestRegressor(n_estimators = 100, random_state = 42)


rf.fit(x,y)

y_head = rf.predict(x)
print("r_score: ", r2_score(y, y_head))
