from datetime import datetime
import textwrap, os, json
from termcolor import cprint


class TaskManager:
    def __init__(self):
        pass

        

    def new_task(self, new = True):

        while new:
            self.task = input('\n\n- Enter Task Bellow \n\n-> ')
            now_dt = datetime.now()
            self.dt = datetime.strftime(now_dt, "%d/%m/%Y, %H:%M:%S")
            print('\n- add date & time for the task (D-M-Y, H:M:S): '.title())

            self.setted_dt = datetime(

                year = int(input('\n- set year : ')),
                month = int(input('\n- set month : ')),
                day = int(input('\n- set day : ')),
                hour = int(input('\n- set hour : ')),
                minute = int(input('\n- set minutes : ')),
                second = int(input('\n- set seconds : '))

                )
            cprint('\n- Date & Time Of The Task Are Configured !!', 'green')
            saved_task = {
                    "Task": self.task,
                    "Date & Time": f'{
                        self.setted_dt.year,
                        self.setted_dt.month,
                        self.setted_dt.day,
                        self.setted_dt.hour,
                        self.setted_dt.minute,
                        self.setted_dt.second
                        }'
                }
            
            try:
                cprint('\n- Task Saved !!')
                os.mkdir('tasks')
                with open('tasks\\Tasks.json', 'a') as t:
                    t.write(json.dumps([saved_task], indent=4))
                    t.close()

            except FileExistsError:
                with open('tasks\\Tasks.json', 'a') as t:
                    json.dump(saved_task, fp=t, indent=4)
                    t.close()

        

        
            
        

            add_more = input('\n\n- add more ( y or n )??\n\n-> ')
            if add_more == 'y':
                new = True
            elif add_more == 'n':
                new = False
                print('\n- Exit ...')
                break
        return saved_task

    def run(self):
        select = input(
'''
_________________________________________________________________________
 _____         _         __  __                                   
|_   _|_ _ ___| | __    |  \/  | __ _ _ __   __ _  __ _  ___ _ __ 
  | |/ _` / __| |/ /____| |\/| |/ _` | '_ \ / _` |/ _` |/ _ \ '__|
  | | (_| \__ \   <_____| |  | | (_| | | | | (_| | (_| |  __/ |   
  |_|\__,_|___/_|\_\    |_|  |_|\__,_|_| |_|\__,_|\__, |\___|_|   
                                                  |___/           
_________________________________________________________________________

(1) New Task 

(2) Show Saved Tasks

>> ''')
        if select == '1':
            self.new_task()
        elif select == '2':
            self.saved_tasks()


TaskManager().run()

