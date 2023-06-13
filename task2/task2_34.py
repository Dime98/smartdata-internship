# 34. Given a set of single-digit positive numbers, find all possible combinations of words 
# formed by replacing the continuous digits with corresponding character in the English 
# alphabet, i.e., subset {1} can be replaced by A, {2} can be replaced by B, {10} can be 
# replaced by J, {21} can be replaced by U, etc.

import random
import string
import itertools

letter_indx = {}
for i in range(len(string.ascii_lowercase)):
	letter_indx[i] = string.ascii_lowercase[i]

# for k,v in letter_indx.items():
# 	print(k, v)

arr = [random.randint(0,9) for i in range(3)]
print(arr)

arr_to_letters = []
for i in arr:
	arr_to_letters.append(letter_indx[i])

print(arr_to_letters)

perm_set = itertools.permutations(arr_to_letters)
# print(sum(1 for _ in perm_set))

premutation_to_words = []
for i in perm_set:
	# print(i)
	full_word = ''
	for x in i:
		# print(x)
		full_word += x
	premutation_to_words.append(full_word)


print()
for i in premutation_to_words:
	print(i)