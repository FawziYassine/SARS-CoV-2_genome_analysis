
def reverse_complement(seq) :
	"Reverse complement of a sequence 'seq'."
	complementsDic = {'G':'C', 'C':'G', 'T':'A','A':'T', 'N':'N'}
	rc = ''
	for base in seq: # loop over every letter
		rc = complementsDic[base] + rc # write the complement of the letter first in order to achieve reversion
	return rc

seq = "AGCTAGCTAAGGGGA"

print("The reverse complement of the sequence %s \nis: %s" % (seq, reverse_complement(seq)))




