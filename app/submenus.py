import os
import utils.screenControllers as sc
import utils.validateData as vd
import config as cfg
import app.submenus as sm




def anadir_menu():
    opcionesMenu = ["Libro","Pelicula","Musica","Regresar al menú principal"]
    while True: 
        sc.limpiar_pantalla()
        print("==============================================")
        print("         Añadir un Nuevo Elemento             ")
        print("==============================================")
        print("¿Qué tipo de elemento deseas añadir?")
        for i, opcion in enumerate(opcionesMenu, start=1):
            print(f"{i}. {opcion}")
        op = vd.validateInt("Selecciona una opción (1-4): ") - 1
        
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
                print("Saliendo del programa...")
                input("Presione Enter para continuar...")
                return 
            case _:
                print("Opción no implementada aún.")
                input("Presione Enter para continuar...")
        
def ver_menu():
    opcionesMenu = ["Ver Todos los Libros","Ver Todas las Películas","Ver Toda la Música","Regresar al menú principal"]
    while True: 
        sc.limpiar_pantalla()
        print("==============================================")
        print("         Ver Todos los Elementos            ")
        print("==============================================")
        print("¿Qué categoría deseas ver?")
        for i, opcion in enumerate(opcionesMenu, start=1):
            print(f"{i}. {opcion}")
        op = vd.validateInt("Selecciona una opción (1-4): ") - 1
        
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
                print("Saliendo del programa...")
                input("Presione Enter para continuar...")
                return 
            case _:
                print("Opción no implementada aún.")
                input("Presione Enter para continuar...")
        
def buscar_menu():
    opcionesMenu = ["Buscar por Título","Buscar por Autor/Director/Artista","Buscar por Género","Regresar al menú principal"]
    while True: 
        sc.limpiar_pantalla()
        print("==============================================")
        print("              Buscar un Elemento              ")
        print("==============================================")
        print("Cómo deseas buscar?")
        for i, opcion in enumerate(opcionesMenu, start=1):
            print(f"{i}. {opcion}")
        op = vd.validateInt("Selecciona una opción (1-4): ") - 1
        
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
                print("Saliendo del programa...")
                input("Presione Enter para continuar...")
                return 
            case _:
                print("Opción no implementada aún.")
                input("Presione Enter para continuar...")
        
def editar_menu():
    opcionesMenu = ["Editar Título","Editar Autor/Director/Artista","Editar Género","Editar Valoración","Regresar al menú principal"]
    while True: 
        sc.limpiar_pantalla()
        print("==============================================")
        print("              Editar un Elemento              ")
        print("==============================================")
        print("Qué tipo de cambio deseas realizar?")
        for i, opcion in enumerate(opcionesMenu, start=1):
            print(f"{i}. {opcion}")
        op = vd.validateInt("Selecciona una opción (1-5): ") - 1
        
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
                print("Saliendo del programa...")
                input("Presione Enter para continuar...")
                return 
            case _:
                print("Opción no implementada aún.")
                input("Presione Enter para continuar...")
        
def eliminar_menu():
    opcionesMenu = ["Eliminar por Título","Eliminar por Identificador Único","Regresar al menú principal"]
    while True: 
        sc.limpiar_pantalla()
        print("==============================================")
        print("            Eliminar un Elemento              ")
        print("==============================================")
        print("Cómo deseas eliminar?")
        for i, opcion in enumerate(opcionesMenu, start=1):
            print(f"{i}. {opcion}")
        op = vd.validateInt("Selecciona una opción (1-3): ") - 1
        
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
                print("Saliendo del programa...")
                input("Presione Enter para continuar...")
                return 
            case _:
                print("Opción no implementada aún.")
                input("Presione Enter para continuar...")
        
def filtrar_menu():
    opcionesMenu = ["Ver Libros","Ver Películas","Ver Música","Regresar al menú principal"]
    while True: 
        sc.limpiar_pantalla()
        print("==============================================")
        print("        Ver Elementos por Categoría           ")
        print("==============================================")
        print("Qué categoría deseas ver?")
        for i, opcion in enumerate(opcionesMenu, start=1):
            print(f"{i}. {opcion}")
        op = vd.validateInt("Selecciona una opción (1-4): ") - 1
        
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
                print("Saliendo del programa...")
                input("Presione Enter para continuar...")
                return 
            case _:
                print("Opción no implementada aún.")
                input("Presione Enter para continuar...")
        
def guardar_menu():
    opcionesMenu = ["Guardar la Colección Actual","Cargar una Colección Guardada","Regresar al menú principal"]
    while True: 
        sc.limpiar_pantalla()
        print("==============================================")
        print("        Guardar y Cargar Colección           ")
        print("==============================================")
        print("Qué deseas hacer?")
        for i, opcion in enumerate(opcionesMenu, start=1):
            print(f"{i}. {opcion}")
        op = vd.validateInt("Selecciona una opción (1-3): ") - 1
        
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
                print("Saliendo del programa...")
                input("Presione Enter para continuar...")
                return 
            case _:
                print("Opción no implementada aún.")
                input("Presione Enter para continuar...")
        
