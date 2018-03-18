#!/usr/bin/python
import random
import math

QUOTES = ["Misfit Wearables began in 2011-co-founded by Sonny Vu, Sridhar Lyengar, and John Sculley, a former Apple CEO. By the following year, Misfit had launched Shine, its original wearable, and in just over two months after that launch, raised enough money and interest to back the product that would help lead the pack in activity trackers. Misfit began with Shine fitness wearables and like ever-evolving smart technology, we just haven't quit innovating, changing and adding to our wearable technology-and beyond like Beddit, our exclusive sleep monitor device and Bolt, our smart light bulb.,",
		"Hope is a waking dream.",
		"A fool flatters himself, a wise man flatters the fool.",
		"The best way out is always through.",
		"Man never made any material as resilient as the human spirit.",
		"Do not go where the path may lead, go instead where there is no path and leave a trail.",
		"As you walk down the fairway of life you must smell the roses, for you only get to play one round.",
		"A good head and a good heart are always a formidable combination.",
		"Give light and people will find the way.",
		"Don't let the fear of striking out hold you back.",
		"Never argue with a fool, onlookers may not be able to tell the difference.",
		"Always do your best. What you plant now, you will harvest later.",
		"I'd rather regret the things I've done than regret the things I haven't done.",
		"Let each man exercise the art he knows.",
		"Always keep an open mind and a compassionate heart.",
		"Discipline is the bridge between goals and accomplishment.",
		"Act as if what you do makes a difference. It does."]

characters_maps = ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

def remove_invalid_characters(input):
	characters = list(input)
	i = 0
	while(i < len(characters)):
		if not characters[i] in characters_maps:
			del characters[i]
		else:
			i += 1
	return ''.join(characters)

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

NUMBER_OF_TEST_CASES = len(QUOTES)
MIN_VALUE = 0
MAX_VALUE = math.pow(2, 10)
RANDOM_SEED = 50205

random.seed(RANDOM_SEED)

with open("18.in", 'w') as outFile:
	outFile.write(str(NUMBER_OF_TEST_CASES) + '\n')

	for i in range(0, NUMBER_OF_TEST_CASES):
		shift = random.randint(MIN_VALUE, MAX_VALUE)
		outFile.write(str(shift) + ' ')

		refined_quote = remove_invalid_characters(QUOTES[i].lower())
		outFile.write(rotate_string(refined_quote, -1 * shift))
		outFile.write('\n')


