# 32. Given a string, find the maximum length contiguous substring of it that is also a 
# palindrome. For example, the longest palindromic substring of "bananas" is "anana", and 
# the longest palindromic substring of "abdcbcdbdcbbc' is "bdcbcdb".

str_arr = ["bananas", "abdcbcdbdcbbc"]
# str_arr = ["bananas",]

palindromic = {}
for i in str_arr:
	# print(i)
	temp_list = []
	for y in range(len(i)):
		x = len(i)
		while x != y + 1:
			# print()
			# print("\t", i[y:x])
			# print("\t", i[y:x][::-1])
			# print(i[:x][::-1])
			x -= 1
			if len(i[y:x]) > 1:
				if i[y:x] == i[y:x][::-1]:
					# print("\t\t palindromic")
					# palindromic[i] = i[y:x]
					temp_list.append(i[y:x])
	palindromic[i] = temp_list

	# break
for k,v in palindromic.items():
	# print(k, v)
	lengths = [len(x) for x in v]
	longest_len = max(lengths)
	# print(lengths)
	# print(longest_len)
	# print(lengths.index(longest_len))
	print(v[lengths.index(longest_len)])

