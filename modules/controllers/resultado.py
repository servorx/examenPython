import modules.utils.screenControllers as sc
import modules.menus as menu
from modules.controllers.impuesto import *

def resultado():
    sc.limpiar_pantalla()
    print(menu.MENU_RESULTADO)
    continuar = int(input("->"))
    match continuar:
        case 1:
            return  
        case 2:
            return 