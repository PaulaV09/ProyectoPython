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

    if not libros_data and not peliculas_data and not musica_data:
        print("No hay elementos en la colección.")
        sc.pausar_pantalla()
        return
    
    titulo_buscar = vd.validate_string("Ingrese el título del elemento a buscar: ").title().strip()
    if not titulo_buscar:
        print("ERROR: El título no puede estar vacío.")
        sc.pausar_pantalla()
        return
    
    for libro in libros_data.get("libros", {}).values():
        if libro.get("titulo", "").lower() == titulo_buscar.lower():
            msg = f"Libro encontrado: {libro['titulo']} (ID: {libro['id']})\nAutor: {libro['autor']}\n Género: {libro['genero']}\n Valoración: {libro['valoracion']} estrellas"
            sc.pausar_pantalla()
            return
        
    for pelicula in peliculas_data.get("peliculas", {}).values():
        if pelicula.get("titulo", "").lower() == titulo_buscar.lower():
            msg = f"Pelicula encontrada: {pelicula['titulo']} (ID: {pelicula['id']})\nDirector: {pelicula['director']}\n Género: {pelicula['genero']}\n Valoración: {pelicula['valoracion']} estrellas"
            sc.pausar_pantalla()
            return
    
    for cancion in musica_data.get("canciones", {}).values():
        if cancion.get("titulo", "").lower() == titulo_buscar.lower():
            msg = f"Canción encontrada: {cancion['titulo']} (ID: {cancion['id']})\nArtísta: {cancion['artista']}\n Género: {cancion['genero']}\n Valoración: {cancion['valoracion']} estrellas"
            sc.pausar_pantalla()
            return
    
    if msg:
        print(msg)
    else:
        print(f"No se encontró ningún elemento con el título '{titulo_buscar}'.")
    sc.pausar_pantalla()
    return

def buscarElementoAutor():
    sc.limpiar_pantalla()
    libros_data = cf.readJson(cfg.DB_LIBROS)
    peliculas_data = cf.readJson(cfg.DB_PELICULAS)
    musica_data = cf.readJson(cfg.DB_MUSICA)

    if not libros_data and not peliculas_data and not musica_data:
        print("No hay elementos en la colección.")
        sc.pausar_pantalla()
        return
    
    nombre_buscar = vd.validate_string("Ingrese el nombre del autor/director/artista del elemento a buscar: ").title().strip()
    if not nombre_buscar:
        print("ERROR: El título no puede estar vacío.")
        sc.pausar_pantalla()
        return
    
    encontrado = []
    for libro in libros_data.get("libros", {}).values():
        if libro.get("autor", "").lower() == nombre_buscar.lower():
            encontrado.append(libro)
        
    for pelicula in peliculas_data.get("peliculas", {}).values():
        if pelicula.get("director", "").lower() == nombre_buscar.lower():
            encontrado.append(pelicula)
    
    for cancion in musica_data.get("canciones", {}).values():
        if cancion.get("artista", "").lower() == nombre_buscar.lower():
            encontrado.append(cancion)
    
    if encontrado:
        for elem in encontrado:
            if 'autor' in elem:
                msg = f"Libro encontrado: {elem['titulo']} (ID: {elem['id']})\nAutor: {elem['autor']}\n Género: {elem['genero']}\n Valoración: {elem['valoracion']} estrellas"
            elif 'director' in elem:
                msg = f"Pelicula encontrada: {elem['titulo']} (ID: {elem['id']})\nDirector: {elem['director']}\n Género: {elem['genero']}\n Valoración: {elem['valoracion']} estrellas"
            else:
                msg = f"Canción encontrada: {elem['titulo']} (ID: {elem['id']})\nArtísta: {elem['artista']}\n Género: {elem['genero']}\n Valoración: {elem['valoracion']} estrellas"
            print(msg)
    else:
        msg = f"No se encontró ningún elemento con el autor/director/artista '{nombre_buscar}'."

    print(msg)
    sc.pausar_pantalla()
    return

def buscarElementoGenero():
    sc.limpiar_pantalla()
    libros_data = cf.readJson(cfg.DB_LIBROS)
    peliculas_data = cf.readJson(cfg.DB_PELICULAS)
    musica_data = cf.readJson(cfg.DB_MUSICA)
    if not libros_data and not peliculas_data and not musica_data:
        print("No hay elementos en la colección.")
        sc.pausar_pantalla()
        return
    
    opGenero = vd.validateInt("Seleccione  la categoría del género a buscar:\n1. Libros\n2. Películas\n3. Música\n4. Regresar al menú principal\nOpción: ")
    if not opGenero:
        print("ERROR: El género no puede estar vacío.")
        sc.pausar_pantalla()
        return
    if opGenero < 1 or opGenero > 4:
        print("ERROR: Opción no válida.")
        sc.pausar_pantalla()
        return
    if opGenero == 1:
        print("-> Lista de géneros disponibles: ")
        for i, genero in enumerate(generos_libros, start= 1):
            print(f"{i}. {genero}")
        genero_opcion = vd.validateInt(f"Seleccione el género de libro (1-{len(generos_libros)}): ")
        if genero_opcion < 1 or genero_opcion > len(generos_libros):
            print("ERROR: Opción no válida.")
            sc.pausar_pantalla()
            return
        genero_buscar = generos_libros[genero_opcion - 1]
        
        encontrado = []
        for libro in libros_data.get("libros", {}).values():
            if libro.get("genero", "").lower() == genero_buscar.lower():
                encontrado.append(libro)
        
        if encontrado:
            for libro in encontrado:
                msg = f"Libro encontrado: {libro['titulo']} (ID: {libro['id']})\nAutor: {libro['autor']}\n Género: {libro['genero']}\n Valoración: {libro['valoracion']} estrellas"
                print(msg)
        else:
            msg = f"No se encontró ningún libro con el género '{genero_buscar}'."
            print(msg)
    elif opGenero == 2:
        print("-> Lista de géneros disponibles: ")
        for i, genero in enumerate(generos_peliculas, start= 1):
            print(f"{i}. {genero}")
        genero_opcion = vd.validateInt(f"Seleccione el género de película (1-{len(generos_peliculas)}): ")
        if genero_opcion < 1 or genero_opcion > len(generos_peliculas):
            print("ERROR: Opción no válida.")
            sc.pausar_pantalla()
            return
        genero_buscar = generos_peliculas[genero_opcion - 1]
        
        encontrado = []
        for pelicula in peliculas_data.get("peliculas", {}).values():
            if pelicula.get("genero", "").lower() == genero_buscar.lower():
                encontrado.append(pelicula)
        
        if encontrado:
            for pelicula in encontrado:
                msg = f"Pelicula encontrada: {pelicula['titulo']} (ID: {pelicula['id']})\nDirector: {pelicula['director']}\n Género: {pelicula['genero']}\n Valoración: {pelicula['valoracion']} estrellas"
                print(msg)
        else:
            msg = f"No se encontró ninguna película con el género '{genero_buscar}'."
            print(msg)    
    elif opGenero == 3:
        print("-> Lista de géneros disponibles: ")
        for i, genero in enumerate(generos_musica, start= 1):
            print(f"{i}. {genero}")
        genero_opcion = vd.validateInt(f"Seleccione el género de música (1-{len(generos_musica)}): ")
        if genero_opcion < 1 or genero_opcion > len(generos_musica):
            print("ERROR: Opción no válida.")
            sc.pausar_pantalla()
            return
        genero_buscar = generos_musica[genero_opcion - 1]
        
        encontrado = []
        for cancion in musica_data.get("cancion", {}).values():
            if cancion.get("genero", "").lower() == genero_buscar.lower():
                encontrado.append(cancion)
        
        if encontrado:
            for cancion in encontrado:
                msg = f"Canción encontrada: {cancion['titulo']} (ID: {cancion['id']})\nDirector: {cancion['artista']}\n Género: {cancion['genero']}\n Valoración: {cancion['valoracion']} estrellas"
                print(msg)
        else:
            msg = f"No se encontró ninguna canción con el género '{genero_buscar}'."
            print(msg)    