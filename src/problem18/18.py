#!/usr/bin/python
import sys

characters_maps = ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

def shift_character(character, shift_number):
	index = characters_maps.index(character)
	shifted_index = index + shift_number
	while shifted_index >= len(characters_maps):
		shifted_index -= len(characters_maps)
	while shifted_index < 0:
		shifted_index += len(characters_maps)

	return characters_maps[shifted_index]


def rotate_string(input, shift_number):
	output = ""
	for c in input:
		output += shift_character(c, shift_number)
	return output;


with open("18.out", 'w') as outFile:
	with open("18.in", 'r') as inFile:
		no_of_test_cases = int(next(inFile)) # read first line
		print no_of_test_cases

		for line in inFile: # read rest of lines
			values = ([x for x in line.split()])
			# print values

			shift = int(values[0])
			string = ''.join(values[1:])
			rotated_string = rotate_string(string, shift)

			outFile.write(rotated_string)
			outFile.write('\n')


