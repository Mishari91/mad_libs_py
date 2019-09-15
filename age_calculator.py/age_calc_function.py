### Birthday Calculator ###

from datetime import date

def check_birthdate(year, month, day):
    
    difference = date.today() - birth_date
    difference_in_days = difference.days

    if difference_in_days <= 0:
        return False
    else:
        True

def calculate_age(year, month, day):
    live = date.today()
    difference = date.today() - birth_date
    years_old = difference.years
    
    print('Your Age in years is ... ' + years_old)

birth_date = year, month, day = input('Enter your birthdate by year month then day each followed by a space! :  ').split()
birth_date.date()
if check_birthdate(year, month, day) == True:
    calculate_age(year, month, day)
else:
    print('The birthdate is Invalid !! ')



        

    
    
