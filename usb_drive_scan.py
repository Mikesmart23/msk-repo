import os
from time import sleep

path = 'I:\\'
os.chdir(path=path)
for file in os.listdir():
    print(file)
    sleep(1.0)  