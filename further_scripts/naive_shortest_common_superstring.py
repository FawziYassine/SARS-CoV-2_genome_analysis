from itertools import permutations

def overlap(a, b, minLength = 3):
	"Returns the length of longest suffix of string 'a' that overlaps prefix of string 'b' of length at least 'minLength'."

	start = 0 # start all the way to the left

	while True:
		start = a.find(b[:minLength], start) # find b's prefix in a
		if start == -1:
			return 0
		# found occurence, look for full prefix/suffix match
		if b.startswith(a[start:]):
			return  len(a) - start
		start += 1

def shortest_common_superstring(ss):
	"Finds using Brute Force Algorithm the shortest common superstring between a given set of strings 'ss'."
	shortest_superstring = None
	for ssperms in permutations(ss): # for all permutations
		superstringPerm = ssperms[0]
		for i in range(len(ss) - 1):  # for each permutation
			# get the overlap length between the pair of consecutive strings
			olen = overlap(ssperms[i], ssperms[i+1], minLength = 1)
			superstringPerm += ssperms[i+1][olen:]
		# check if this permutation is the shortest seen so far
		if shortest_superstring == None or len(superstringPerm) < len(shortest_superstring):
			shortes_superstring = superstringPerm
	return shortes_superstring

# test
reads = ['ACCGGGTAGC', 'AGCTTTTGGGGGGGGGA', 'AGCTTGGGGGGGA', 'GGGGGGACCGGGTA']
print("The shortest common superstring using brute force algorithm between the strings in %s is:\n" % reads)
print(shortest_common_superstring(reads))

