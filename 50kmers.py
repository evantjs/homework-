#!/usr/bin/env python3
# 50kmers.py

import sys

# Make a program that reports the kmer counts for a fasta file
# Your program should take 2 arguments:
#    1. The file name
#    2. The size of k

#seq = "ATGCTGGGGTCCAGTAACTACGGCGCATAATTT"

#make all combinations based on k size and put it in a dictionary
#read fasta and count the number of each kmer from dictionary

seqs = [] 	
names = []
seq = ""
with open(sys.argv[1]) as fp:
	for line in fp.readlines():
		line = line.rstrip() 
		if line.startswith( ">"): 
			words = line.split()#glues lines together
			names.append(words[0][1:])#skips the >
			if seq != "": seqs.append(seq) #stops the seq
			seq = "" #creates another sequence 
		else: seq += line
	seqs.append(seq) #last line gets added in		
		

k = 2
tot = 0
count = {}
for i in range(len(seq)-k+1):
	kmer = seq[i:i+k]
	if kmer not in count: 
		count[kmer] = 0
	count[kmer] += 1
	tot += 1
for kmer in count:
	print(kmer, count[kmer], f'{(count[kmer]/tot):.4f}')	
	


	
# sort with |sort
"""
python3 50kmers.py ../Data/chr1.fa 2
AA	33657	0.1106
AC	15836	0.0520
AG	18244	0.0600
AT	27223	0.0895
CA	18965	0.0623
CC	10517	0.0346
CG	8147	0.0268
CT	18142	0.0596
GA	19994	0.0657
GC	9673	0.0318
GG	10948	0.0360
GT	16348	0.0537
TA	22344	0.0734
TC	19744	0.0649
TG	19624	0.0645
TT	34869	0.1146
"""
