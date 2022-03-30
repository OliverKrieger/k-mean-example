import numpy as np
import matplotlib.pyplot as plt
debug = False

################################
#       Calculate Cluster      #
################################

def calc_cluster(cluster, datapoint):
    centroid_number = len(cluster) # cluster will only have centroids currently, so length matches
    for i in range(len(datapoint['x'])):
        min_centroid_index = 0 # variable to store the minimal point to centroid distance in
        dists = [] # distances calculated for centroid
        for j in range(centroid_number):
            d1 = (cluster[j][0][0] - datapoint['x'][i])**2 # x1 - x2
            d2 = (cluster[j][0][0] - datapoint['y'][i])**2 # y1 - y2
            d = np.sqrt(np.abs(d1)+np.abs(d2)) # distance algorithm for the point to centroid
            t = (d, j) # distance and index
            dists.append(t) # add to the list of distances
        
        min_centroid_index = min(dists)[1] # find the centroid that has the smallest distance

        if(debug):
            print("min centroid: ", min_centroid_index)

        # add point to the closest centroid index in the cluster
        t = (datapoint['x'][i]), (datapoint['y'][i]) # create the tuple for the point
        cluster[min_centroid_index].append(t) # add it to the array element for the centroid it was closest to
    
    return plot_points(cluster) # now plot

################################
#         Draw Cluster         #
################################
def plot_points(cluster):
    for i in cluster:
        counter = 0 # counter so we would know which point we are plotting (want it so we can make the centroid look different on graph)
        if(debug):
            print(i)
        c_val = np.random.rand(3,) # select cluster colour
        for j in i:
            if(counter == 0):
                plt.scatter(j[0], j[1], color=c_val, marker="x", s=100) # if first element in cluster, is a centriod
            else:
                plt.scatter(j[0], j[1], color=c_val) # for any other element, is a point
            plt.text(j[0], j[1]+0.5, '({}, {})'.format(j[0], j[1]), c="red") # draw point coordinates next to them on graph
            if(debug):
                print(j)
            counter += 1 # increase counter for the point in the cluster
    
    plt.show() # draw graph
    return calc_new_centroids(cluster)

######################################
# Calculate New Centroid for Cluster #
######################################
def calc_new_centroids(cluster):
    counter = 0
    for i in cluster:
        avg = np.average(i[1:], axis=0) # calculate average between the points for a new centroid (excludes the centroid itself)
        if(debug):
            print(np.average(i, axis=0))
        t = [(avg[0], avg[1])] # make a tuple of the new centroid
        if(debug):
            print(t)
        cluster[counter] = t # override the cluster with centroid
        counter += 1 # calculate next cluster

    if(debug):
        print(cluster)
    return cluster