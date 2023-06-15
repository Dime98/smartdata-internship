# 27. Given a positive number n, efficiently generate binary numbers between 1 and n in 
# linear time.

import random

# print(random.randint(0,1))

n = 10
for i in range(n):
	print(f"{i} || {random.randint(0,n):04b} ")
	# print(random.randint(0,n))
# arr = [random.randint(0,1) for i in range(n)]
# print(arr)