# 10. Given a number n create a list with first n fibonacci numbers.
nr1 = 0
nr2 = 1
n = 10
for i in range(n):
    # print(f"nr1 {nr1}")
    # print(f"nr2 {nr2}")
    f_sum = nr1 + nr2
    # print(f"sum {f_sum}")
    nr1 = nr2
    nr2 = f_sum
    print(f_sum)
