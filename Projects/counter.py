import os, time

def ascending():
    print('\n-Ascending Counting Script ...')
    start = int(input('\n- Set Start Time Per Seconds : \n\n>> '))
    end = int(input('\n- Set End Time : \n\n>> '))
    while end > start :
        os.system('cls')
        for count in range(start, end):
            print(count) 
            time.sleep(1)
            os.system('cls')
            start += 1

def descending():
    print('\n- Descending Counting Script ...')
    start = int(input('\n-Set Time By Seconds : \n\n>> '))
    while start > 0:
        os.system('cls')
        print(start)
        time.sleep(1)
        start -= 1
    os.system('cls')
    print('💣 BOOOOOOOM')

def count():
    typeOfCount = input(
'''
    ============================================================================

                            COUNTING SCRIPT

    ============================================================================

    - for :

        >> Ascending COUNTING Write The Command [ coun -a ]

        >> Descending COUNTING Script Write The Command [ coun -d ]

        >> ''')
    if typeOfCount == 'coun -a':
        ascending()
    elif typeOfCount == 'coun -d':
        descending()

count()