# 20. Write a function that would rotate a list n places to the left.

lst = [1,2,3,4,5,6]

n = 3

# lst2 = []
# for i in range(len(lst)):
#     lst2.append(lst[i-n])
# print(lst2)

lst = [lst[i-n] for i in range(len(lst))]
print(lst)