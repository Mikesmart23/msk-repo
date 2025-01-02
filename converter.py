import os
from time import sleep


class ConverterSim:
    def __init__(self):
        pass

    def video_convert():
        print('\n        * Wait A Second ... ')
        sleep(1.0)
        print('\n** [ ConverterSim ] Video Converter **')
        filePath = input('\n- Paste Video Directory Path Bellow > " C:\\Users\\lenovo\\Videos "\n\n- > ')
        os.chdir(filePath)
        
        select = input(
    ''' 
=========================================================================

        * Video-Converter [ Available Formats ]:

        1) > [ mp4 ] -- Moving Picture Experts Group - 4
        
        2) > [ mkv ] -- Matroska Vidéo
        
        3) > [ wmv ] -- Windows Media Video
        
        4) > [ flv ] -- Flash Video

        5) > [ ADD NEW FORMATS ??? ] 
        
        ?) - Enter the format to convert to [ ??? ] >> ''')
        
        
        files = os.listdir()
        try:
            for index, file in enumerate(files):
                extension = file.split()[-1]
                os.rename(file, f'{index}.{select}')
            input('\n        * Press Enter To Exit !! ')
        except:
            pass
            
    def picture_convert():
        pass

    def convert():
        select = input(
'''
=====================================================================================


 _______  _______  _                 _______  _______ _________ _______  _______  _______ _________ _______ 
(  ____ \(  ___  )( (    /||\     /|(  ____ \(  ____ )\__   __/(  ____ \(  ____ )(  ____ \\__   __/(       )
| (    \/| (   ) ||  \  ( || )   ( || (    \/| (    )|   ) (   | (    \/| (    )|| (    \/   ) (   | () () |
| |      | |   | ||   \ | || |   | || (__    | (____)|   | |   | (__    | (____)|| (_____    | |   | || || |
| |      | |   | || (\ \) |( (   ) )|  __)   |     __)   | |   |  __)   |     __)(_____  )   | |   | |(_)| |
| |      | |   | || | \   | \ \_/ / | (      | (\ (      | |   | (      | (\ (         ) |   | |   | |   | |
| (____/\| (___) || )  \  |  \   /  | (____/\| ) \ \__   | |   | (____/\| ) \ \__/\____) |___) (___| )   ( |
(_______/(_______)|/    )_)   \_/   (_______/|/   \__/   )_(   (_______/|/   \__/\_______)\_______/|/     \|
                                                                                                            
                                                          
                
=====================================================================================                                                                               
                                == By PyQonsole ==

=====================================================================================

* Description:
______________

    ** PyQonveter program allows you to change file format

        * [ how to use ] > Select one of integrated converters :

        1) video converter : [ mp4 > mkv | wmv to flv ] ...

        2) picture converter : [ jpg to png | svg to ico ] ...
                                                                                                                                                         
        >> ''')
        if select == '1':
            ConverterSim.video_convert()
        elif select == '2':
            ConverterSim.picture_convert()
        else:
            print('     * Try Again !!!')

if __name__ == '__main__':
    pass