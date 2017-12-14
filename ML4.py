# -*- coding: utf-8 -*-
"""
Created on Thu Dec 14 15:41:48 2017

@author: marko
"""

import pandas as pd

from sklearn.cluster import KMeans

import numpy as np

import matplotlib.pyplot as plt

#set up dataframe
df = pd.read_csv('EnglandPlayers.csv')
df1 = pd.read_csv('EnglandPlayers.csv')
del df1['name']
del df1['link']


#makes cluster
kmeans = KMeans(n_clusters=4, random_state=0).fit(df1)

#check single player
kmeans.predict(df1.loc[[9]])

#Assign clusters to all players
df['A'] = pd.Series(kmeans.predict(df1), index=df.index)


#plot based on an attribute
plt.scatter(df['Heading accuracy'],df['A'])
plt.show()



# 1 = goalkeeper, 2 = defender,  3 = forward, 0= midfield