# Functions

# def square(x):
# 	r = x * x
# 	return r

# print(square(6))

# def code_message(text_string, coding_dictionary):
# 	coded_message = ''
# 	for char in text_string:
# 		if char in coding_dictionary:
# 			newchar = coding_dictionary[char]
# 		else:
# 			newchar = char
# 		coded_message += newchar
# 	return coded_message

def mean(some_list):
	sum = 0
	for item in some_list:
		sum += item
	return len(some_list) and sum/len(some_list)	# evaluates to 0 if list is empty, otherwise returns the mean

print(mean([1,6,3,4,9]))

# A function ALWAYS returns something in Python >> if return is not explicit, the function returns the value 'none'

def mean(*data):
	sum = 0
	for item in data:
		sum += item
	return (sum/len(data))

def stdev(mean, *data):
	avg = mean(*data)
	sumsq = 0
	for item in data:
		sumsq += (item - avg) * (item - avg)
	return sumsq/len(data)

print(stdev(mean, 4,9,2,3))

import statistics as st
x = (4,5,6,2,3)
print(st.stdev(x))

import math
print(math.sqrt(24))

from statistics import variance
#disambiguous function
print(variance(x))
