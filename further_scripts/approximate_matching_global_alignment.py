alphabet = ['A', 'C', 'G', 'T']
"""
Penalty matrix: bases A (adenine) and G (guanine) are purines (double ring chemical compounds)
while bases C (cytosine) and T (thymine) are pyrimidines (single ring chemical compounds).
In humans, transitions (purines to purines) are more frequent than transveresions (pyrimidines to pyrimidines)
whereas the indels (insertions and deletions) are less frequent than substitutions.
"""
penalty = [[0, 4, 2, 4, 8], \
           [4, 0, 4, 2, 8], \
           [2, 4, 0, 4, 8], \
           [4, 2, 4, 0, 8], \
           [8, 8, 8, 8, 8]]

def globalAlignment(a, b):
	"Calculate the Approximate Matching Edit Distance between strings 'a' and 'b' using Global Alignment (Dynamic Programming)."

	D = [] # A matrix of the edit distances for the substrings of 'a' and 'b'
	for i in range(len(a) + 1):
		D.append([0] * (len(b) + 1))

	for i in range(1, len(a) + 1):
		D[i][0] = D[i-1][0] + penalty[alphabet.index(a[i-1])][-1]

	for i in range(1, len(b) + 1):
		D[0][i] = D[0][i-1] + penalty[-1][alphabet.index(b[i-1])]
	for i in range(1, len(a) + 1):
		for j in range(1, len(b) + 1):
			distHor = D[i][j-1] +  penalty[-1][alphabet.index(b[j-1])] 
			distVer = D[i-1][j] + penalty[alphabet.index(a[i-1])][-1]

			if a[i-1] == b[j-1]:
				distDiag = D[i-1][j-1]
			else:
				distDiag = D[i-1][j-1] +  penalty[alphabet.index(a[i-1])][alphabet.index(b[j-1])]
			D[i][j] = min(distHor, distVer, distDiag)
	return  D[-1][-1] # return the right-lower corner of the matrix

s1 = 'AAAAAAAACCCCCGGATC'
s2 = 'AAAAAAACCCCGGATG'

print("The Approximate Matching Edit Distance between strings '%s' and '%s' using Global Alignment (Dynamic Programming) is:\n" % (s1, s2))
print(globalAlignment(s1, s2))


