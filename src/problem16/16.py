#!/usr/bin/python
import sys

def findLocalExtreme(inputs):
	isLocalExtreme = True
	localExtremePositions = []
	count = len(inputs)

	for i in range(0, count):
		isLocalExtreme = False

		if i - 1 < 0:
			isLocalExtreme = False
		elif i + 1 >= count:
			isLocalExtreme = False
		elif inputs[i] < inputs[i-1] and inputs[i] < inputs[i+1]:
			isLocalExtreme = True
		elif inputs[i] > inputs[i-1] and inputs[i] > inputs[i+1]:
			isLocalExtreme = True

		if isLocalExtreme == True:
			localExtremePositions.append(i)

	return localExtremePositions


with open("16.out", 'w') as outFile:
	with open("16.in", 'r') as inFile:
		no_of_test_cases = int(next(inFile)) # read first line
		print no_of_test_cases

		for line in inFile: # read rest of lines
			values = ([int(x) for x in line.split()])
			# print values

			localExtremePositions = findLocalExtreme(values)
			# print localExtremePositions

			for i in localExtremePositions:
				outFile.write(str(i) + ' ')
			outFile.write('\n')


