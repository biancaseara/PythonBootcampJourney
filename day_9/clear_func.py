import os
import platform

def clear():
    # if os.name == 'nt':
    if platform.system() == 'Windows':
        os.system('cls')
        os.system('clear')
    else:
        os.system('clear')

clear()