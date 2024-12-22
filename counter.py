import os, time


def count():
    typeOfCount = input(        
'''
    ____________________________________________________

                        Counting Script 
    ____________________________________________________

    - For : 
    
        >> Ascend Counting Write The Command [ coun -a ]

        >> Descend Counting Write The Command [ coun -d ] 

        >> ''')

    if typeOfCount == 'coun -a':
        ascending()
    elif typeOfCount == 'coun -d':
        descending()

def ascending():
    print('\n- Ascending Counting Script ...')
    start = int(input('\n- Set Start Time  !!\n\n>> '))
    end = int(input('\n- Set Time End  !!\n\n>> '))
    while end > start:
        os.system('cls')
        for count in range(start, end):
            print(count)
            time.sleep(1)
            os.system('cls')
            start += 1
def descending():
    print('\n- Descending Counting Script ...')
    start = int(input('\n- Set Time By Seconds !!\n\n>> '))
    while start > 0:
        os.system('cls')
        print(start)
        time.sleep(1)
        os.system('cls')
        start -= 1
    print('💣 BOOOOOOOM')

if __name__ == '__main__':
    count()