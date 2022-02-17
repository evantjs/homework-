#!/usr/bin/env python3

# Write a program that simulates random read coverage over a chromosome
# Report min, max, and average coverage
# Make variables for genome size, read number, read length
# Input values from the command line
# Note that you will not sample the ends of a chromosome very well
# So don't count the first and last parts of a chromsome

import sys
import random

trials = 100



Coverage = []
seq = int(sys.argv[1])
read = int(sys.argv[2])
l = int(sys.argv[3])
for i in range(seq):
	Coverage.append(0)

for i in range(read):
	start = random.randint(0, seq - l)
	for j in range(start, start + l):
		Coverage[j] += 1


min = Coverage[l]
max = Coverage[l]
for val in Coverage[l:-l]:
	if val < min: min = val
	if val > max: max = val

avg = sum(Coverage[l:-l])/len(Coverage[l:-l])

print(min, max, f'{avg:.4f}')
	
"""


python3 32xcoverage.py 1000 100 100
5 20 10.82375
"""
