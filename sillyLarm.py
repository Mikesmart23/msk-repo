import os, datetime
from time import sleep

dt = datetime.datetime.now().strftime('%H:%M:%S')

def alarm(hr, min, sec):
    while True:
        
        if dt == f'{hr}:{min}:{sec}':
            print('match')

        elif dt != f'{hr}:{min}:{sec}':
            pass
        
        os.system('cls')

alarm('08','23','15')