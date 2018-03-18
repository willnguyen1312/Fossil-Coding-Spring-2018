#!/usr/bin/python
import sys

def removeNeighboringDuplicateCharacters(input):
	characters = list(input)

	found = True
	while(found):
		found = False
		for i in range(0, len(characters) - 1):
			if characters[i] == characters[i+1]:
				del characters[i+1]
				del characters[i]
				found = True
				break
	
	if len(characters) == 0:
		return "Empty String"

	return ''.join(characters)


with open("19.out", 'w') as outFile:
	with open("19.in", 'r') as inFile:
		no_of_test_cases = int(next(inFile)) # read first line
		print no_of_test_cases

		for line in inFile: # read rest of lines
			result = removeNeighboringDuplicateCharacters(line.strip())
			outFile.write(result)
			outFile.write('\n')
			


