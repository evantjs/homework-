#!/usr/bin/env python3

# You are probably well aware of the 'birthday paradox'
# https://en.wikipedia.org/wiki/Birthday_problem
# Let's try simulating it

# You will need a list for the 365 day calendar
# You will need a set number of people (e.g. 25)
# During each 'trial' you do the following
#	Choose a person
#	Git them a random birthday
#	Store it in the calendar
# Once you have stored all birthdays, check to see if any have the same day
# Do this for many trials to see what the probability of sharing a birthday is

import random

trials = 100000
n= 23
days= 365
share = 0
for i in range(trials):
	#make an empty calendar
	calendar = [0]*days
	#fill it with random birthdays
	for j in range(n):
		 bd = random.randint(0, days-1)
		 calendar[bd] += 1
	#check for shared birthdays	
	for val in calendar:
		 if val > 1: 
		 	share += 1
		 	break
		
		 
print(share/trials)		
		
"""
python3 33birthday.py
0.571
"""

