#!/usr/bin/python
def countNumberOfOccurences(keyword, text):
	found = 0
	index = 0
	while index < len(text):
		found_index = text.find(keyword, index)
		if found_index > -1:
			found += 1
			index = found_index + 1
		else:
			index += 1

	return found

with open("20.out", 'w') as outFile:
	with open("20.in", 'r') as inFile:
		no_of_test_cases = int(next(inFile)) # read first line
		print no_of_test_cases

		for line in inFile: # read rest of lines
			values = ([x for x in line.split()])
			result = countNumberOfOccurences(values[0], values[1])
			outFile.write(str(result))
			outFile.write('\n')
