year, month, day = input().split()
year = int(year)
month = int(month)
day = int(day)
year1, month1, day1 = input().split()
year1 = int(year1)
month1 = int(month1)
day1 = int(day1)
if year == year1 and day == day1 and month == month1:
    print('Same')
elif year > year1:
    print("After")
elif month > month1:
    print("After")
elif day > day1:
    print("After")
else:
    print("Before")