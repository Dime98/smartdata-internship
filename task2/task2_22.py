# 22. Write a function to calculate the prime factorization of an integer.

nr = 75
prime_numbers = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

i = 0
prime_factorization = []
while True:
    # print(i)
    if nr % prime_numbers[i] == 0:
        ret = nr / prime_numbers[i]
        nr = ret
        # print()
        # print(prime_numbers[i])
        # print(ret)
        prime_factorization.append(prime_numbers[i])
        if ret == 1: break
    else:
        if i >= len(prime_numbers) - 1:
            i = 0
        else:
            i += 1

print(prime_factorization)