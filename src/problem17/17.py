#!/usr/bin/python
import sys
import math

# A utility function that returns true if x is perfect square
def isPerfectSquare(x):
    s = int(math.sqrt(x))
    return s*s == x
 
# Returns true if n is a Fibinacci Number, else false
def isFibonacci(n):
 
    # n is Fibinacci if one of 5*n*n + 4 or 5*n*n - 4 or both
    # is a perferct square
    return isPerfectSquare(5*n*n + 4) or isPerfectSquare(5*n*n - 4)

def printMissingFibonacciOrdered(inputs):
	result = []
	for number in range(min(inputs), max(inputs)):
		if isFibonacci(number) == True:
			if not number in inputs:
				print str(number) + " is Fibonacci"
				result.append(number)
			# else:
			# 	print str(number) + " is Fibonacci but is ignored"
	# else:
	# 	print str(number) + " is NO Fibonacci"
	return result
	

with open("17.out", 'w') as outFile:
	with open("17.in", 'r') as inFile:
		no_of_test_cases = int(next(inFile)) # read first line
		print no_of_test_cases

		for line in inFile: # read rest of lines
			values = ([int(x) for x in line.split()])
			# print values

			missingFibonacciOrdered = printMissingFibonacciOrdered(values)
			# print missingFibonacciOrdered

			for i in missingFibonacciOrdered:
				outFile.write(str(i) + ' ')
			outFile.write('\n')
		