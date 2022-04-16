from itertools import permutations

def overlap(a, b, minLength = 3):
	"Returns length of longest suffix of string 'a' that overlaps prefix of string 'b' of at least length 'minLength'"

	start = 0 # start all the way to the left

	while True:
		start = a.find(b[:minLength], start) # find b's prefix in a
		if start == -1:
			return 0
		# found occurence, look for full prefix/suffix match
		if b.startswith(a[start:]):
			return  len(a) - start
		start += 1

def pick_maximal_overlap(reads, k):
	"Finds the longest overlap between a given set of strings 'reads' of at least length 'k'."
	reada, readb = None,  None
	best_olen = 0
	for a, b in permutations(reads, 2): # for all pairs
		olen = overlap(a, b, minLength = k)
		# check if this overlap is the longest seen so far
		if olen > best_olen:
			reada, readb = a, b
			best_olen = olen
	return reada, readb, best_olen

def greedy_shortest_common_superstring(reads, k):
	"Finds the shortest common superstring between a given set of strings 'reads' of at least length 'k'."
	readA, readB, olen = pick_maximal_overlap(reads, k) # first maximal overlap
	while olen > 0: # keep looping as long as there are overlaps
		reads.remove(readA)
		reads.remove(readB)
		reads.append(readA + readB[olen:]) # merge prefix/suffix match and append it to reads
		readA, readB, olen = pick_maximal_overlap(reads, k) # next maximal overlap
	return ''.join(reads)

# test
reads = ['ACCGGGTAGC', 'AGCTTTTGGGGGGGGGA', 'AGCTTGGGGGGGA', 'GGGGGGACCGGGTA']
print("The shortest common superstring using greedy algorithm between the strings in %s is:\n" % reads)
print(greedy_shortest_common_superstring(reads, 2))

