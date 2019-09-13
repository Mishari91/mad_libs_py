print("Calculator \n")

def calc():

    number_1 = input('Enter your first number:  ')
    if number_1.isdigit():
        True
    else:
        print('Invalid input! Try again. ')
        return calc()
        
    
    
    number_2 = input('Enter your second number:  ')
    if number_2.isdigit():
        True
    else:
        print('Invalid input! Try again. ')
        return calc()
    
    operation = input("please enter your operation '+_/_-_*' : ")

    if operation == '+':
        print(number_1 + number_2)

    elif operation == '/':
        print(number_1 / number_2)

    elif operation == '-':
        print(number_1 - number_2)

    elif operation == '*':
        print(number_1 * number_2)

    else:
        print('Invalid input! Try again. ')
        return calc()

calc()
    



