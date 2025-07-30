import os
import utils.corefiles as cf
import utils.screenControllers as sc
import utils.validateData as vd
import config as cfg

def anadirElementoLibro():
    sc.limpiar_pantalla()
    libros_data = cf.readJson(cfg.DB_LIBROS)
    if not isinstance(libros_data, dict) or 'libros' not in libros_data:
        libros_data = {"libros": {}}

    print("-> Añadir un nuevo libro")
    titulo = vd.validate_string("Ingrese el título del libro: ").title()
    for libro in libros_data.get("libros", {}).values():
        if libro.get("titulo", "").lower() == titulo.lower():
            print(f"Error: El libro con el título '{titulo}' ya está registrado.")
            sc.pausar_pantalla()
            return
    if not titulo:
        print("ERROR: El título no puede estar vacío.")
        sc.pausar_pantalla()
        return
    autor = vd.validatetext("Ingrese el autor del libro: ")
    genero = vd.validatetext("Ingrese el género del libro: ")
    valoracion = vd.validateInt("Ingrese la valoración del libro (1-5): ")
    if valoracion < 1 or valoracion > 5:
        print("ERROR: La valoración debe estar entre 1 y 5.")
        sc.pausar_pantalla()
        return
    if not libros_data.get("libros"):
        id_libro = "1"
    else:
        max_id = max(int(k) for k in libros_data["libros"].keys())
        id_libro = str(max_id + 1)

    nuevo_libro = {
        "id": id_libro,
        "titulo": titulo,
        "autor": autor,
        "genero": genero,
        "valoracion": valoracion
    }
    
    libros_data["libros"][id_libro] = nuevo_libro
    cf.writeJson(cfg.DB_LIBROS, libros_data)

    print(f"\nLibro '{titulo}' registrado con éxito con el ID: {id_libro}")
    sc.pausar_pantalla()

def anadirElementoPelicula():
    sc.limpiar_pantalla()
    peliculas_data = cf.readJson(cfg.DB_PELICULAS)
    if not isinstance(peliculas_data, dict) or 'peliculas' not in peliculas_data:
        peliculas_data = {"peliculas": {}}

    print("-> Añadir una nueva película")
    titulo = vd.validate_string("Ingrese el título de la película: ").title()
    for pelicula in peliculas_data.get("peliculas", {}).values():
        if pelicula.get("titulo", "").lower() == titulo.lower():
            print(f"Error: La película con el título '{titulo}' ya está registrada.")
            sc.pausar_pantalla()
            return
    if not titulo:
        print("ERROR: El título no puede estar vacío.")
        sc.pausar_pantalla()
        return
    director = vd.validatetext("Ingrese el director de la película: ")
    genero = vd.validatetext("Ingrese el género de la película: ")
    valoracion = vd.validateInt("Ingrese la valoración de la película (1-5): ")
    if valoracion < 1 or valoracion > 5:
        print("ERROR: La valoración debe estar entre 1 y 5.")
        sc.pausar_pantalla()
        return
    if not peliculas_data.get("peliculas"):
        id_pelicula = "1"
    else:
        max_id = max(int(k) for k in peliculas_data["peliculas"].keys())
        id_pelicula = str(max_id + 1)

    nueva_pelicula = {
        "id": id_pelicula,
        "titulo": titulo,
        "director": director,
        "genero": genero,
        "valoracion": valoracion
    }
    
    peliculas_data["peliculas"][id_pelicula] = nueva_pelicula
    cf.writeJson(cfg.DB_PELICULAS, peliculas_data)

    print(f"\Película '{titulo}' registrada con éxito con el ID: {id_pelicula}")
    sc.pausar_pantalla()

def anadirElementoMusica():
    sc.limpiar_pantalla()
    musica_data = cf.readJson(cfg.DB_MUSICA)
    if not isinstance(musica_data, dict) or 'canciones' not in musica_data:
        musica_data = {"canciones": {}}

    print("-> Añadir una nueva canción")
    titulo = vd.validate_string("Ingrese el título de la canción: ").title()
    for cancion in musica_data.get("canciones", {}).values():
        if cancion.get("titulo", "").lower() == titulo.lower():
            print(f"Error: La canción con el título '{titulo}' ya está registrada.")
            sc.pausar_pantalla()
            return
    if not titulo:
        print("ERROR: El título no puede estar vacío.")
        sc.pausar_pantalla()
        return
    artista = vd.validatetext("Ingrese el artísta de la canción: ")
    genero = vd.validatetext("Ingrese el género de la canción: ")
    valoracion = vd.validateInt("Ingrese la valoración de la canción (1-5): ")
    if valoracion < 1 or valoracion > 5:
        print("ERROR: La valoración debe estar entre 1 y 5.")
        sc.pausar_pantalla()
        return
    if not musica_data.get("canciones"):
        id_cancion = "1"
    else:
        max_id = max(int(k) for k in musica_data["canciones"].keys())
        id_cancion = str(max_id + 1)

    nueva_cancion = {
        "id": id_cancion,
        "titulo": titulo,
        "artista": artista,
        "genero": genero,
        "valoracion": valoracion
    }
    
    musica_data["canciones"][id_cancion] = nueva_cancion
    cf.writeJson(cfg.DB_MUSICA, musica_data)

    print(f"\Canción '{titulo}' registrada con éxito con el ID: {id_cancion}")
    sc.pausar_pantalla()