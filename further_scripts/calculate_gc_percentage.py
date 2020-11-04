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

### Method1
genome = read_genome(filename)
print("The length of the genome read from '%s' is %d nucleotides long." % (filename,  len(genome)))

def gc_percentage(genome) :

	no_c = genome.count('C')
	no_g = genome.count('G')
	length_genome = len(genome)
	per_gc = float((no_c+no_g)*100/length_genome)
	return per_gc

print("The gc_percentage of the genome read from '%s' by method1 is %d%%." % (filename, gc_percentage(genome)))

### Method2
nucleotidesDic = {'C':0, 'A':0, 'G':0, 'T':0, 'N':0}
for base in genome:
	nucleotidesDic[base] += 1

print("The gc_percentage of the genome read from '%s' by method2 is %d%%." % (filename, float((nucleotidesDic['G']+nucleotidesDic['C'])*100/len(genome))))
