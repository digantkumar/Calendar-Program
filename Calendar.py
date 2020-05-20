# Digant Kumar
# Calendar Program

# Returns true if the given year is leap year
# A year is a leap year if it is divisible by 4 and not divisible by 100. But if a year is divisible by 400
# It is considered to be a leap year

def is_leap(year):
    if year%4 == 0 or year%400 == 0:
        return True
    elif year%4 == 0 and year%100 == 0:
        return False
    else:
        return False

# Counting the number of days in a given month in the given year
# Here 1,2,3..12 specifies the order of the months from Jan till December.
def num_days(month,year):
    leap_year = is_leap(year)
    if leap_year:
        if month == 2:
            return 29
        elif month == 9 or month == 4 or month == 6 or month == 11:
            return 30
        else:
            return 31
    if not leap_year:
        if month == 2:
            return 28
        elif month == 9 or month == 4 or month == 6 or month == 11:
            return 30
        else:
            return 31

# The following function returns the start date of the given month in the given year.
# According to the program we are only allowed to take years from 2000 till 2099.
def start_day(month,year):
    start_year = 2000
    start_month = 1
    total_days = 0
    for yr in range(start_year,year+1):
        for mm in range(start_month,13):
            if yr == year and mm == month:
                break
            total_days = total_days + num_days(mm,yr)
    return (total_days + 6)%7                               # Adding 6 as Jan 2000 began on a Saturday

# Pretty printing the calendar for a given month in a given year
def cal(month,year):
    print("%4s %3s %3s %3s %2s %3s %3s" %("Su","Mu","Tu","We","Th","Fr","Sa"))
    num_of_day = num_days(month,year)            # Storing the number of days
    starting_month = start_day(month,year)        # Storing the starting month
    date = 1
    for k in range(1,starting_month):
        print("    ",end="")
    for l in range(starting_month,7):
        print("%5d" %date, end="")
        date = date + 1
    while date < num_of_day:
        print("")
        for i in range(7):
            print("%4d" %date, end="")
            date = date + 1
            if date > num_of_day:
                break
    return " "

