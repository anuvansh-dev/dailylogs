"""
Write a program that will tell whether the given year is a leap year
or not.

Leap year is either divisible by 400 or divisible by 4 but not by 100
"""

def is_leap_year(year):
    if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
        return True
    else:
        return False

print(is_leap_year(2023))