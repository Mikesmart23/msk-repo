import os
from time import sleep

class Xscanner:
    
    def __init__(self, hard_drives = ['C:\\', 'D:\\']):
        self.hard_drives = hard_drives
        
    
    def analyse(self, directories = [], is_file = []):
        for hard_drive in self.hard_drives:
            os.chdir(hard_drive)
            for files in os.listdir():
                directories.append(hard_drive + files)   
                
        for path in directories:
            try:
                os.chdir(path)
                for dir in os.listdir():
                    sleep(0.2)
                    os.chdir(f'{path}\\{dir}')
                    if len(os.listdir()) == 0:
                            pass
                    else:
                        print('*~*-*' * 15)
                        full_dir = f'*~*    📁 {path}\\{dir}'
                        print(full_dir)
                        
                    for files in os.listdir():
                        file_size = int((os.lstat(files).st_size / 1024))
                        print('*~*    📄', files, f'[ {file_size} ] Ko')
                        sleep(0.5)                   
                
            except NotADirectoryError:
                is_file.append(path)
            except PermissionError:
                pass

if __name__ == '__main__':
    print(Xscanner().analyse())