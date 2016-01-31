#!/usr/bin/env python
import csv
reader = csv.reader(open("Ndistance.txt","rb"), delimiter=',')
distance = list(reader)
for i in range(len(distance)):
	distance[i] = map(float, distance[i])
	print distance[i]

cluster = []

for i in range(len(distance))