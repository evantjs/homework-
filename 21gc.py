#!/usr/bin/env python3

# Write a program that computes the GC% of a DNA sequence
# Format the output for 2 decimal places
# Use all three formatting methods

dna = 'ACAGAGCCAGCAGATATACAGCAGATACTAT' # feel free to change

gc = 0

for i in range(len(dna)):
	if dna[i] == 'G' :gc += 1
	elif dna[i] == 'C': gc += 1
fgc = gc/len(dna) #can skip this line and plug gc/len(dna) into the next line 
print('%.2f' % fgc)#print style format
print( '{:.2f}'.format(fgc))#string format
print(f'{fgc:.2f}')#f-strings


"""

gccount = 0 
for i in range (len(dna)):
	base = dna[i]  #can resuse the varianble base for in the future
	if base == 'C' or base == 'G':
		gcount +=1

gcpercent = gcount / len(dna)

#another solution to the problem
gc = 0 
for i in range(len(dna)):
	nt = dna[i]
	if nt == 'C' or nt =='G": gc += 1
print(f'{fgc/len(dna):.2f}')
# within the curly brackets are executed with, thus able to format as well

"""	 
"""
python3 21gc.py
0.42
0.42
0.42
"""
