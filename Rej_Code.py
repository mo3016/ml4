# -*- coding: utf-8 -*-
"""
Created on Thu Dec 14 23:47:07 2017

@author: Rejpal
"""

# loading libraries
import pandas as pd
import numpy as np
import scipy as scipy
from sklearn.cluster import KMeans

#import dataset
df = pd.read_table('EnglandPlayers.csv', sep=',')
df1 = df.iloc[:,2:]

#apply clusters, set to 4
kmeans = KMeans(n_clusters=4)

#training model
model = kmeans.fit(df1)

#y prediction
players = df.iloc[:,0:2]
labels = kmeans.predict(df1)
se = pd.Series(labels)
players['Groups']=se.values

#We store the clusters
clus0 = players.loc[players.Groups == 0]
clus1 = players.loc[players.Groups == 1]
clus2 = players.loc[players.Groups == 2]
clus3 = players.loc[players.Groups == 3]

k_list = [clus0.values, clus1.values,clus2.values]

#centroids
centroids = pd.DataFrame(kmeans.cluster_centers_)
centroids.columns=list(df1)


# Crossing = 0, Sprint Speed = 11, Long Shots = 19, etc...
centroids_selected = centroids.loc[:,['Crossing','Sprint speed','Long shots','Aggression','Marking','Finishing','GK handling']]

new_sample = pd.DataFrame(columns=centroids_selected.columns)

new_sample.loc[0]=[0,0,0,0,0,0,500]


min_dist_ind=-1
min_dist=0
for i in range(len(centroids_selected)):
    dist = scipy.spatial.distance.cdist(centroids_selected.iloc[[i],:], new_sample, metric='euclidean')
    if min_dist==0 or dist[0,0]<= min_dist:
        min_dist=dist[0,0]
        min_dist_ind=i
        
    

    
