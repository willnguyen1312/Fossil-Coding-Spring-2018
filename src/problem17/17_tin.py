#!/usr/bin/python
import sys
import math

cached_fibonaci = []

a, b = 1, 1
while True:
    a, b = b, a+b
    cached_fibonaci.append(a)
    if a > 99999999:
        break

# A utility function that returns true if x is perfect square
def isPerfectSquare(x):
    s = int(math.sqrt(x))
    return s*s == x
 
# Returns true if n is a Fibinacci Number, else false
def isFibonacci(n):
    return n in cached_fibonaci

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


with open("17.out_tin", 'w') as outFile:
    with open("17.in", 'r') as inFile:
        no_of_test_cases = int(next(inFile)) # read first line
        print no_of_test_cases

        for line in inFile: # read rest of lines
            values = ([int(x) for x in line.strip().split()])

            s = set(values)
            mn = min(values)
            mx = max(values)
            a = []
            for each in cached_fibonaci:
                if mn <= each <= mx and each not in s:
                    a.append(each)

            # print values

            for i in a:
                outFile.write(str(i) + ' ')
            outFile.write('\n')
