# 11. Create two arrays a and b and initialize them with random numbers. Stack them vertically. 
# Then, try to create another array, stacking arrays a and b horizontally.(take care of their size).

import numpy as np
import random

# =============================
def fix_size(lst):
	print(lst)

# =============================
# a = [random.randint(1,10) for i in range(4)]
# b = [random.randint(1,10) for i in range(5)]
# print(a)
# print(b)

np_a = np.random.randint(1,10,size=(5,))
np_b = np.random.randint(1,10,size=(7,))
print()

print(np_a, np_a.size, np_a.shape)
print(np_b, np_b.size, np_b.shape)
diff = abs(np_a.size - np_b.size)
# print(f"diff {diff}")

# check size
if np_a.size > np_b.size:
	print("np_a.size > np_b.size")
	add_missing = [np.nan for i in range(diff)]
	np_b = np.append(np_b,[add_missing])
if np_a.size < np_b.size:
	print("np_a.size < np_b.size")
	add_missing = [np.nan for i in range(diff)]
	np_a = np.append(np_a,[add_missing])

print()
print(np_a, np_a.size, np_a.shape)
print(np_b, np_b.size, np_b.shape)

# print(np_a)
np_c = np.stack((np_a, np_b), axis = 1)
print(np_c)


np_c = np.stack((np_a, np_b), axis = 0)
print(np_c)