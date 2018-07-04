#Done by Makena p15/34267/2015

from scipy.spatial import distance
import numpy as np 
import random
from itertools import izip

def objectToCentroidDistance(centroids, clusters):
    return sum(distance.cdist([centroid], cluster, 'sqeuclidean').sum()
        for centroid, cluster in izip(centroids, clusters))

def computingNewCentroids(clusters):
    return [np.mean(cluster, axis =0) for cluster in clusters]

def kmeans(k, centroids, points, method):
    clusters = [[] for _ in range(k)]

    for point in points:
        clusters[closest_centroid(point, centroids)].append(point)


    new_centroids = computingNewCentroids(clusters)

    print("\nThe new centroids are: ")
    print(new_centroids)

    print("The new grouping is as below: ")
    print(clusters)
    if not equals(centroids, new_centroids):

        clusters = kmeans(k, new_centroids, points, method)

    return clusters

def closest_centroid(point, centroids):
    min_distance = float('inf')
    belongs_to_cluster = None
    for j, centroid in enumerate(centroids):
        dist = distance.sqeuclidean(point, centroid)
        if dist < min_distance:
            min_distance = dist
            belongs_to_cluster = j

    return belongs_to_cluster


def contains(point1, points):
    for point2 in points:
        if point1[0] == point2[0] and point1[1] == point2[1]:
        # if all(x == y for x, y in izip(points1, points2)):
            return True

    return False


def equals(points1, points2):
    if len(points1) != len(points2):
        return False

    for point1, point2 in izip(points1, points2):
        if point1[0] != point2[0] or point1[1] != point2[1]:
        # if any(x != y for x, y in izip(points1, points2)):
            return False
            
    return True

if __name__ == "__main__":
    medicine = np.array([[1, 1],[2, 1], [4, 3], [5, 4]])

    print("This is the array we are dealing with \n") 
    print(medicine)

    k = 2

    centroids = medicine[:k]
    print('\n The first centroids are:')
    print(centroids)
    clusters = kmeans(k, centroids, medicine, "first")