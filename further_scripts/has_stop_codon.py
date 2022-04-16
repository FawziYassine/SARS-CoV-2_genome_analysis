def has_stop_codon(dna, frame = 0) :
	has_stop_codon = False
	stop_codon = ['tag','tga','taa']

	for i in range(int(frame), len(dna), 3) :
		codon = dna[i:i+3].lower()
		if codon in stop_codon :
			has_stop_codon = True
			break 
	return has_stop_codon


dna = 'AGCTTAGGCCC'
frame = 1

print("The DNA '%s'" % dna)
if (has_stop_codon(dna, frame)) :
	print("has stop codon.")
else  :
	print("has no stop codon.")
