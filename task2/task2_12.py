# 12. Create a function that will return the age of a person given their date of birth. Consider
# the current date as the date to count to.
from datetime import datetime

#       y /m /d
dob = '98/12/01'
datetime_object = datetime.strptime(dob, '%y/%m/%d')
# print(type(datetime_object))
# print(datetime_object)  # printed in default format

today = datetime.today()
days = today - datetime_object
print(f"aprox {days.days/365:.2f} years")

# print(today)

# print(datetime_object.month)
# print(today.month)

# print(days.days / 365)
# month_diff = 1 if today.month > datetime_object.month else 0
# print(today.month > datetime_object.month)
# print(month_diff)

# age = today.year - datetime_object.year - 1 
# print(age)