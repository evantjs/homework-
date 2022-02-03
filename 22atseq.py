#!/usr/bin/env python3

import random
random.seed(1) # comment-out this line to change sequence each time

# Write a program that stores random DNA sequence in a string
# The sequence should be 30 nt long
# On average, the sequence should be 60% AT
# Calculate the actual AT fraction while generating the sequence
# Report the length, AT fraction, and sequence

#create a variable for DNA
# everytime the loop occus,I need to add an AT or GC
"""
for i in range(30):
	r = random.random()
	if r >0.6:
		print(i,'G')
	elif r<0.6:
		print(i,'A')
	else:
		print(i,'?')
#Not good because that if r=0.6 code will not work but because right now r has no 0.6 so it works. 

Another workable code for this problem

import random 
random.seed(1)

dna=""
for i in range(30):
	r = random.random()
	if 	 r < 0.3: dna += 'A' #A is 30% while T is 30% so AT is 60%
	elif r < 0.6: dna += 'T'
	elif r < 0.8: dna += 'C'
	else        : dna += 'G'
	print(dna)
"""
dna =""
for i in range(30):
	if random.random()>0.6: #this is to satisfy line 8 
		if random.random()>0.5:#this is to see if its going to be  G or C
			dna += 'G'
		else: 
			dna += 'C'
		
	else:
		if random.random()>0.5: #this is to see if its going to be A or T
			dna += 'A' #this is more clear than the above code lines 15 - 22
		else:
			dna += 'T'
		
at = 0
for i in range(len(dna)):
	if   dna[i] == 'A': at += 1
	elif dna[i] == 'T': at += 1

print(len(dna),at/len(dna))
print(dna)

"""
python3 22atseq.py
30 0.6666666666666666 ATTACCGTAATCTACTATTAAGTCACAACC
"""
