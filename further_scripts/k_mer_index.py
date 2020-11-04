import bisect

class Index(object): # define an index class
	def __init__(self, t, k):
		"Initialization method which preprocesses the string."
		self.k = k
		self.index = []

		for i in range(len(t) - k + 1): # take every kmer of length k in text 't'
			self.index.append((t[i:i+k], i)) # add that kmer to the index along with its offset in text 't' as a tuple
		self.index.sort()

	def query(self, p):
		"Query the index for pattern 'p'."
		kmer = p[:self.k]
		i = bisect.bisect_left(self.index, (kmer, -1)) # use binary search to find the first position in the index where this kmer occurs
		hits = []
		while i < len(self.index):
			if self.index[i][0] != kmer:
				break
			hits.append(self.index[i][1]) # append  the second value of that tuple to our list of hits
			i += 1
		return hits

	def queryIndex(self, p, t, index):
		"Match a full pattern 'p' against the the text 't'."
		k = index.k
		offsets = []
		for i in index.query(p): # use the query function to get a list of possible places where 'p' could start
			 if p[k:] == t[i+k:i+len(p)]:
			 	offsets.append(i)
		return offsets

t = 'AGCCTCAAGCCTCAAAGG'
p = 'TCAA'

index = Index(t,3) # create an index object
print(index.queryIndex(p, t, index))
