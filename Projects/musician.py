import os
import shutil

class Favor:
    def __init__(self,
                favor_artist = ['Samara', 'La mass', 'Maes'],
                path = 'C:\\Users\\lenovo\\Music\\mix'):
        self.favor_artist = favor_artist
        self.path = path

    def create_dir(self):
        os.chdir(self.path)
        os.mkdir('Samara')
        for files in os.listdir():
            if 'Samara' in files or files.startswith('Samara') is True:
            
                
                print(os.getcwd())
                shutil.copy(files, 'Samara')
                os.remove(files)
                print('Done ...')
                
if __name__ == '__main__':
    Favor().create_dir()
