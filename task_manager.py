import datetime
import json


class TaskManager:
    
    def __init__(self, dt = datetime.datetime.now()):
        self.dt = dt

    def new_task(self):
        object = input('Set The Task Object : ')
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
            print('\n', json_file.read())
    
    def Menu(self):
        select = input(
'''
__________________ Task Manager Home _________________

- Select an Option From List Bellow :

1 - Add New Task 

2 - Check Tasks

? -> ''')
        if select == '1':
            TaskManager().new_task()
        elif select == '2':
            TaskManager().check_tasks()
        else:
            print('\nError, Try Again !!')


if __name__ == '__main__':
    TaskManager().Menu()