from modules.controllers.screenControllers import *
from modules.menus import * 

def validate_menu_calculo():
  clean_screen()
  print(MENU_IMPUESTO_CALCULO)
  try:
    valor_base = int(input("-> "))
    return valor_base
  except ValueError:
    print("ingreso un dato invalido")
    pause_screen()
    return

def validate_menu_tipo():
  clean_screen()
  print(MENU_IMPUESTO_TIPO)
  try:
    value_menu = int(input("-> "))
    return value_menu
  except ValueError:
    print("ingreso un dato invalido")
    pause_screen()
    return
  
def validate_menu_continuar():
  clean_screen()
  print(MENU_IMPUESTO_CONTINUAR)
  try:
    value_menu_continue = int(input("-> "))
    return value_menu_continue
  except ValueError:
    print("ingreso un dato invalido")
    pause_screen()
    return

def input_data():
  # definir estas valores con 0 al principio en caso de que no se vayan a usar o calcular
  iva = 0
  impuesto_especial = 0
  impuesto_local = 0
  impuesto_otro = 0

  # validar ingreso correcto para valor_base
  valor_base = None
  while valor_base is None:
    valor_base = validate_menu_calculo()
  # lo mismo con el impuesto, se hace en bucle para tener mejor estructura del programa
  value_menu = None
  while value_menu is None:
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
        impuesto_otro_input = int(input(f"{MENU_IMPUESTO_TIPO_OTRO}\n-> "))
        impuesto_otro = (valor_base * impuesto_otro_input) / 100
      except ValueError:
        print("valor inválido")
        pause_screen()
        return input_data()
      pause_screen()
    case _:
      print("valor no encontrado")
      pause_screen()
      return input_data()
  # validacion para continuar o mostrar los resultados con un bucle
  value_menu_continue = None
  while value_menu_continue is None:
    value_menu_continue = validate_menu_continuar()

  match value_menu_continue:
    case 1:
      return input_data()
    case 2:
      total = iva + impuesto_especial + impuesto_local + impuesto_otro + valor_base
      print(f"""---------------------------------------------------
                RESULTADO DEL CÁLCULO
---------------------------------------------------
Precio Base: ${valor_base}
Impuesto(s):
- IVA (10%): ${iva}
- Impuesto Especial (5%): ${impuesto_especial}
- Impuesto Local (8%): ${impuesto_local}
- Otro: ${impuesto_otro}
Total con impuestos: ${total}

¿Desea hacer otro cálculo?
1. Sí
2. No (Regresa al menú principal)
---------------------------------------------------""")
      try:
        value_menu_again = int(input("-> "))
      except ValueError:
        print("ingreso un dato invalido")
        pause_screen()
        return
      else:
        match value_menu_again:
          case 1:
            return input_data()
          case 2:
            return 
          case _:
            print("Opción no válida")
            pause_screen()
            return input_data()

