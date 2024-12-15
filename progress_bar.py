from time import sleep


def progress_bar():
    print('Wait A While >> ', end=' ')
    bar = ''
    start = 0
    while start < 5:
        bar += '🟢'
        sleep(0.5)
        start += 1
        print(bar, end='')
    input('\n\npress enter to continue !! '.title())
    
        
        
if __name__ == '__main__':
    
    progress_bar()