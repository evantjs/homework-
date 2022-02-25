#!/usr/bin/env python3

import sys
import random
# Write a program that predicts if a protein is trans-membrane
# Trans-membrane proteins have the following properties
#	Signal peptide: https://en.wikipedia.org/wiki/Signal_peptide
#	Hydrophobic regions(s): https://en.wikipedia.org/wiki/Transmembrane_protein
#	No prolines in hydrophobic regions (alpha helix)
# Hydrophobicity is measued via Kyte-Dolittle
#	https://en.wikipedia.org/wiki/Hydrophilicity_plot
# For our purposes:
#	Signal peptide is 8 aa long, KD > 2.5, first 30 aa
#	Hydrophobic region is 11 aa long, KD > 2.0, after 30 aa
# Hints:
#   Create a function for KD calculation
#   Create a function for amphipathic alpha-helix




def kdhydrophob(prot):
	kd=0
	for aa in prot:
		if   aa == "I": kd += 4.5
		elif aa == "V": kd += 4.2
		elif aa == "L": kd += 3.8
		elif aa == "F": kd += 2.8
		elif aa == "C": kd += 2.5
		elif aa == "M": kd += 1.9
		elif aa == "A": kd += 1.8
		elif aa == "G": kd += -0.4
		elif aa == "T": kd += -0.7
		elif aa == "S": kd += -0.8
		elif aa == "W": kd += -0.9
		elif aa == "Y": kd += -1.3
		elif aa == "P": kd += -1.6
		elif aa == "H": kd += -3.2
		elif aa == "E": kd += -3.5
		elif aa == "Q": kd += -3.5
		elif aa == "D": kd += -3.5
		elif aa == "N": kd += -3.5
		elif aa == "K": kd += -3.9
		elif aa == "R": kd += -4.5
	return kd/len(prot)

def amphelix(seq, size, t):
	for i in range(len(seq)- size+1):
		pep = seq[i:i+size]
		if "P" in pep : continue# goes to the next i in the loop 
		if kdhydrophob(pep) >= t:
			return True
	return False

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
		
for name, seq in zip(names, seqs):
	if amphelix(seq[0:30], 8, 2.5) and amphelix(seq[30:], 11, 2.0): print(name)
		

"""
python3 40transmembrane.py ../Data/at_prots.fa
AT1G75120.1
AT1G10950.1
AT1G75110.1
AT1G74790.1
AT1G12660.1
AT1G75130.1
"""
