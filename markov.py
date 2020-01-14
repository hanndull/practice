from random import choice, randint

sample = "I am such a happy lass, I am. Oh, yes, happy indeed. What a fine day it is. The weather makes me happy when it is sunny."

def create_chains(sample):
	'''create dict of trailing word options for each word in sample list'''
	
	sample_list = sample.split()
	sample_dict = {}
	index = 1
	length = len(sample_list)

	for word in sample_list:

		if length > index:

			if not sample_dict.get(word):
				sample_dict[word] = [sample_list[index]]
			
			else:
				sample_dict[word].append(sample_list[index])

			index += 1

		else: 
			sample_dict[word] = []

	return(sample_dict)


def scramble_sample(sample_dict, sample):
	'''starts scramble with a random sample word, and starts there, trailing from the markov dict'''

	sample_list = sample.split()
	random_length = randint(len(sample_list), len(sample_list)*2)
	scramble = [choice(sample_list)]
	scramble_length = 1

	while scramble_length < random_length:
		last_word = scramble[-1]

		if sample_dict[last_word] != []:
			scramble.append(choice(sample_dict[last_word]))
			scramble_length += 1
		
		else:
			return(scramble)
	
	return(scramble)


def print_result(sample):
	'''Utilizes other 2 functions to return scrambled sample'''

	sample_dict = create_chains(sample)

	return (scramble_sample(sample_dict, sample))




	

