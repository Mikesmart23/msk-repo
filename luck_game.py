import random
import termcolor

class LuckGame:
    def __init__(self):
        pass

    def GuessTheNumber(self):
        print(' ** Guess The Number Mini Game **\n ** Enter A Number Between (0-10) Below : ')
        fails = 0
        while fails < 3:
            random_number = random.randint(0, 10)
            numberSelected = int(input(' ** -> '))
            if numberSelected == random_number:
                print(f'Selected Number : {numberSelected} - Random Number : {random_number}')
                termcolor.cprint('Right Guess !!', 'light_green')
                fails = 0

            elif numberSelected != random_number:
                print(f'Selected Number : {numberSelected} - Random Number : {random_number}')
                termcolor.cprint('No, Guess Again !!', 'light_red')
                fails += 1
        termcolor.cprint('Game Over ...', 'red')
        
LuckGame().GuessTheNumber()
