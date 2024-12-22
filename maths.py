import os
class MathOperations:
    def __init__(self):
        pass

    def multipliTable(self):
        number = int(input('\n- multiplication [ x ] table of which number ( ? )  : \n\n-> '))
        max_range = int(input('\n- set the max range of the operation : '))
        os.system('cls')
        for i in range(0, max_range):
            print('_'*50)
            print(f'- {number} x {i} =', number * i)

    def subTable(self):
        
        number = int(input('\n- substriction [ - ] table of which number ( ? )  : \n\n-> '))
        max_range = int(input('\n- set the max range of the operation : '))
        os.system('cls')
        for i in range(0, max_range):
            print('_'*50)
            print(f'- {number} - {i} =', number - i)
        

    def load(self):
        select = input(
'''

    ** Table Selection :

    1) Multiplication Table

    2) substriction Table

    >> ''')
        if select == '1':
            MathOperations().multipliTable()
        elif select == '2':
            MathOperations().subTable()
           


MathOperations().load()