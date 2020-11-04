"""
This code divides a multi-genome file into seperate files each containing a seperate genome.
The files will be written to a directory named 'genomes'.
"""

import sys
filename = sys.argv[1]

f = open(filename)
# create a dictionay of id:fileContents pairs
fileContents  = {} # it was not necessary to create a dictionay; I could have written the fileContents directly to the file
line = f.readline()
while True :
	if line.startswith('>') :
		words = line.split()
		id = words[0][1:] # the id of the file or the genome is the first word of the header line except the first charachter
		fileContents[id] = ''
		fileContents[id] = fileContents[id] + line # append the header line to fileContent
	else :
		fileContents[id] = fileContents[id] + line # append this line to fileContent
	line = f.readline()
	if len(line) == 0:
		break;
f.close()

import os
os.system("mkdir SARS-CoV-2_virus_genomes")

for id,fileContent in fileContents.items():
	fhandle = open('SARS-CoV-2_virus_genomes/' + id + '.fa', 'w')
	fhandle.write(fileContent)
	fhandle.close()
