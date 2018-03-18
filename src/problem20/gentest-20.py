#!/usr/bin/python
import string
import random

NUMBER_OF_TEST_CASES = 1000
MIN_KEY_COUNT = 1
MAX_KEY_COUNT = 10
MIN_TEXT_COUNT = 10
MAX_TEXT_COUNT = 1000
RANDOM_SEED = 50205

random.seed(RANDOM_SEED)

SPECIAL_TEST_LOCATION = 500
SPECIAL_TESTS = ["abc abcabcabcabcabc",
				 "bca abcabcabcabcabc",
				 "abca abcabcabcabcabc",
				 "abcabcabcabcabc abcabcabcabcabc"]

def printSpecialTests(outFile):
	for test in SPECIAL_TESTS:
		outFile.write(test + '\n')

with open("20.in", 'w') as outFile:
	outFile.write(str(NUMBER_OF_TEST_CASES + len(SPECIAL_TESTS)) + '\n')

	for i in range(0, NUMBER_OF_TEST_CASES):
		count = random.randint(MIN_TEXT_COUNT, MAX_TEXT_COUNT)

		characters = []
		for n in range(0, count):
			value = random.choice(string.letters)
			characters.append(value)
		text = ''.join(characters)

		keyword_start = random.randint(0, len(characters) - 5)
		keyword_length = random.randint(MIN_KEY_COUNT, MAX_KEY_COUNT)
		keyword_end = keyword_start + keyword_length
		if keyword_end >= len(characters):
			keyword_end = len(characters) - 1
		keyword = text[keyword_start:keyword_end]

		outFile.write(keyword + ' ' + text)
		outFile.write('\n')

		if i == SPECIAL_TEST_LOCATION:
			printSpecialTests(outFile)
