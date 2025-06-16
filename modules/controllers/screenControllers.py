from os import system
import sys 

def clean_screen():
    if sys.platform == "linux":
        system('clear')
    else:
        system('cls')

def pause_screen():
    if sys.platform == "linux":
        x = input("presione una tecla para continuar...")
        return x
    else:
        system('pause')
