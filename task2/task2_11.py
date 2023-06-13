# 11. Create a function that will return how many work days there are until the weekend, given the current day.

days = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]

current_day_nr = days.index("Monday") + 1
weekend = days.index("Saturday") + 1
print(f"{weekend - current_day_nr} day left till weekend")