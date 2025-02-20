import modules.utils.screenControllers as sc
import modules.menus as menu
def datosIngresar():
    sc.limpiar_pantalla()
    print(menu.MENU_IMPUESTO_CALCULO)
    precioBase = int(input("->"))
    #hacer tyrs a todos estos inputs
    print(menu.MENU_IMPUESTO_TIPO)
    tipoImpuesto = int(input("->"))
    match tipoImpuesto:
        case 1:
            iva= (precioBase/10)
            sc.pausar_pantalla()
        case 2:
            ImpuestoEspecial = ((precioBase*5)/100)
            sc.pausar_pantalla()
        case 3:
            valorImpuestoLocal = ((precioBase*8)/100)
        case 4:
            sc.pausar_pantalla()
            impuestoOtro = (menu.MENU_IMPUESTO_TIPO_OTRO, "->")
    #total = iva + ImpuestoEspecial + valorImpuestoLocal + impuestoOtro
    #print(total)
    sc.limpiar_pantalla()
    print(menu.MENU_IMPUESTO_CONTINUAR)
    continuar = int(input("->"))
    match continuar:
        case 1:
            return datosIngresar()
        case 2:
            sc.pausar_pantalla()

