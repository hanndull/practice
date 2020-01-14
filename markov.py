sample = "I am such a happy lass, I am. Oh, yes, happy indeed. What a fine day it is. The weather makes me happy when it is sunny."

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



print(sample_dict)