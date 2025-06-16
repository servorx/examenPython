from modules.menus import *
from modules.controllers.screenControllers import *
from modules.utils.input_data import *
from modules.utils.result import *

def main():
  while True:
    clean_screen()
    print(MENU_PRINCIPAL)
    try:
      opcion = int(input("-> "))
    except ValueError:
      print("dato no valido")
      pause_screen
      return
    else:
      match opcion:
        case 1:
          input_data()
        case 2:
          results()
        case 3:
          print(MENU_SALIR)
          break
        case _:
          print("valor no encontrado")
          return main