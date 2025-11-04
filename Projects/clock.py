from datetime import datetime
from os import system
from time import sleep

def clock():
    
    while True:
        print(datetime.now().strftime('%H:%M:%S'))
        sleep(1)
        system('cls')

def timer():
    seconds, minute, hour = 59, 59, 00
    for hr in range(hour, -1, -1):
        for min in range(minute, -1, -1):   
           for sec in range(seconds, -1, -1):
            print(f'{hr}:{min}:{sec}')  
            sleep(1) 
            system('cls')
            
if __name__ == '__main__':
    clock()

