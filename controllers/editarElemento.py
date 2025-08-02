import utils.corefiles as cf
import utils.screenControllers as sc
import utils.validateData as vd
import config as cfg
import controllers.buscarElemento as be


def editarLibros():
    sc.limpiar_pantalla()
    print("\n--- Libros disponibles ---")
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
    sc.limpiar_pantalla()
    print("\n--- Datos actuales ---")
    for k, v in libro.items():
        print(f"{k.capitalize()}: {v}")

    titulo = input("Nuevo titulo (enter para mantener): ")
    autor = input("Nuevo autor (enter para mantener): ")

    print("\n--- Generos disponibles ---")
    
    for idx, genero in enumerate(be.generos_libros,start=1):
        print(f"{idx}. {genero}")

    genero_codigo = input("Nuevo código del genero (enter para mantener): ")
    
    genero = libro["genero"] 
    if genero_codigo.strip() != "":
        if genero_codigo.isdigit():
            genero_idx = int(genero_codigo)
            if 1 <= genero_idx <= len(be.generos_libros):
                genero = be.generos_libros[genero_idx - 1]
            else:
                print("Índice fuera de rango. Se mantiene el género actual.")
        else:
            print("Código inválido. Se mantiene el género actual.")

    valoracion = vd.validateValoracion("Nueva valoración (enter para mantener): ")

    
    libro["titulo"] = titulo or libro["titulo"]
    libro["autor"] = autor or libro["autor"]
    libro["genero"] = genero or libro["genero"]
    libro["valoracion"] = float(valoracion) if valoracion else libro["valoracion"]

    libros[id] = libro
    data["libros"] = libros
    cf.writeJson(cfg.DB_LIBROS, data)
    print("Libro actualizado correctamente.")
    sc.pausar_pantalla()


def editarMusica():
    sc.limpiar_pantalla()
    print("\n--- Canciones disponibles ---")
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
    sc.limpiar_pantalla()
    print("\n--- Datos actuales ---")
    for k, v in song.items():
        print(f"{k.capitalize()}: {v}")

    titulo = input("Nuevo título (enter para mantener): ")
    artista = input("Nuevo artista (enter para mantener): ")


    print("\n--- Generos disponibles ---")
    
    for idx, genero in enumerate(be.generos_musica,start=1):
        print(f"{idx}. {genero}")

    genero_codigo = input("Nuevo código del genero (enter para mantener): ")
    
    genero = song["genero"] 
    if genero_codigo.strip() != "":
        if genero_codigo.isdigit():
            genero_idx = int(genero_codigo)
            if 1 <= genero_idx <= len(be.generos_musica):
                genero = be.generos_musica[genero_idx - 1]
            else:
                print("Índice fuera de rango. Se mantiene el género actual.")
        else:
            print("Código inválido. Se mantiene el género actual.")

    
    valoracion = vd.validateValoracion("Nueva valoración (enter para mantener): ")

    song["titulo"] = titulo or song["titulo"]
    song["artista"] = artista or song["artista"]
    song["genero"] = genero or song["genero"]
    song["valoracion"] = float(valoracion) if valoracion else song["valoracion"]

    musica[id] = song
    data["canciones"] = musica
    cf.writeJson(cfg.DB_MUSICA, data)
    print("Canción actualizada correctamente.")
    sc.pausar_pantalla()


def editarPeliculas():
    sc.limpiar_pantalla()
    print("\n--- Películas disponibles ---")
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
    sc.limpiar_pantalla()
    print("\n--- Datos actuales ---")
    for k, v in peli.items():
        print(f"{k.capitalize()}: {v}")

    titulo = input("Nuevo título (enter para mantener): ")
    director = input("Nuevo director (enter para mantener): ")
    
    print("\n--- Generos disponibles ---")
    
    for idx, genero in enumerate(be.generos_peliculas,start=1):
        print(f"{idx}. {genero}")

    genero_codigo = input("Nuevo código del genero (enter para mantener): ")
    
    genero = peli["genero"] 
    if genero_codigo.strip() != "":
        if genero_codigo.isdigit():
            genero_idx = int(genero_codigo)
            if 1 <= genero_idx <= len(be.generos_peliculas):
                genero = be.generos_peliculas[genero_idx - 1]
            else:
                print("Índice fuera de rango. Se mantiene el género actual.")
        else:
            print("Código inválido. Se mantiene el género actual.")
    
    valoracion = vd.validateValoracion("Nueva valoración (enter para mantener): ")
    if valoracion < 1 or valoracion > 5:
        print("ERROR: La valoración debe estar entre 1 y 5.")
        sc.pausar_pantalla()
        return

    peli["titulo"] = titulo or peli["titulo"]
    peli["director"] = director or peli["director"]
    peli["genero"] = genero or peli["genero"]
    peli["valoracion"] = float(valoracion) if valoracion else peli["valoracion"]

    peliculas[id] = peli
    data["peliculas"] = peliculas
    cf.writeJson(cfg.DB_PELICULAS, data)
    print("Película actualizada correctamente.")
    sc.pausar_pantalla()
