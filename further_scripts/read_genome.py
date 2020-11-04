def read_genome(filename):
	"Reads genome from a .fa 'filename'."
	f = open(filename)
	genome = ''
	for line in f:
		if not line.startswith('>') : # skip the header line (> symbol)
			genome += line.rstrip()
	f.close()
	return genome

import sys


filename = sys.argv[1]

genome = read_genome(filename)
print(genome[:100])
print(len(genome))
