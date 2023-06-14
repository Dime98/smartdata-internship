# 30. Given an M x N integer matrix, print it in spiral order.
# Input:
# [  1   2   3   4  5 ]
# [ 16  17  18  19  6 ]
# [ 15  24  25  20  7 ]
# [ 14  23  22  21  8 ]
# [ 13  12  11  10  9 ]
 
# Output:
# 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25

import numpy as np

N, M = 4, 4
np_arr = np.random.randint(10, size=(N,M))
# print(np_arr)
for i in np_arr:
    print(i)

print()
# print(np_arr[:,2])
# n, m = N-1, M-1
n, m = 0, 0
move_vert, move_horis = 0, 0
for i in range(M):
    for x in range(10):
        if x %2 == 0:
            move_vert = 0
            move_horis = 0
        while move != N:
            print(np_arr[0,move])
            move += 1
    
