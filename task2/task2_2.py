# 2. Write a program that checks two given integers and returns true if at least one of 
# them is 30 or if their sum is 30. In other words, if either of the two integers is 30 or 
# if their sum equals 30, the program will return true.

def check_numbers(nr1, nr2):
	print(f"nr1: {nr1}")
	print(f"nr2: {nr2}")
	print(f"sum: {nr2 + nr1}")
	if ((nr1 == 30) or (nr2 == 30)) or (nr1 + nr2 == 30):
		return True
	else: return False

nr1 = 15
nr2 = 15

print(check_numbers(nr1, nr2))