
import os
from time import sleep

GBA_PATH = 'D:\\RG35XX\\Roms\\GBA'
os.chdir(GBA_PATH)
for games in os.listdir():
    print(games)
    sleep(1.0)
