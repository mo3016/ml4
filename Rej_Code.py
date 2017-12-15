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
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3d

#import dataset
df = pd.read_table('EnglandPlayers.csv', sep=',')
df1 = df.iloc[:,2:]

#apply clusters, set to 4
kmeans = KMeans(n_clusters=4)

#training model
model = kmeans.fit(df1)

#y prediction
players = df.iloc[:,:]
labels = kmeans.predict(df1)
se = pd.Series(labels)
players['Groups']=se.values

#We store the clusters
clus0 = players.loc[players.Groups == 0]
clus1 = players.loc[players.Groups == 1]
clus2 = players.loc[players.Groups == 2]
clus3 = players.loc[players.Groups == 3]

k_list = [clus0.values, clus1.values,clus2.values]

#plot based on an attribute
plt.clf()
plt.figure(figsize=(8,8))
grp0 = plt.scatter(df[df['Groups']==0]['GK reflexes'], df[df['Groups']==0]['Finishing'], color = 'red', alpha = 0.7)
grp1 = plt.scatter(df[df['Groups']==1]['GK reflexes'], df[df['Groups']==1]['Finishing'], color = 'blue', alpha = 0.7)
grp2 = plt.scatter(df[df['Groups']==2]['GK reflexes'], df[df['Groups']==2]['Finishing'], color = 'green', alpha = 0.7)
grp3 = plt.scatter(df[df['Groups']==3]['GK reflexes'], df[df['Groups']==3]['Finishing'], color = 'yellow', alpha = 0.7)  

plt.legend((grp0, grp1, grp2, grp3), ('Defenders', 'Midfielders', 'Goalkeepers', 'Forwards'), loc='right')
plt.xlabel('Gk reflexes')
plt.ylabel('Finishing')
plt.show()

#ploy 2

plt.clf()
plt.figure(figsize=(8,8))
grp0 = plt.scatter(df[df['Groups']==0]['Interceptions'], df[df['Groups']==0]['Shot power'], color = 'red', alpha = 0.7)
grp1 = plt.scatter(df[df['Groups']==1]['Interceptions'], df[df['Groups']==1]['Shot power'], color = 'blue', alpha = 0.7)
grp2 = plt.scatter(df[df['Groups']==2]['Interceptions'], df[df['Groups']==2]['Shot power'], color = 'green', alpha = 0.7)
grp3 = plt.scatter(df[df['Groups']==3]['Interceptions'], df[df['Groups']==3]['Shot power'], color = 'yellow', alpha = 0.7)  

plt.legend((grp0, grp1, grp2, grp3), ('Defenders', 'Midfielders', 'Goalkeepers', 'Forwards'), loc='lower right')
plt.xlabel('Interceptions')
plt.ylabel('Shot power')
plt.show()



#centroids
centroids = pd.DataFrame(kmeans.cluster_centers_)
centroids.columns=list(df1)


#Calculate the euclidean distance using the centroids calculated
# Crossing = 0, Sprint Speed = 11, Long Shots = 19, etc...
centroids_selected = centroids.loc[:,['Crossing','Sprint speed','Long shots','Aggression','Marking','Finishing','GK handling']]

new_sample = pd.DataFrame(columns=centroids_selected.columns)

new_sample.loc[0]=[45,40,35,45,60,40,15]


min_dist_ind=-1
min_dist=0
for i in range(len(centroids_selected)):
    dist = scipy.spatial.distance.cdist(centroids_selected.iloc[[i],:], new_sample, metric='euclidean')
    if min_dist==0 or dist[0,0]<= min_dist:
        min_dist=dist[0,0]
        min_dist_ind=i
        
    

    
