# 5. Write a program to reverse a given array of integers of length 5.
import random

arr = [random.randint(1, 6) for i in range(5)]
print(arr)

print(arr[::-1])