#!/usr/bin/env python3

# Write a program that prints the reverse-complement of a DNA sequence
# You must use a loop and conditional

dna = 'ACTGAAAAAAAAAAA'

anti = ""
for i in range(len(dna)):
	nt = dna[::-1][i]#[::-1] inverse func
	if   nt == 'A': anti += 'T'
	elif nt == 'C': anti += 'G'
	elif nt == 'G': anti += 'C'
	else		  : anti += 'A'
print(anti)
	
#for i in range(len(dna):
#j = len(dna) -i -1
#print(i, j) also goes backwards
#print (len(dna), i)
"""
python3 23anti.py
TTTTTTTTTTTCAGT
"""
