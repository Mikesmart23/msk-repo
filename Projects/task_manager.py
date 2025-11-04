import datetime
import json


class TaskManager:
    
    def __init__(self, dt = datetime.datetime.now()):
        self.dt = dt

    def new_task(self):
        object = input('\n- Set The Task Object : ')
        year = int(input('- Year : ')) ; month = int(input('- Month : ')) ; day = int(input('- Day : '))
        hour = int(input('- Hour : ')) ; minute = int(input('- Minute : ')) ; second = int(input('- Second : '))

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
==================================================================================
================================== Saved Tasks ===================================
==================================================================================

- Task Object : {loadfile['object']}

- Date & Time : {loadfile['date & time']}

''')
    
    def Menu(self):
        select = input(
'''
==================================================================================
=============================== Task Manager Home ================================
==================================================================================

                      Welcome To Your TaskManager Script

==== - Select A Command From The Lines Bellow By Typing Its Index :

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