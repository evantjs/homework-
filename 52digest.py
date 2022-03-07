#!/usr/bin/env python3
# 52digest.py

import re
import sys

# Write a program that performs an EcoRI digest on the SARS-COV2 genome
# The program should have 2 arguments
#    1. The genome file
#    2. The restriction pattern
# The output should be the sizes of the restriction fragments

seqs = [] 	
names = []
seq = ""
with open(sys.argv[1]) as fp:
	for line in fp.readlines():
		line = line.rstrip()
		line = line.upper()
		if line.startswith("ORIGIN"):
			words = line.split()
			names.append(words[0][1:])
			if seq != "": seqs.append(seq) 
			seq = "" 
		else: seq += re.sub("\d*?","", line.strip())
	seqs.append(seq) 

restseq = sys.argv[2]

EcoRI = sys.argv[2].upper()
fragpos = []

for match in re.finditer(EcoRI, seq):
	fragpos.append( match.start())
for match in re.finditer(EcoRI[::-1], seq):
	fragpos.append( match.start())
	 
fragpos.sort()
print(fragpos)

	

frag = []
for i in range(len(fragpos)):
	if  fragpos[i-1] <= fragpos[i]:
		frag.append(fragpos[i] - fragpos[i-1] + 1)
	else: 
		frag.append(fragpos[i] +1 )
			
frag.append(len(seq)- fragpos[-1] -1)

print(frag)

#if match in re.finditer(EcoRI, seq) and re.finditer(EcoRI[::-1], seq): 
	#print(match.start())


"""
python3 52digest.py ../Data/sars-cov2.gb gaattc
1160
10573
5546
448
2550
2592
3569
2112
1069
"""
