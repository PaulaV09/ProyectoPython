from tabulate import tabulate
import utils.corefiles as cf
import utils.screenControllers as sc
import utils.validateData as vd
import config as cfg

def listarLibros():
    data = cf.readJson(cfg.DB_LIBROS)
    libros = data.get("libros", {})

    print("-------Libros------")
    if not libros:
        print("No hay libros registrados.")
        return

    tabla = []
    for cod, libro in libros.items():
        tabla.append([
            cod,
            libro.get("titulo", "N/A"),
            libro.get("autor", "N/A"),
            libro.get("genero", "N/A"),
            libro.get("valoracion", "N/A")
        ])

    print(tabulate(tabla, headers=["ID", "Título", "Autor", "Género", "Valoración"], tablefmt="fancy_grid"))
    sc.pausar_pantalla()

def listarMusica():
    data = cf.readJson(cfg.DB_MUSICA)
    musica = data.get("canciones", {})

    print("-------Música------")
    if not musica:
        print("No hay música registrada.")
        return

    tabla = []
    for cod, cancion in musica.items():
        tabla.append([
            cod,
            cancion.get("titulo", "N/A"),
            cancion.get("autor", "N/A"),
            cancion.get("genero", "N/A"),
            cancion.get("valoracion", "N/A")
        ])

    print(tabulate(tabla, headers=["ID", "Título", "Autor", "Género", "Valoración"], tablefmt="fancy_grid"))
    sc.pausar_pantalla()

def listarPeliculas():
    data = cf.readJson(cfg.DB_PELICULAS)
    peliculas = data.get("peliculas", {})

    print("-----Películas-----")
    if not peliculas:
        print("No hay películas registradas.")
        return

    tabla = []
    for cod, pelicula in peliculas.items():
        tabla.append([
            cod,
            pelicula.get("titulo", "N/A"),
            pelicula.get("director", "N/A"),
            pelicula.get("genero", "N/A"),
            pelicula.get("valoracion", "N/A")
        ])

    print(tabulate(tabla, headers=["ID", "Título", "Director", "Género", "Valoración"], tablefmt="fancy_grid"))
    sc.pausar_pantalla()

def listarColeccion():
    listarLibros()
    listarMusica()
    listarPeliculas()
