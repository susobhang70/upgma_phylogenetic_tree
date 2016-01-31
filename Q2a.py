#!/usr/bin/env python
import csv

i = 0
proteindict = {}
values = [[0.0 for x in range(100)] for x in range(100)]

with open('BLOSUM62.txt') as Pinput:
	for line in Pinput:
		line = line[2:]
		temp = line.split()
		if i == 0:
			for j in range(len(temp)):
				proteindict[temp[j]] = j
		else:
			values[i - 1] = map(int, temp)
		i = i+1

str = []
temp = ''
with open('Protein.txt') as Pinput:
	for line in Pinput:
		if(line[1] == '\n'):
			str.append(temp)
			temp = ''
			continue
		line = line.rstrip('\r\n')
		if(line[0] != '>'):
			temp = temp + line

if temp != '':
	str.append(temp)
	temp = ''

matrix = [[0 for x in range(len(str))] for x in range(len(str))] 

for i in range(len(str) - 1):
	for j in range(i + 1, len(str)):
		count = 0
		for k in range(min(len(str[i]), len(str[j]))):
			count = count + values[proteindict[str[i][k]]][proteindict[str[j][k]]]
			
		count = count + (max(len(str[i]), len(str[j])) - min(len(str[i]), len(str[j]))) * values[proteindict['*']][proteindict['*']]


		matrix[i][j] = count
		matrix[j][i] = count

Poutput = open("Pdistance.txt", "w")
writer = csv.writer(Poutput)
for i in range(len(matrix)):
	writer.writerow(matrix[i])
Poutput.close()