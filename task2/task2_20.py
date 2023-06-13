# 20. Write a function that would rotate a list n places to the left.

lst = [1,2,3,4,5,6]

lst2 = []
n = 3
for i in range(len(lst)):
    print(lst[i])
    lst2.append(lst[i-n])

print()
print(lst2)