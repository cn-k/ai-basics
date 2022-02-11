#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  4 15:04:04 2021

@author: cenkakdeniz
"""
import pandas as pd

df = pd.read_csv("iris.csv")

print(df.columns)

print(df.Species.unique())

print(df.info())

print(df.describe())

setosa = df[df.Species == "Iris-setosa"]
versicolor = df[df.Species == "Iris-versicolor"]

print(setosa.describe())
print(versicolor.describe())

# %%

import matplotlib.pyplot as plt
df1 = df.drop(["Id"], axis = 1)

setosa = df[df.Species == "Iris-setosa"]
versicolor = df[df.Species == "Iris-versicolor"]
virginica = df[df.Species == "Iris-virginica"]

plt.plot(setosa.Id, setosa.PetalLengthCm, color ="red", label="setosa")
plt.plot(versicolor.Id, versicolor.PetalLengthCm, color ="green", label="versicolor")
plt.plot(virginica.Id, virginica.PetalLengthCm, color ="blue", label="virginica")
plt.xlabel("Id")
plt.ylabel("PetalLenghtCm")
plt.legend()
plt.show()

# %% 
setosa = df[df.Species == "Iris-setosa"]
versicolor = df[df.Species == "Iris-versicolor"]
virginica = df[df.Species == "Iris-virginica"]

plt.scatter(setosa.PetalLengthCm, setosa.PetalWidthCm, color="red", label="setosa")
plt.scatter(versicolor.PetalLengthCm, versicolor.PetalWidthCm , color="green", label="versicolor")
plt.scatter(virginica.PetalLengthCm, virginica.PetalWidthCm, color="blue", label="virginica")

plt.legend()
plt.xlabel("PetalLengthCm")
plt.ylabel("PetalWidthCm")
plt.title("scatter plt")
plt.show()

# %% histogram
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("iris.csv")
setosa = df[df.Species == "Iris-setosa"]
versicolor = df[df.Species == "Iris-versicolor"]
virginica = df[df.Species == "Iris-virginica"]

plt.hist(setosa.PetalLengthCm, bins=50)
plt.xlabel("PetalLengthCm values")
plt.ylabel("frequency")
plt.title("hist")
plt.show()

#%%
import numpy as np

x = np.array([1,2,3,4,5,6,7])

y = x * 2 + 5
plt.bar(x,y)
plt.title("bar plot")
plt.xlabel("x")
plt.ylabel("y")
plt.show()
