import os
from time import sleep
# 
class PyConverter:
    def __init__(self):
        pass

    def picture_convert(
        filePath = 'C:\\Users\\lenovo\\Pictures\\Screenshots',
        icon = '.ico'):

        os.chdir(filePath)
        files = os.listdir()
        for index, file in enumerate(files):
            extension = file.split()[-1]
            os.rename(file, f'{index}{icon}')
            print('done')

    def video_convert():
        print('\n        * Wait A Second ... ')
        sleep(1.0)
        print('\n** [ PyConverter ] Video Converter **')
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
            
    def convert():
        select = input(
'''
=====================================================================================

 ___                   ___                                      _                
(  _`\                (  _`\                                   ( )_              
| |_) ) _   _  ______ | ( (_)   _     ___   _   _    __   _ __ | ,_)   __   _ __ 
| ,__/'( ) ( )(______)| |  _  /'_`\ /' _ `\( ) ( ) /'__`\( '__)| |   /'__`\( '__)
| |    | (_) |        | (_( )( (_) )| ( ) || \_/ |(  ___/| |   | |_ (  ___/| |   
(_)    `\__, |        (____/'`\___/'(_) (_)`\___/'`\____)(_)   `\__)`\____)(_)   
       ( )_| |                                                                   
       `\___/'                                                                   
                
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
            PyConverter.video_convert()
        elif select == '2':
            PyConverter.picture_convert()
        else:
            print('     * Try Again !!!')
            


PyConverter.convert()