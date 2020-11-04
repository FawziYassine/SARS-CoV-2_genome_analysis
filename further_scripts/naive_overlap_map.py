from itertools import permutations

def overlap(a, b, minLength = 3):
	"Returns the length of longest suffix of string 'a' that overlaps prefix of string 'b' of at least 'minLength'."

	start = 0 # start all the way to the left

	while True:
		start = a.find(b[:minLength], start) # find b's prefix in a
		if start == -1:
			return 0
		# found occurence, look for full prefix/suffix match
		if b.startswith(a[start:]):
			return  len(a) - start
		start += 1

def naive_overlap_map(reads, k):
	"Create a naive overlap map for a set of reads."
	olaps = {}
	for a,b in permutations(reads, 2): # for each pair of reads a, b, in permutations of reads, 2 
		olen =  overlap(a, b, k)
		if olen > 0:
			olaps[(a, b)] = olen
	return olaps

reads = ['ACCGGGTAGC', 'AGCTTTTGGGGGGGAG', 'GTAGCTTGGGGGGGA', 'TTGGGGGGGACC']
print(naive_overlap_map(reads, 4))

