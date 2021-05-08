def is_year_leap(year):
    if year % 4 == 0 and year % 100 != 0: 
        return True
    elif year % 4 == 0 and year % 100 == 0 and year % 400 == 0:
        return True
    else:
        return False

def days_in_month(year, month):
    months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
   
    if is_year_leap(year) is True:
        months[1] = 29
        
    for i in months:
        if 1 <= month <= 12:
            return months[month - 1]
        else:
            return None

def day_of_year(year, month, day):
    
    year_length = 365
    
    if is_year_leap(year) is True:
        year_length = 366
        
    current_month = days_in_month(year, month)
    
    months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    if is_year_leap(year) is True:
        months[1] = 29
    
    total_days = 0
    
    for i in range(month):
        total_days += months[i]
        
    total_days += (current_month - day)
    
    return total_days

print(day_of_year(2000, 11, 30))
