# 10. Given a number n create a list with first n fibonacci numbers.
nr1, nr2 = 0, 1
n = 10
arr = [nr1]

for i in range(n):
    f_sum = nr1 + nr2
    nr1, nr2 = nr2, f_sum
    arr.append(f_sum)

print(arr)
