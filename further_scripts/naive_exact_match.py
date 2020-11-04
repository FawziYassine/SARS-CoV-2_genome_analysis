def naive(p, t):
	"""
	Naive Exact Matcth of pattern 'p' against text 't'.
	Returns a list that will keep track of all the indices where 'p' matches against 't'
	"""
	occurences = [] # a list that will keep track of all the indices where 'p' matches against 't'
	for i in range(len(t) - len(p) + 1): # loop through every position (token) where 'p' could start
		match = True
		for j in range(len(p)):
			if not t[i+j] == p[j]:
				match = False
				break
		if match == True:
			occurences.append(i)
	return occurences

#try 1
print(naive('TAG', 'GCTAGGTAG'))

def read_genome(filename):
	"Reads genome from a .fa 'filename'."
	f = open(filename)
	genome = ''
	for line in f:
		if not line.startswith('>') : # skip the header line (> symbol)
			genome += line.rstrip()
	f.close()
	return genome

import random
def generateReads(genome, numReads, readLen):
	reads = []

	for _ in range(numReads):
		start = random.randint(0, len(genome) - readLen - 1)	
		reads.append(genome[start:start+readLen])
	return reads	


def read_fastq(filename):
	
	f = open(filename)
	sequences = []
	qualities = []
	while True:
		f.readline()
		seq = f.readline().rstrip()
		
		f.readline()
		qual = f.readline().rstrip()
		if len(seq) == 0:
			break
		sequences.append(seq)
		qualities.append(qual)
	f.close()
	return sequences, qualities 


#try 2
import sys

genomeFilename = sys.argv[2]

genome = read_genome(genomeFilename)
print(genome[:100])
print(len(genome))

artificialReads = generateReads(genome, 100, 75)

numMatched = 0

for r in artificialReads:
	occurences = naive(r, genome)
	if len(occurences) > 0:
		numMatched += 1
print('found %d out of %d artificially generated reads' %(numMatched, len(artificialReads)))

#try 3
readsFilename = sys.argv[1]
realReads, quals = read_fastq(readsFilename)
print(realReads[:5])
print(quals[:5])
print(len(realReads))


numMatched = 0
n = 0

for r in realReads:
	n += 1
	occurences = naive(reversecomplement(r), genome)
	if len(occurences) > 0:
		numMatched += 1
print('found %d out of %d real reads' %(numMatched, n))


