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

print(overlap('ACCGGGTAGC', 'AGCTTTTGGGGGGGGAG'))
print(overlap('ACCGGGTAGC', 'GCTTTTGGGGGGGGAG'))
print(overlap('ACCGGGTAGCTT', 'AGCTTTTGGGGGGGGAG'))
