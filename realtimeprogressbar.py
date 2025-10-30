import os

def rt_progress_bar(count = len(os.listdir())):
    path = 'c:\\Users\\lenovo\\Documents\\PythonProjects'
    for files in os.listdir():
        os.system(f'move {files} {path}')
        

rt_progress_bar()