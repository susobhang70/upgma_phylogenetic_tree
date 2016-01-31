#!/usr/bin/env python
import csv
str = []
temp = ''
with open('Nucleotide.txt') as Qinput:
    for line in Qinput:
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

matrix = [[0.0 for x in range(len(str))] for x in range(len(str))] 

for i in range(len(str) - 1):
	for j in range(i + 1, len(str)):
		count = 0
		for k in range(len(str[i])):
			if(str[i][k] != str[j][k]):
				count = count + 1
		matrix[i][j] = float(count)/len(str[i])
		matrix[j][i] = float(count)/len(str[i])

Qoutput = open("Ndistance.txt", "w")
writer = csv.writer(Qoutput)
for i in range(len(matrix)):
	writer.writerow(matrix[i])
Qoutput.close()