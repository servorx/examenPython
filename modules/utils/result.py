from modules.controllers.screenControllers import *
from modules.menus import * 
from modules.utils.input_data import *

def validate_menu_tipo():
  clean_screen()
  print(MENU_VER)
  try:
    value_menu = int(input("-> "))
    return value_menu
  except ValueError:
    print("ingresó un dato inválido")
    pause_screen()
    return results()

def results():
  value_menu = validate_menu_tipo()
  match value_menu:
    case 1:
      print("Opción 1 seleccionada")
      pause_screen()  
      return input_data()
    case 2:
      print("Opción 2 seleccionada")
      pause_screen()
      return
    case _:
      print("valor no encontrado")
      pause_screen()
      return results()
