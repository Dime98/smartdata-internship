# 1. Write a program to compute the sum of the two input values. If the two values are the same, then return triple their sum.
nr1 = input("nr1>> ")
nr2 = input("nr2>> ")

if nr1 == nr2:
	print("numbers are the same, tripling the sum")
	sum2 = int(nr1) + int(nr2)
	print(sum2*3)
else:
	sum1 = int(nr1) + int(nr2)
	print(sum1)