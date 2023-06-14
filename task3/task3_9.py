# 9. Create and initialize an array of size 4x4 with random numbers. Replace all odd numbers in arr with -1.

import numpy as np
import random

# non numpy
# generate 4x4 array w/zeroes
arr = [[0]*4 for i in range(4)]
# arr = [[0 for _ in range(4)] for _ in range(4)]

# fill w/random values 
for i in range(4):
	for j in range(4):
		arr[i][j] = random.randint(1,10)

print(arr)

# quetion, can this replacing be done w/lst comprehension
# arr = [arr[i][j] for i in range(4) for j in range(4) if arr[i][j] %2 == 0]
for i in range(4):
	for j in range(4):
		if arr[i][j] %2 == 0:
			# print(i)
			arr[i][j] = -1
print(arr)

# ====================================
# with numpy
print()
# np_arr = np.random.random((4,4))
np_arr = np.random.randint(1,10,size=(4,4))
print(np_arr)
# print(np_arr %2 == 0)
np_arr[np_arr %2 == 0] = -1
print(np_arr)

