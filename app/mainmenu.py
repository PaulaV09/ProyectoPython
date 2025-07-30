import os
import utils.screenControllers as sc
import utils.validateData as vd
import config as cfg
import app.submenus as sm

opcionesMenu = ['Añadir un nuevo elemento', 'Ver todos los elementos', 'Buscar elemento en la colección', 'Editar elemento en la colección', 'Eliminar elemento de la colección', 'Ver elementos por catagoría', 'Guardar y cargar colección', 'Salir']

def main_menu():
    while True: 
        sc.limpiar_pantalla()
        print("==============================================")
        print("         ADMINISTRADOR DE COLECCIONES         ")
        print("==============================================")
        print("-> Bienvenido al Menú Principal del sistema <-")
        for i, opcion in enumerate(opcionesMenu, start=1):
            print(f"{i}. {opcion}")
        op = vd.validateInt("Seleccione una opción: ") - 1
        
        if op < 0 or op >= len(opcionesMenu): 
            print("Opción no válida. Intente de nuevo.")
            input("Presione Enter para continuar...")
            continue 
        
        match op:
            case 0:
                pass
            case 1:
                pass
            case 2:
                pass
            case 3:
                pass
            case 4:
                pass
            case 5:
                pass
            case 6:
                pass
            case 7:
                print("Saliendo del programa...")
                input("Presione Enter para continuar...")
                return 
            case _:
                print("Opción no implementada aún.")
                input("Presione Enter para continuar...")
        