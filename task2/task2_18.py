# 18. Given an unlimited supply of coins of given denominations, find the minimum number of 
# coins required to get the desired change.

def get_keys_by_value(dict_obj, value):
    return [k for k, v in dict_obj.items() if v == value]

denominations = [1, 5, 10, 50]

change = 47
denominations.sort(reverse=True)

coin_sum = []
for i in denominations:
	print()
	print(f"coin 	{i}")
	print(f"change  {change}")
	print(f"coins   {coin_sum}")
	if i > change:
		continue
	else:
		print("\t",int(change/i))
		temp = int(change/i)
		temp_sum  = []
		for x in range(temp):
			# coin_sum.append(int(change/i))
			temp_sum.append(i)
			coin_sum.append(i)
			print("\t\t x   	", x)
			print("\t\t sum 	",sum(coin_sum))
		change = change - sum(temp_sum)

print(f"coins {coin_sum} \
	\ncoin_sum {sum(coin_sum)}")