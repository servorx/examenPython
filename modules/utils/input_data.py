from modules.controllers.screenControllers import *
from modules.menus import * 

def validate_menu_calculo():
  clean_screen()
  print(MENU_IMPUESTO_CALCULO)
  try:
    valor_base = int(input("-> "))
  except ValueError:
    print("ingreso un dato invalido")
    pause_screen()
    return

def validate_menu_tipo():
  clean_screen()
  print(MENU_IMPUESTO_TIPO)
  try:
    value_menu = int(input("-> "))
  except ValueError:
    print("ingreso un dato invalido")
    pause_screen()
    return
  
def validate_menu_continuar():
  clean_screen()
  print(MENU_IMPUESTO_CONTINUAR)
  try:
    value_menu_continue = int(input("-> "))
  except ValueError:
    print("ingreso un dato invalido")
    pause_screen()
    return

def input_data():
  valor_base = validate_menu_calculo()
  value_menu = validate_menu_tipo()
  match value_menu:
    case 1:
      iva = (valor_base/10)
      pause_screen()
    case 2:
      impuesto_especial = ((valor_base*5)/100)
      pause_screen()
    case 3:
      impuesto_local = ((valor_base*8)/100)
      pause_screen()
    case 4:
      pause_screen()
      try:
        impuesto_otro_input = int(input(MENU_IMPUESTO_TIPO_OTRO, "\n-> "))
      except ValueError:
        print("valor invalido")
        pause_screen()
        return
      else:
        impuesto_otro = ((valor_base*impuesto_otro_input)/100)
        pause_screen()
  value_menu_continue = validate_menu_continuar()
  match value_menu_continue:
    case 1:
      return input_data()
    case 2:
      total = iva + impuesto_especial + impuesto_local + impuesto_otro
      print(MENU_RESULTADO)
      pause_screen()

