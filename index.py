import numpy as np
from sympy import true
from cluster import calc_cluster

################################
#         Variable init        #
################################
debug = False

centroid = {'x':[2.0, -2.0], 'y':[2.0, -2.0]}
datapoint = {'x':[-1.88, -0.71, 2.41, 1.85, -3.69], 'y':[2.05, 0.42, -0.67, -3.80, -1.33]}

##########################################
#     Create clusters with centroids     #
##########################################
cluster = []
for i in range(len(centroid['x'])):
    t = [(centroid['x'][i], centroid['y'][i])]
    cluster.append(t)

# print cluster
if(debug):
    print("Cluster:", cluster)

################################
#          Main Loop           #
################################
# start finding the next cluster
# loop until new cluster centroids is same as last
while(True):
    print("calculating next cluster for centroids: ", cluster)
    prev_cluster = [ x[:] for x in cluster ] # save previous cluster to compare
    cluster = calc_cluster(cluster, datapoint) # calculate new cluster points
    if(prev_cluster == cluster):
        print("Same cluster values reached: ", prev_cluster, " : ", cluster)
        break

