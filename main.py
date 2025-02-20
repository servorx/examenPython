import os
import modules.menus as menu
import modules.utils.screenControllers as sc
import modules.utils.corefiles as cf
import modules.controllers.impuesto.datosIngresar as di
#import modules.controllers.impuesto.Datosingresar as
import modules.controllers.salir as salir
import modules.controllers.resultado as resultado
import modules.utils.corefiles as cf

if __name__ == "__main__":
    sc.limpiar_pantalla()
    print(menu.MENU_PRINCIPAL)
    #hacer try en estos input
    opcion = int(input("->"))
    match opcion:
        case 1:
            di.datosIngresar()
        case 2:
            resultado.resultado()
        case 3:
            salir.salir()





