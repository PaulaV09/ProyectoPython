import os
from tabulate import tabulate 
import utils.corefiles as cf
import utils.screenControllers as sc
import utils.validateData as vd
import config as cfg

generos_libros = [
  "Ficción",
  "No ficción",
  "Novela histórica",
  "Ciencia ficción",
  "Fantasía",
  "Romance",
  "Terror",
  "Misterio",
  "Suspenso",
  "Biografía",
  "Autobiografía",
  "Poesía",
  "Drama",
  "Aventura",
  "Literatura juvenil",
  "Autoayuda",
  "Ensayo",
  "Crónica",
  "Cuento",
  "Religión y espiritualidad"
]
generos_musica = [
  "Pop",
  "Rock",
  "Reguetón",
  "Rap",
  "Hip Hop",
  "Electrónica",
  "Techno",
  "House",
  "Clásica",
  "Jazz",
  "Blues",
  "R&B",
  "Salsa",
  "Bachata",
  "Merengue",
  "Cumbia",
  "Folk",
  "Country",
  "Metal",
  "Trap"
]
generos_peliculas = [
  "Acción",
  "Comedia",
  "Drama",
  "Terror",
  "Ciencia ficción",
  "Fantasía",
  "Suspenso",
  "Romance",
  "Aventura",
  "Animación",
  "Documental",
  "Musical",
  "Crimen",
  "Misterio",
  "Histórica",
  "Bélica",
  "Western",
  "Cine negro",
  "Familiar",
  "Biográfica"
]

def buscarElementoTitulo():
    sc.limpiar_pantalla()
    libros_data = cf.readJson(cfg.DB_LIBROS)
    peliculas_data = cf.readJson(cfg.DB_PELICULAS)
    musica_data = cf.readJson(cfg.DB_MUSICA)

    if not (libros_data) and not (peliculas_data) and not (musica_data):
        print("No hay elementos en la colección.")
        sc.pausar_pantalla()
        return

    titulo_buscar = vd.validate_string("Ingrese el título del elemento a buscar: ").title().strip()
    if not (titulo_buscar):
        print("ERROR: El título no puede estar vacío.")
        sc.pausar_pantalla()
        return
    
    encontrado = None 
    tipo_elemento = ""

    for libro in libros_data.get("libros", {}).values():
        if (libro.get("titulo", "").lower() == titulo_buscar.lower()):
            encontrado = libro
            tipo_elemento = "Libro"
            break 
            
    if not (encontrado):
        for pelicula in peliculas_data.get("peliculas", {}).values():
            if (pelicula.get("titulo", "").lower() == titulo_buscar.lower()):
                encontrado = pelicula
                tipo_elemento = "Película"
                break

    if not (encontrado):
        for cancion in musica_data.get("canciones", {}).values():
            if (cancion.get("titulo", "").lower() == titulo_buscar.lower()):
                encontrado = cancion
                tipo_elemento = "Canción"
                break

    if (encontrado):
        print(f"\n{tipo_elemento} encontrado:")
        headers = ["ID", "Título", "Autor/Director/Artista", "Género", "Valoración"]

        autor_director_artista = (encontrado.get("autor") or encontrado.get("director") or encontrado.get("artista"))

        datos = [
            [
                encontrado.get('id'), 
                encontrado.get('titulo'), 
                autor_director_artista, 
                encontrado.get('genero'), 
                f"{encontrado.get('valoracion', 0)} estrellas"
            ]
        ]        
        print(tabulate(datos, headers=headers, tablefmt="fancy_grid"))
    else:
        print(f"\nNo se encontró ningún elemento con el título '{titulo_buscar}'.")
        
    sc.pausar_pantalla()
    return

def buscarElementoAutor():
    sc.limpiar_pantalla()
    libros_data = cf.readJson(cfg.DB_LIBROS)
    peliculas_data = cf.readJson(cfg.DB_PELICULAS)
    musica_data = cf.readJson(cfg.DB_MUSICA)

    if not (libros_data) and not (peliculas_data) and not (musica_data):
        print("No hay elementos en la colección.")
        sc.pausar_pantalla()
        return
    
    nombre_buscar = vd.validate_string("Ingrese el nombre del autor/director/artista del elemento a buscar: ").title().strip()
    if not (nombre_buscar):
        print("ERROR: El título no puede estar vacío.")
        sc.pausar_pantalla()
        return
    
    encontrado = []
    for libro in libros_data.get("libros", {}).values():
        if (libro.get("autor", "").lower() == nombre_buscar.lower()):
            libro["tipo"] = "Libro" 
            encontrado.append(libro)
            
    for pelicula in peliculas_data.get("peliculas", {}).values():
        if (pelicula.get("director", "").lower() == nombre_buscar.lower()):
            pelicula["tipo"] = "Película"
            encontrado.append(pelicula)
    
    for cancion in musica_data.get("canciones", {}).values():
        if (cancion.get("artista", "").lower() == nombre_buscar.lower()):
            cancion["tipo"] = "Canción"
            encontrado.append(cancion)
    
    if (encontrado):
        print(f"\nElementos encontrados para '{nombre_buscar}':")
        headers = ["Tipo", "ID", "Título", "Género", "Valoración"]

        datos_tabla = []
        for elem in encontrado:
            fila = [
                elem["tipo"],
                elem["id"],
                elem["titulo"],
                elem["genero"],
                f"{elem['valoracion']} estrellas"
            ]
            datos_tabla.append(fila)
        
        print(tabulate(datos_tabla, headers=headers, tablefmt="fancy_grid"))
    else:
        print(f"No se encontró ningún elemento con el autor/director/artista '{nombre_buscar}'.")

    sc.pausar_pantalla()
    return

def buscarElementoGenero():
    sc.limpiar_pantalla()
    libros_data = cf.readJson(cfg.DB_LIBROS)
    peliculas_data = cf.readJson(cfg.DB_PELICULAS)
    musica_data = cf.readJson(cfg.DB_MUSICA)
    if not (libros_data) and not (peliculas_data) and not (musica_data):
        print("No hay elementos en la colección.")
        sc.pausar_pantalla()
        return
    
    opGenero = vd.validateInt("Seleccione  la categoría del género a buscar:\n1. Libros\n2. Películas\n3. Música\n4. Regresar al menú principal\nOpción: ")
    if not (opGenero):
        print("ERROR: El género no puede estar vacío.")
        sc.pausar_pantalla()
        return
    if (opGenero < 1) or (opGenero > 4):
        print("ERROR: Opción no válida.")
        sc.pausar_pantalla()
        return
    
    encontrado = []
    genero_buscar = ""
    tipo_busqueda = ""
    headers = []

    if (opGenero == 1):
        sc.limpiar_pantalla()
        print("-> Lista de géneros disponibles: ")
        for i, genero in enumerate(generos_libros, start= 1):
            print(f"{i}. {genero}")
        genero_opcion = vd.validateInt(f"Seleccione el género de libro (1-{len(generos_libros)}): ")
        if (genero_opcion > 0) or (genero_opcion <= len(generos_libros)):
            genero_buscar = generos_libros[genero_opcion - 1]
            tipo_busqueda = "Libro"
            headers = ["ID", "Título", "Autor", "Género", "Valoración"]
            for libro in libros_data.get("libros", {}).values():
                if (libro.get("genero", "").lower() == genero_buscar.lower()):
                    encontrado.append(libro)
        else:
            print("ERROR: Opción no válida.")
            sc.pausar_pantalla()
            return
            
    elif (opGenero == 2):
        sc.limpiar_pantalla()
        print("-> Lista de géneros disponibles: ")
        for i, genero in enumerate(generos_peliculas, start= 1):
            print(f"{i}. {genero}")
        genero_opcion = vd.validateInt(f"Seleccione el género de película (1-{len(generos_peliculas)}): ")
        if (genero_opcion > 0) or (genero_opcion <= len(generos_peliculas)):
            genero_buscar = generos_peliculas[genero_opcion - 1]
            tipo_busqueda = "Película"
            headers = ["ID", "Título", "Director", "Género", "Valoración"]
            for pelicula in peliculas_data.get("peliculas", {}).values():
                if (pelicula.get("genero", "").lower() == genero_buscar.lower()):
                    encontrado.append(pelicula)
        else:
            print("ERROR: Opción no válida.")
            sc.pausar_pantalla()
            return
            
    elif (opGenero == 3):
        sc.limpiar_pantalla()
        print("-> Lista de géneros disponibles: ")
        for i, genero in enumerate(generos_musica, start= 1):
            print(f"{i}. {genero}")
        genero_opcion = vd.validateInt(f"Seleccione el género de música (1-{len(generos_musica)}): ")
        if (genero_opcion > 0) or (genero_opcion <= len(generos_musica)):
            genero_buscar = generos_musica[genero_opcion - 1]
            tipo_busqueda = "Canción"
            headers = ["ID", "Título", "Artista", "Género", "Valoración"]
            for cancion in musica_data.get("canciones", {}).values(): 
                if (cancion.get("genero", "").lower() == genero_buscar.lower()):
                    encontrado.append(cancion)
        else:
            print("ERROR: Opción no válida.")
            sc.pausar_pantalla()
            return
    elif (opGenero == 4):
        return
        
    if (encontrado):
        sc.limpiar_pantalla()
        print(f"\nResultados encontrados para el género '{genero_buscar}':")
        datos_tabla = []
        for elem in encontrado:
            fila = [
                elem.get("id"), 
                elem.get("titulo"), 
                elem.get("autor") or elem.get("director") or elem.get("artista"),
                elem.get("genero"), 
                f"{elem.get('valoracion', 0)} estrellas"
            ]
            datos_tabla.append(fila)
        print(tabulate(datos_tabla, headers=headers, tablefmt="fancy_grid"))
    elif (opGenero in [1, 2, 3]): 
        print(f"No se encontró ningún {tipo_busqueda.lower()} con el género '{genero_buscar}'.")
        
    sc.pausar_pantalla()
    return