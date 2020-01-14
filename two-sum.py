def two_sum(arr, num):
	nums_dict = {}
	index = 0
	for int in arr:
		nums_dict[int] = index
		index += 1
	for int in arr:
		target = abs(num - int)
		if nums_dict.get(target):
			return(nums_dict[int], nums_dict[abs(num - int)])
	return("No matches")

print(two_sum([1,3,5], 8))
