def read_fastq(filename):
	"Reads the sequences and qualities from a .fastq 'filename'."
	f = open(filename)
	sequences = []
	qualities = []

	while True:
		f.readline() # skip the read header line (@ symbol)
		seq = f.readline().rstrip()		
		f.readline() # skip the seperator line (+ symbol)
		qual = f.readline().rstrip()
		if len(seq) == 0:
			break
		sequences.append(seq)
		qualities.append(qual)

	f.close()
	return sequences, qualities 

import sys
filename = sys.argv[1]
seqs, quals = read_fastq(filename)
print(seqs[:5])
print(quals[:5])
print(len(seqs))

def phred33toQ(q):
	"Converts a phred33 encoded character to a numerical quality."
	return ord(q) - 33 # ord(q) returns the ASCII encoding of 'q'

print(phred33toQ('#')) 
print(phred33toQ('J')); print(phred33toQ('/')) 
print(phred33toQ('E'))

def createHist(qualities):
	"`Create a Histogram of qualities."
	hist = [0] * 50 # initialize a list of integers of width 50 to 0s
	for readQualities in qualities: 
		for qual in readQualities: 
			hist[phred33toQ(qual)] += 1  # inrement by 1 the relative bin
	return hist

h = createHist(quals) # Create a Histogram of qualitiese 'quals' just read from the file
print(h)
import matplotlib.pyplot as plt
plt.bar(range(len(h)), h)
plt.show()  
	
import collections
count = collections.Counter()

for read in seqs:
	count.update(read)
print(count)
.
	def  findGCByPos(reads):
		"Find GC content of sequences in 'reads'."
		gc = [0] * 75 # initialize a list of integers of width 75 to 0s (75 is the read length)
		total = [0] * 75 # initialize a list of integers of width 75 to 0s (75 is the read length)

		for read in reads:
			for i in range(len(read)):
				if read[i] == 'G' or read[i] == 'C':
					gc[i] += 1 # inrement by 1 the relative bin if the base 'i' a chararcter 'G' or a chararcter 'C'
				total[i] += 1  # inrement by 1 the relative bin for any base 'i'
		for i in range(len(gc)):
			if not total[i] ==  0:
				gc[i] /= float(total[i])
		return gc

	gc =  findGCByPos(seqs) # Find GC content of sequences 'seqs' just read from the file
	plt.plot(range(len(gc)), gc)
	plt.show() 
	
