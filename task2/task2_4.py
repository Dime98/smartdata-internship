# 4. Write a program to check whether the sequence of numbers 1, 2, 3 appears in a given 
# array of integers somewhere.

# arr = [3,12,1,2,4,1,2]

def arr_to_str(arr):
	arr_str = ""
	for i in arr:
		# added , in case the seq is 1, 2, 33
		arr_str += str(i) + ","
	return arr_str

# init array and 1, 2, 3 sequence
# arr = [1,2,3,4,1,2]
arr = [3,12,1,2,3,4,1,2]
check_seq = [1,2,3]

# # convert array to string
# str_arr = arr_to_str(arr)
# # print(str_arr)

# check_seq_str = arr_to_str(check_seq)
# # print(check_seq_str)

# # check for sequence
# seq_index = str_arr.find(check_seq_str)
# if seq_index == -1:
# 	print(f"{check_seq} not found")
# else:
# 	print(f"{check_seq} sequence found @ index[{seq_index}:{seq_index+len(check_seq)}]")

check_seq_len = len(check_seq)
for i in range(len(arr) - check_seq_len + 1):
	if arr[i:i+check_seq_len] == check_seq:
		print(f"{check_seq} sequence found @ index[{i}]")


