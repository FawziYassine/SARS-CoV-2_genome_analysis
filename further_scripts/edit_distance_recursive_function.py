
def editDistanceRecursive(a, b):
 	"Calculate the dit Distance between strings 'a' and 'b' using a recursive function."
	if len(a) == 0:
		return len(b)
	if len(b) == 0:
		return len(a)

	delt = 1 if a[-1] != b[-1] else 0 # delt = 1 if the last characters of 'a' and 'b' are equal otherwise delt = 0 
	return min(editDistanceRecursive(a[:-1], b[:-1]) + delt,
		   editDistanceRecursive(a[:-1], b) + 1,
		   editDistanceRecursive(a, b[:-1]) + 1)

s1 = 'AGCTAAAGGGTTGGGGCCCCGGGGGGGA'
s2 = 'AGCTAAAGGGTTGA'

import datetime as d
st = d.datetime.now()
print("The Edit Distance between strings '%s' and '%s' using a recursive function is:\n" % (s1, s2))
print(editDistanceRecursive(s1, s2))
print((d.datetime.now() - st).total_seconds())


