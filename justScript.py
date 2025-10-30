import os
from time import sleep

times = 3
print('- the script is runnung ...')
for time in range(1, times):
    print(f'process n°: {time}')
    sleep(1.)
    os.startfile("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe")