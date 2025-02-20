from os import system
import sys 

def limpiar_pantalla():
    if sys.platform == "linux":
        system('clear')
    else:
        system('cls')

def pausar_pantalla():
    if sys.platform == "linux":
        x = input("presione una tecla para continuar...")
        return x
    else:
        system('pause')
