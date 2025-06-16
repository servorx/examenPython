from modules.controllers.screenControllers import *
from modules.menus import * 
from modules.utils.input_data import *

def validate_menu_tipo():
  clean_screen()
  print(MENU_VER)
  try:
    value_menu = int(input("-> "))
  except ValueError:
    print("ingreso un dato invalido")
    pause_screen()
    return

def results():
  value_menu = validate_menu_tipo()
  match value_menu:
    case 1:
      return input_data()
    case 2:
      return 