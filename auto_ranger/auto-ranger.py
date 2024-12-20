import os
import shutil


class AutoRanger:
    def __init__(self):
        print("                            Ranging Program By {'PyQonsole': 'Khalil'}")
        print('\n\n>> this program is for automate files to move to directories followed by file extension')
        pass
    def do(self):
        extensions = [
            '.msi','.exe', '.mp3',
            '.mp4', '.zip', '.rar',
            '.png', '.jpg', '.py'
        ]
        input('\n\n>> Press Enter To Start Reranging !! >> ')
        files = os.listdir()
        for file in files:
            if file.endswith('.py'):
                try:
                    os.mkdir('Python-Files')
                except OSError:
                    pass
                shutil.copy(file, 'Python-Files')
                os.remove(file)
            elif file.endswith('.mp3'):
                try:
                    os.mkdir('Musics')
                except OSError:
                    pass
                shutil.copy(file, 'Musics')
                os.remove(file)
            elif file.endswith('.mp4'):
                try:
                    os.mkdir('Videos')
                except OSError:
                    pass
                shutil.copy(file, 'Videos')
                os.remove(file)
            elif file.endswith('.zip'):
                try:
                    os.mkdir('Compressed')
                except OSError:
                    pass
                shutil.copy(file, 'Compressed')
                os.remove(file)
            elif file.endswith('.rar'):
                try:
                    os.mkdir('Compressed')
                except OSError:
                    pass
                shutil.copy(file, 'Compressed')
                os.remove(file)
            elif file.endswith('.png'):
                try:
                    os.mkdir('Pictures')
                except OSError:
                    pass
                shutil.copy(file, 'Pictures')
                os.remove(file)
            elif file.endswith('.jpg'):
                try:
                    os.mkdir('Pictures')
                except OSError:
                    pass
                shutil.copy(file, 'Pictures')
                os.remove(file)
            elif file.endswith('.exe'):
                try:
                    os.mkdir('Programms')
                except OSError:
                    pass
                shutil.copy(file, 'Programms')
                os.remove(file)
            elif file.endswith('.msi'):
                try:
                    os.mkdir('Programms')
                except OSError:
                    pass
                shutil.copy(file, 'Programms')
                os.remove(file)
            
        print('\nReranged !!')

AutoRanger().do()
