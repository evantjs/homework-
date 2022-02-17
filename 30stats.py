#!/usr/bin/env python3

# Write a program that computes typical stats
# Count, Min, Max, Mean, Std. Dev, Median
# No, you cannot import the stats library!

import sys
import math

arr = []
for r in sys.argv[1:]:
	arr.append(float(r))
count = len(arr)
mean = sum(arr)/len(arr)

print(f'Count: {count}')
print(f'Mean: {mean:.3f}')

arr.sort()
last = (len(arr)-1)
min = arr[0]
max = arr[last]

print(f'Minimum: {min:.1f}')
print(f'Maximum: {max:.1f}')
Variance = []
for i in range(count):
	Variance.append(mean**2- arr[i]**2)
sd = math.sqrt(abs(sum(Variance))/count)		
print(f'Std. dev: {sd:.3f}')

median = 0

if len(arr) % 2 == 0: 
	m1 = arr[len(arr)//2]
	m2 = arr[len(arr)//2-1]
	median = (m1 + m2)/2
else: median = arr[len(arr)//2]
	
print(f'Median:{median:.3f}')

"""
python3 30stats.py 3 1 4 1 5
Count: 5
Minimum: 1.0
Maximum: 5.0
Mean: 2.800
Std. dev: 1.600
Median 3.000
"""
