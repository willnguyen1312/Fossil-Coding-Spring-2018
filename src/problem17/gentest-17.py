#!/usr/bin/python
import random
import math

NUMBER_OF_TEST_CASES = 100
MIN_COUNT = 1
MAX_COUNT = 1000
MIN_VALUE = 0
MAX_VALUE = 1024 * 1024
RANDOM_SEED = 101742

random.seed(RANDOM_SEED)

with open("17.in", 'w') as outFile:
	outFile.write(str(NUMBER_OF_TEST_CASES) + '\n')
	print MAX_VALUE
	for i in range(0, NUMBER_OF_TEST_CASES):
		count = random.randint(MIN_COUNT, MAX_COUNT)
		# outFile.write(str(count))
		# outFile.write(' ')

		for n in range(0, count):
			value = random.randint(MIN_VALUE, MAX_VALUE)
			outFile.write(str(value))
			outFile.write(' ')

		outFile.write('\n')
