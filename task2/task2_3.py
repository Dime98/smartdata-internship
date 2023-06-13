# 3. Write a program that checks if three given integers are in the range of 20 to 50 
# (inclusive) and returns true if at least one of them is within the range. If none of the 
# integers are within the range, the program returns false.

def check_number(nr, range_low, range_high):
	if 20 <= nr <= 50:
		return True
	else:
		return False

nr = 50
print(check_number(nr, 20, 50))