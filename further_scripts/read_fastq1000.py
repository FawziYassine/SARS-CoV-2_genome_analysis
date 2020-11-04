
def read_fastq(filename):
	
	fr = open(filename, 'r')
	newContent = ''
	for i in range(4000):
		newContent += fr.readline()
	fr.close()
	return newContent 

import sys
filename = sys.argv[1]
fw = open(filename[0:-6] + '1000.fastq' , 'w')
fw.write(read_fastq(filename))
fw.close()
