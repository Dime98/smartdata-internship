# 16. Given an array of positive integers, find the smallest subarray's length whose sum of 
# elements is greater than a given number k.

arr = [1,10,2,8,3,12]

k = 15

grater_than_k = []
for i in range(len(arr)):
	x = i
	# loop till end to find sum more than k
	while x < len(arr):
		if sum(arr[i:x]) > k:
			grater_than_k.append(arr[i:x])
		x += 1

# get the length of each subarray grater than k
lengths = [len(i) for i in grater_than_k]
shortest_len = min(lengths)
print(grater_than_k[lengths.index(shortest_len)])
# print()
# for i in grater_than_k:
# 	print(i, sum(i), len(i))