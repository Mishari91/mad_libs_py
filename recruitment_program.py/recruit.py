skills = ['python', 'reading', 'exercise', 'swimming', 'gaming', 'cooking']


user_name = input('what is your name? ')
user_age = int(input('what is your age? '))
user_experience = int(input('How many years of experience do you have? '))

cv = {'name': user_name, 'age': user_age,'experience': user_experience, 'skills':[]}

index = 1
for x in skills:
    print(f'{index}. {x}')
    index+=1


first_skill = input('choose a skill by entering its number:  ')
second_skill = input('choose another a skill by entering its number:  ')

cv['skills'] = first_skill
cv['skills'].append(second_skill)

if (user_age >=25 and user_age <= 40 and
    user_experience >= 1 and
    first_skill or second_skill ==1):

    print('you are accepted ' + user_name.capitalize())

else:
    print('Sorry, you dont meet our criteria.')

    

    

                






