# 18. Given an unlimited supply of coins of given denominations, find the minimum number of 
# coins required to get the desired change.

def get_keys_by_value(dict_obj, value):
    return [k for k, v in dict_obj.items() if v == value]

denominations = [.01, .05, .10, .50]

change = 20

min_nr = {}
for i in denominations:
	min_nr[i] = int(change/i)

shortest_len = min(min_nr.values())
print(f"{get_keys_by_value(min_nr, shortest_len)[0]} minimum number of \
coins required to get {change} change ")