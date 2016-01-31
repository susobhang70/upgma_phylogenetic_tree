#!/usr/bin/env python
import csv
import sys
reader = csv.reader(open("Pdistance.txt","rb"), delimiter=',')
distance = list(reader)
for i in range(len(distance)):
	distance[i] = map(float, distance[i])

cluster = []
clustersize = []

for i in range(len(distance)):
	cluster.append(i)
	clustersize.append(1)

clustermapping = ['Cow', 'Sheep', 'Marine Worm', 'Rat', 'Frog', 'Wild Pig']

size = len(cluster)

olddistance = None
oldcluster = None
oldclustersize = None

count = 1

while size > 2:
	olddistance = [[0 for x in range(len(cluster))] for x in range(len(cluster))]
	maxValue = sys.float_info.min
	x = None
	y = None
	for i in range(size):
		for j in range(size):
			olddistance[i][j] = distance[i][j]
			if distance[i][j] != 0 and distance[i][j] > maxValue:
				x = i
				y = j
				maxValue = distance[i][j]

	firstspecies = cluster[x]
	secondspecies = cluster[y]

	firstspeciesmapping = clustermapping[x]
	secondspeciesmapping = clustermapping[y]

	print '*******************'
	print 'Step -', count
	print '*******************'
	print 'maxCluster 1 =', firstspeciesmapping
	print 'maxCluster 2 =', secondspeciesmapping
	print 'MaxValue = ', maxValue

	oldcluster = list(cluster)

	cluster.remove(firstspecies)
	cluster.remove(secondspecies)

	clustermapping.remove(firstspeciesmapping)
	clustermapping.remove(secondspeciesmapping)

	temp = (firstspecies, secondspecies)
	tempmapping = (firstspeciesmapping, secondspeciesmapping)

	cluster.insert(0, temp)
	clustermapping.insert(0, tempmapping)

	size = len(cluster)
	oldclustersize = list(clustersize)

	temp1 = None
	temp2 = None

	if y > x:
		temp2 = clustersize.pop(y)
		temp1 = clustersize.pop(x)

	else:
		temp1 = clustersize.pop(x)
		temp2 = clustersize.pop(y)

	temp12 = temp1 + temp2
	clustersize.insert(0, temp12)

	distance = [[0.0 for x in range(len(cluster))] for x in range(len(cluster))]

	for i in range(size):
		for j in range(size):
			if i == j:
				distance[i][j] = 0.0

			elif i == 0 or j == 0:
				it1 = oldcluster.index(firstspecies)
				it2 = oldcluster.index(secondspecies)
				it3 = None
				if i == 0:
					it3 = oldcluster.index(cluster[j])
				else:
					it3 = oldcluster.index(cluster[i])
				distance[i][j] = (olddistance[it1][it3]*oldclustersize[it1] + olddistance[it2][it3]*oldclustersize[it2])/(oldclustersize[it1] + oldclustersize[it2])

			else:
				distance[i][j] = olddistance[oldcluster.index(cluster[i])][oldcluster.index(cluster[j])]

	print '*******************'
	print 'New Matrix'
	print '*******************'
	for i in range(len(cluster)):
		print distance[i]
	print '*******************'
	print 'Clusters'
	print '*******************'
	for i in clustermapping:
		print i
	count = count + 1