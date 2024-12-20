
class MathOperation:
    def __init__(self):
        pass

    def multipliTable(self):
        number = int(input('- multiplication [ x ] table of ( ? ) number : \n\n-> '))
        max_range = int(input('\n- set the max range of the operation : '))
        for i in range(0, max_range):
            print('_'*50)
            print(f'- {number} x {i} =', number * i)
           


MathOperation().multipliTable()