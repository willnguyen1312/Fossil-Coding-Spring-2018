#!/usr/bin/python
import random

NUMBER_OF_TEST_CASES = 1000
MIN_COUNT = 1
MAX_COUNT = 1000
MIN_VALUE = 0
MAX_VALUE = 2^32
RANDOM_SEED = 50205

random.seed(RANDOM_SEED)

def printSpecialTestCases(outFile):
	for i in range(0, len(SPECIAL_TEST_CASES)):
		outFile.write(SPECIAL_TEST_CASES[i])

with open("16.in", 'w') as outFile:
	outFile.write(str(NUMBER_OF_TEST_CASES) + '\n')

	for i in range(0, NUMBER_OF_TEST_CASES):
		count = random.randint(MIN_COUNT, MAX_COUNT)

		for n in range(0, count):
			value = random.randint(MIN_VALUE, MAX_VALUE)
			outFile.write(str(value))
			outFile.write(' ')

		outFile.write('\n')
