import os
import utils.screenControllers as sc
import utils.validateData as vd
import config as cfg
import app.submenus as sm

opcionesMenu = ['Añadir elemento a la colección', 'Listar elementos de la colección', 'Buscar elemento en la colección', 'Editar elemento en la colección', 'Eliminar elemento de la colección', 'Salir']

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
                sm.subMenuGestionLiga()
            case 1:
                sm.subMenuGestionEquipo()
            case 2:
                sm.subMenuGestionJugador()
            case 3:
                sm.subMenuGestionCuerpoTecMed()
            case 4:
                sm.subMenuGestionTorneo()
            case 5:
                print("Saliendo del programa...")
                input("Presione Enter para continuar...")
                return 
            case _:
                print("Opción no implementada aún.")
                input("Presione Enter para continuar...")
        