#Practice > Algorithms > Implementation > Day of the Programmer

#Julian -> after 1918 (leap year is divisible by 4)
#Gregorian -> from 1919
#During 1918 feb starts from 14.
#Jan + Mar + April + May + June + July + Aug = 215

def dayOfProgrammer(year):
    if year < 1917:
        if year % 4 == 0: #Leap Year
            day = 256 - (215 + 29) #Day Of Programmer always lies on the 256 day of the year.
            if day < 10:
                day = "0" + str(day) #To get the proper output format
        else: #Not a leap year
            day = 256 - (215 + 28)
            if day < 10:
                day = "0" + str(day)

    elif year >= 1919:
         if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):  #Leap Year
             day = 256 - (215 + 29)
             if day < 10:
                 day = "0" + str(day)
         else: #Not a leap year
            day = 256 - (215 + 28)
            if day < 10:
                day = "0" + str(day)

    elif year == 1918:
        day = 256 - (215 + 15) #1918 is not a leap year and feb has only 15 days.
        if day < 10:
            day = "0" + str(day)

    date = str(day) + ".09." + str(year)
    return date

'''
For testing:
year = 1918
print(dayOfProgrammer(year))
'''
