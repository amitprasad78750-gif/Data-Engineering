indicater = True
def is_leap_year(year):
    if year %4 == 0 or year %100 ==0 or year %400 ==0 :
        return "leap year"
    else:
        return "not leap Year"

while indicater:
    result=is_leap_year(int(input("Please enter the year")))
    print(result)
