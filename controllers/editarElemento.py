import utils.corefiles as cf
import utils.screenControllers as sc
import utils.validateData as vd
import config as cfg


def editarLibros():
    libros = cf.readJson(cfg.DB_LIBROS)

    if not libros:
        print("No hay libros.")
        return

    for cod, libro in libros.items():
        print(f"{cod}: {libro['nombre']}")

    id = input("Id del libro a editar: ")
    id = libros.get(id)

    if not libro:
        print("Código no válido.")
        return
    
    print("\n--- Datos actuales ---")
    libro = libros[id]

    for k, v in libro.items():
        print(f"{k.capitalize()}: {v}")

    titulo= input("Nuevo titulo (enter para mantener): " or libro["titulo"])
    autor= input("Nuevo autor (enter para mantener): " or libro["autor"])
    genero= input("Nuevo genero (enter para mantener): " or libro["genero"])
    valoracion= input("Nuevo valoracion (enter para mantener): " or libro["valoracion"])

    nuevo_libro = {
        "titulo": titulo,
        "autor": autor,
        "genero": genero,
        "valoracion": valoracion
    }
    libros[libro]= nuevo_libro
    cf.writeJson(cfg.DB_LIBROS, libros)
    print("Libro actualizado correctamente.")

def editarMusica():
    musica = cf.readJson(cfg.DB_MUSICA)

    if not musica:
        print("No hay canciones.")
        return

    for cod, music in musica.items():
        print(f"{cod}: {music['titulo']}")

    id = input("Id del libro a editar: ")
    id = musica.get(id)

    if not music:
        print("Código no válido.")
        return
    
    print("\n--- Datos actuales ---")
    music = musica[id]

    for k, v in music.items():
        print(f"{k.capitalize()}: {v}")

    titulo= input("Nuevo titulo (enter para mantener): " or music["titulo"])
    artista= input("Nuevo artista (enter para mantener): " or music["artista"])
    genero= input("Nuevo genero (enter para mantener): " or music["genero"])
    valoracion= input("Nuevo valoracion (enter para mantener): " or music["valoracion"])

    nuevo_music = {
        "titulo": titulo,
        "artista": artista,
        "genero": genero,
        "valoracion": valoracion
    }
    musica[music]= nuevo_music
    cf.writeJson(cfg.DB_MUSICA, musica)
    print("Cancion actualizado correctamente.")

def editarPeliculas():
    peliculas = cf.readJson(cfg.DB_PELICULAS)

    if not peliculas:
        print("No hay peliculas.")
        return

    for cod, pelicula in peliculas.items():
        print(f"{cod}: {pelicula['nombre']}")

    id = input("Id del peliculas a editar: ")
    id = pelicula.get(id)

    if not pelicula:
        print("Código no válido.")
        return
    
    print("\n--- Datos actuales ---")
    pelicula = peliculas[id]

    for k, v in pelicula.items():
        print(f"{k.capitalize()}: {v}")

    titulo= input("Nuevo titulo (enter para mantener): " or pelicula["titulo"])
    director= input("Nuevo director (enter para mantener): " or pelicula["director"])
    genero= input("Nuevo genero (enter para mantener): " or pelicula["genero"])
    valoracion= input("Nuevo valoracion (enter para mantener): " or pelicula["valoracion"])

    nueva_pelicula = {
        "titulo": titulo,
        "director": director,
        "genero": genero,
        "valoracion": valoracion
    }
    peliculas[pelicula]= nueva_pelicula
    cf.writeJson(cfg.DB_PELICULAS, peliculas)
    print("Pelicula actualizada correctamente.")