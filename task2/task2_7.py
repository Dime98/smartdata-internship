# 7. Generate a multiplication table for all numbers from 1 to 10.

arr = [1,2,3,4,5,6,7,8,9,10]

print(arr)

for i in arr:
	print()
	for j in arr:
		print(f"{i} * {j} = {i*j}")
