# -*- coding: utf-8 -*-
"""
Created on Thu Dec 14 21:49:47 2017

@author: Yiting
"""
# import libraries
import scipy
import numpy as np
import pandas as pd
from sklearn.cluster import KMeans

# Question 4

# read csv
df = pd.read_csv('EnglandPlayers.csv')

# samples with attributes
samples = df.iloc[:, 2:]

# use KMeans model, cluster players in to four groups with different labels
model = KMeans(n_clusters = 4)
model.fit(samples)
labels = model.predict(samples)
df["labels"] = labels
# df.to_csv('EnglandPlayersWithLabels.csv',index=False)

# Question 5
# Maybe different positions?

# Question 6

# calculate centroids and select attributes 
# Crossing = 0, Sprint Speed = 11, Long Shots = 19, etc...
centroids = model.cluster_centers_
centroids_selected = centroids[:, [0, 11, 19, 20, 26, 1, 30]]

# new sample's available attributes
new_sample = np.array([[45, 40, 35, 45, 60, 40, 15]])

# calculate distance to the cluster centroids
dist = scipy.spatial.distance.cdist(centroids_selected, new_sample, metric='euclidean')
dist

# assign the new sample to the group with shortest distance!