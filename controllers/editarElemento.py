import utils.corefiles as cf
import utils.screenControllers as sc
import utils.validateData as vd
import config as cfg


def editarLibros():
    data = cf.readJson(cfg.DB_LIBROS)
    libros = data.get("libros", {})

    if not libros:
        print("No hay libros.")
        return

    for cod, libro in libros.items():
        print(f"{cod}: {libro['titulo']}")

    id = input("Id del libro a editar: ")

    if id not in libros:
        print("Código no válido.")
        return
    
    libro = libros[id]

    print("\n--- Datos actuales ---")
    for k, v in libro.items():
        print(f"{k.capitalize()}: {v}")

    titulo = input("Nuevo titulo (enter para mantener): ")
    autor = input("Nuevo autor (enter para mantener): ")
    genero = input("Nuevo genero (enter para mantener): ")
    valoracion = input("Nueva valoración (enter para mantener): ")

    
    libro["titulo"] = titulo or libro["titulo"]
    libro["autor"] = autor or libro["autor"]
    libro["genero"] = genero or libro["genero"]
    libro["valoracion"] = float(valoracion) if valoracion else libro["valoracion"]

    libros[id] = libro
    data["libros"] = libros
    cf.writeJson(cfg.DB_LIBROS, data)
    print("Libro actualizado correctamente.")


def editarMusica():
    data = cf.readJson(cfg.DB_MUSICA)
    musica = data.get("canciones", {})

    if not musica:
        print("No hay canciones.")
        return

    for cod, song in musica.items():
        print(f"{cod}: {song['titulo']}")

    id = input("ID de la canción a editar: ")

    if id not in musica:
        print("ID no válido.")
        return

    song = musica[id]

    print("\n--- Datos actuales ---")
    for k, v in song.items():
        print(f"{k.capitalize()}: {v}")

    titulo = input("Nuevo título (enter para mantener): ")
    autor = input("Nuevo autor (enter para mantener): ")
    genero = input("Nuevo género (enter para mantener): ")
    valoracion = input("Nueva valoración (enter para mantener): ")

    song["titulo"] = titulo or song["titulo"]
    song["autor"] = autor or song["autor"]
    song["genero"] = genero or song["genero"]
    song["valoracion"] = float(valoracion) if valoracion else song["valoracion"]

    musica[id] = song
    data["canciones"] = musica
    cf.writeJson(cfg.DB_MUSICA, data)
    print("Canción actualizada correctamente.")


def editarPeliculas():
    data = cf.readJson(cfg.DB_PELICULAS)
    peliculas = data.get("peliculas", {})

    if not peliculas:
        print("No hay películas.")
        return

    for cod, peli in peliculas.items():
        print(f"{cod}: {peli['titulo']}")

    id = input("ID de la película a editar: ")

    if id not in peliculas:
        print("ID no válido.")
        return

    peli = peliculas[id]

    print("\n--- Datos actuales ---")
    for k, v in peli.items():
        print(f"{k.capitalize()}: {v}")

    titulo = input("Nuevo título (enter para mantener): ")
    director = input("Nuevo director (enter para mantener): ")
    genero = input("Nuevo género (enter para mantener): ")
    valoracion = input("Nueva valoración (enter para mantener): ")

    peli["titulo"] = titulo or peli["titulo"]
    peli["director"] = director or peli["director"]
    peli["genero"] = genero or peli["genero"]
    peli["valoracion"] = float(valoracion) if valoracion else peli["valoracion"]

    peliculas[id] = peli
    data["peliculas"] = peliculas
    cf.writeJson(cfg.DB_PELICULAS, data)
    print("Película actualizada correctamente.")
