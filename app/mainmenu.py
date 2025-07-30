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
                sm.anadir_menu()
            case 1:
                sm.ver_menu()
            case 2:
                sm.buscar_menu()
            case 3:
                sm.editar_menu()
            case 4:
                sm.eliminar_menu()
            case 5:
                sm.filtrar_menu()
            case 6:
                sm.guardar_menu()
            case 7:
                print("Saliendo del programa...")
                input("Presione Enter para continuar...")
                return 
            case _:
                print("Opción no implementada aún.")
                input("Presione Enter para continuar...")
        