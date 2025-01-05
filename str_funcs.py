# string variable
from termcolor import colored

condition = True

alpha = colored('Alphabetic', 'green'); digit = colored('Degit', 'red')
alnum = colored('Alphanumeric', 'yellow'); lower = colored('LowerCase', 'cyan')
upper = colored('UpperCase', 'blue')

while condition:
    
    string = input(
    '''
    * Enter Anything To Test String Functions That Returns Boolean Variables:

    >> ''')

    if string.isalpha():
        print(f'\n   - You Entered An Entire - {alpha} - String Variable !!')
    # isdigit()
    if string.isdigit():
        print(f'\n   - You Entered An Entire - {digit} - String Variable !!')
    # isalnum()
    if string.isalnum():
        print(f'\n   - You Entered An Entire - {alnum} - String Variable !!')
    # islower()
    if string.islower():
        print(f'\n   - You Entered An Entire - {lower} -  String Variable !!')
    # isupper()
    if string.isupper():
        print(f'\n   - You Entered An Entire - {upper} -  String Variable !!')
    else:
        pass

    add_new = input('\n\n* Add New String ?\n\n* > ')
    if add_new == 'y' or add_new == 'Y':
        condition = True
    elif add_new == 'n' or add_new == 'N':
        condition == False



