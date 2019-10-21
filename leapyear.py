year = input()
leap = int(year) % 4

if (leap == 0):
    print('it is a leap year', year)
else:
    print('it is not a leap year',year)