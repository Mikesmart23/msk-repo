import datetime
import json
from termcolor import colored

description = colored('Description', 'light_green')
saved_tasks = colored('Saved Tasks', 'light_green')

class TaskManager:
    
    def __init__(self, dt = datetime.datetime.now()):
        self.dt = dt

    def new_task(self):
        object = input('\n- Set The Task Object : ')
        year = int(input('\n- Year : ')) ; month = int(input('\n- Month : ')) ; day = int(input('\n- Day : '))
        hour = int(input('\n- Hour : ')) ; minute = int(input('\n- Minute : ')) ; second = int(input('\n- Second : '))

        set_time = datetime.datetime(year=year, month=month, day=day,    
                                    hour=hour, minute=minute, second=second)
        with open('MyTasks.json', 'a') as data:
            data.write(json.dumps({
                "object" : object,
                "date & time" : str(set_time)
        }, indent=4))
            
    def check_tasks(self):
        with open('MyTasks.json', 'r') as json_file:
            loadfile = json.loads(json_file.read())
            print(
f'''
==== {saved_tasks} :

- Task Object : {loadfile['object']}

- Date & Time : {loadfile['date & time']}

''')
    
    def Menu(self):
        select = input(
f'''==================================================================================

=============================== Task Manager Home ================================

==================================================================================

==== {description} : Select A Command From The Lines Bellow By Typing Its Index 

     Then Press Enter :

==== 1 - Add New Task 

==== 2 - Check Tasks

==== ? -> ''')
        if select == '1':
            TaskManager().new_task()
        elif select == '2':
            TaskManager().check_tasks()
        else:
            print('\nError, Try Again !!')


if __name__ == '__main__':
    TaskManager().Menu()