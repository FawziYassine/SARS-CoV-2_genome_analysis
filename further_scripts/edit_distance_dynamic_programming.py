
def editDistDynamicProgramming(a, b):
	"Calculate the Edit Distance between strings 'a' and 'b' using Dynamic Programming."
	D = [] # A matrix of the edit distances for the substrings of 'a' and 'b'
	for i in range(len(a) + 1):
		D.append([0] * (len(b) + 1))

	for i in range(len(a) + 1):
		D[i][0] = i

	for i in range(len(b) + 1):
		D[0][i] = i

	for i in range(1, len(a) + 1):
		for j in range(1, len(b) + 1):
			distHor = D[i][j-1] + 1
			distVer = D[i-1][j] + 1

			if a[i-1] == b[j-1]:
				distDiag = D[i-1][j-1]
			else:
				distDiag = D[i-1][j-1] + 1
			D[i][j] = min(distHor, distVer, distDiag)

	return  D[-1][-1] # return the right-lower corner of the matrix

s1 = 'AGCTAAAGGGTTGGGGCCCCGGGGGGGA'
s2 = 'AGCTAGTTGGCCGGA'

import datetime as d
st = d.datetime.now()
print("The Edit Distance between strings '%s' and '%s' using Dynamic Programming is:\n" % (s1, s2))
print(editDistDynamicProgramming(s1, s2))
print((d.datetime.now() - st).total_seconds()) # calculate running time in seconds


