import os
import sys
from tkinter import *
from tkinter.filedialog import askdirectory
from auto_ranger import autoRanger

def load():
    dir_path = askdirectory()
    process = autoRanger.AutoRanger().do()
    if process:
        pass

   

root = Tk()
root.title('Arranger Program By PyQonsole')
root.geometry('480x120')
icon = PhotoImage(file='C:\\Users\\lenovo\\Downloads\\accord.png')
root.iconphoto(True, icon)
run_button = Button(
            master=root,
            text='Choose Directory',
            command=load).place(x=190, y=30)







root.mainloop()











