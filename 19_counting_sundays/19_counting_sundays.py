"""
How many Sundays fell on the first of the month during the twentieth century
(1 Jan 1901 to 31 Dec 2000)?
"""

days_in_month = [31,28,31,30,31,30,31,31,30,31,30,31]

def next_day(date):
    day = (date[0] +1)
    month = date[1]
    year = date[2]
    if day>days_in_month[month-1]:
        month += 1
        day = 1
        if month > 12:
            month = 1
            year += 1
    ndate = [day,month,year]
    return ndate

next_day([1,12,1906])
date = [1,1,1901]
weekday = 1
suma = 0
while date[2]<2001:
    date = next_day(date)
    print(date)
    if (date[0] == 1) & (weekday == 0):
        print('COMIDA')
        suma += 1
    weekday = (weekday + 1)%7
    print(weekday)
print(suma)
