def is_year_leap(year):
    if year % 4 == 0 and year % 100 != 0: 
        return True
    elif year % 4 == 0 and year % 100 == 0 and year % 400 == 0:
        return True
    else:
        return False


def days_in_month(year, month):
    months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    # Number of days in each month
   
    if is_year_leap(year) is True:
        months[1] = 29 # Taking leap years into account
        
    for i in months:
        if 1 <= month <= 12:
            return months[month - 1]
        else:
            return None

test_years = [1900, 2000, 2016, 1987]
test_months = [2, 2, 1, 11]
test_results = [28, 29, 31, 30]
for i in range(len(test_years)):
	yr = test_years[i]
	mo = test_months[i]
	print(yr, mo, "->", end="")
	result = days_in_month(yr, mo)
	if result == test_results[i]:
		print("OK")
	else:
		print("Failed")
