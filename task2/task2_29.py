# 29. Given an integer array, find out the minimum and maximum element present using minimum 
# comparisons.


arr = [12, 1, -14, 32, 6, 16]

min_val, max_val = arr[0], arr[0]

# print(min_val, max_val)
for i in arr:
    if i < min_val:
        min_val = i
    if i > max_val:
        max_val = i

print(min_val)
print(max_val)