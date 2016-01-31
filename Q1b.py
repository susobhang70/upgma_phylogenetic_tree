import sys

def main():
	f = open('Ndistance.txt','rU')
	Matrix = [[0 for x in range(6)] for x in range(6)] 
	i = j = 0
	for line in f:
		lst = line.split(',')
		j = 0
		for nucleotide in lst:
			Matrix[i][j] = float(nucleotide)
			j += 1
		i += 1

	speciesMapping = []
	speciesMapping.append('Cow')
	speciesMapping.append('Sheep')
	speciesMapping.append('Marine Worm')
	speciesMapping.append('Rat')
	speciesMapping.append('Frog')
	speciesMapping.append('Wild Pig')


	cluster = []
	sizeCluster = []
	for i in range(6):
		cluster.append(i)
		sizeCluster.append(1)

	prevMatrix = None
	prevCluster = None
	prevSizeCluster = None

	numCluster = len(cluster)

	while numCluster > 2:
		minValue = Matrix[0][1]
		minClusterA = 0
		minClusterB = 1
		for i in range(len(cluster)):
			for j in range(len(cluster)):
				if minValue > Matrix[i][j] and Matrix[i][j] != 0.0:
					minClusterA = i
					minClusterB = j
					minValue = Matrix[i][j]
		valueClusterA = cluster[minClusterA]
		valueClusterB = cluster[minClusterB]
		print 'Minvalue ->' + str(minValue)
		print 'A-> ' + str(valueClusterA)
		print 'B-> ' + str(valueClusterB)
		print 'minClusterA-> ' + str(minClusterA)
		print 'minClusterB-> ' + str(minClusterB)


		prevMatrix = [[0 for x in range(len(cluster))] for x in range(len(cluster))]
		for i in range(len(cluster)):
			for j in range(len(cluster)):
				prevMatrix[i][j] = Matrix[i][j]

		prevCluster = list(cluster) 
		if valueClusterA in cluster:
			cluster.remove(valueClusterA)
		else:
			print 'Not in cluster :Error A'
		if valueClusterB in cluster:
			cluster.remove(valueClusterB)
		else:
			print 'Not in cluster :Error B'
		tempTuple = (valueClusterA, valueClusterB)
		cluster.insert(0, tempTuple)
		numCluster = len(cluster)

		prevSizeCluster = list(sizeCluster)
		if minClusterB > minClusterA:
			s2 = sizeCluster.pop(minClusterB)
			s1 = sizeCluster.pop(minClusterA)
		else:
			s1 = sizeCluster.pop(minClusterA)
			s2 = sizeCluster.pop(minClusterB)
		sum12 = s1 + s2
		sizeCluster.insert(0, sum12)

		Matrix = [[0 for x in range(len(cluster))] for x in range(len(cluster))]

		for i in range(len(cluster)):
			for j in range(len(cluster)):
				if i == j:
					Matrix[i][j] = 0
				elif i == 0 or j == 0:
					idx1 = prevCluster.index(valueClusterA)
					idx2 = prevCluster.index(valueClusterB)
					if i == 0:
						idx3 = prevCluster.index(cluster[j])
					else:
						idx3 = prevCluster.index(cluster[i])
					Matrix[i][j] = (prevMatrix[idx1][idx3]*prevSizeCluster[idx1] + prevMatrix[idx2][idx3]*prevSizeCluster[idx2])/(prevSizeCluster[idx1] + prevSizeCluster[idx2])
				else:
					idx1 = prevCluster.index(cluster[i])
					idx2 = prevCluster.index(cluster[j])
					Matrix[i][j] = prevMatrix[idx1][idx2]
		#print
		print 'Matrix'
		for i in range(len(cluster)):
			for j in range(len(cluster)):
				print str(Matrix[i][j]) + ' , ',
			print
		print 'Clusters'
		for temp in cluster:
			print temp

		print '*******************'
					

	'''
	for i in range(6):
		for j in range(6):
			print Matrix[i][j],
		print 
	'''


if __name__ == '__main__':
	main()