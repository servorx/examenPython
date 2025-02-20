import modules.utils.screenControllers as sc
import modules.menus as menu

def salir():
    sc.limpiar_pantalla()
    print(menu.MENU_SALIR)
    sc.pausar_pantalla()