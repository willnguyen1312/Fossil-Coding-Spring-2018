#!/usr/bin/python
import string
import random

NUMBER_OF_TEST_CASES = 1000
MIN_COUNT = 1
MAX_COUNT = 1000
RANDOM_SEED = 50205

SPECIAL_TEST_LOCATION = 500
SPECIAL_TESTS = ["abcdefghijklmnopqrstuvwxyz",
				 "aabbccddeeffgghhiijjkkllmmnnooppqq",
				 "abcdefghijklmnopqrstuvwxyzzyxwvutsrqponmlkjihgfedcba",
				 "abcdefghijklmnopqrstuvwxyzzyxwvutsrqponmlkjihgfedcb"]

def printSpecialTests(outFile):
	for test in SPECIAL_TESTS:
		outFile.write(test + '\n')

random.seed(RANDOM_SEED)

with open("19.in", 'w') as outFile:
	outFile.write(str(NUMBER_OF_TEST_CASES + len(SPECIAL_TESTS)) + '\n')

	for i in range(0, NUMBER_OF_TEST_CASES):
		count = random.randint(MIN_COUNT, MAX_COUNT)

		for n in range(0, count):
			value = random.choice(string.ascii_lowercase)
			outFile.write(str(value))

		outFile.write('\n')
		
		if i == SPECIAL_TEST_LOCATION:
			printSpecialTests(outFile)
