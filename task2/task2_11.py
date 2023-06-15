# 11. Create a function that will return how many work days there are until the weekend, given the current day.

days = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]

current_day_nr = days.index("Saturday") + 1
# current_day_nr = days.index("Monday") + 1
weekend = days.index("Saturday") + 1

# print(days[-2:])
if current_day_nr > 5:
	print(f"it's weekend, it's {days[current_day_nr-1]}")
else:
	print(f"{weekend - current_day_nr} day left till weekend")