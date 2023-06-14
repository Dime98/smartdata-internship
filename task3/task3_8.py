# 8. Create an array of size 4x4 with random numbers. Transform it into a numpy array.

import numpy as np
import random

# generate 4x4 array w/zeroes
arr = [[0]*4 for i in range(4)]
# arr = [[0 for _ in range(4)] for _ in range(4)]

# fill w/random values 
for i in range(4):
	for j in range(4):
		arr[i][j] = random.randint(1,10)

# convert to numpy array
np_arr = np.array(arr)
print(np_arr, type(np_arr))
