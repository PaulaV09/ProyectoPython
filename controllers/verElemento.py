import utils.corefiles as cf
import utils.screenControllers as sc
import utils.validateData as vd
import config as cfg


def listarLibros():
    libros = cf.readJson(cfg.DB_LIBROS)
    print("-------Libros------")
    if not libros:
        print("No hay libros registrados.")
        return
    for cod, libro in libros.items():
        print(f"{cod}. {libro['']}\n {libro['titulo']}\n {libro['autor']}\n {libro['genero']}\n {libro['valoracion']}\n")
    sc.pausar_pantalla()



def listarMusica():
    musica = cf.readJson(cfg.DB_MUSICA)
    print("-------Musica------")
    if not musica:
        print("No hay musica registrada.")
        return
    for cod, music in musica.items():
        print(f"{cod}. {music['']}\n {music['titulo']}\n {music['artista']}\n {music['genero']}\n {music['valoracion']}\n")
    sc.pausar_pantalla()
    
def listarPeliculas():
    peliculas = cf.readJson(cfg.DB_PELICULAS)
    print("-----Peliculas-----")
    if not peliculas:
        print("No hay peliculas registradas.")
        return
    for cod, pelicula in peliculas.items():
        print(f"{cod}. {pelicula['']}\n {pelicula['titulo']}\n {pelicula['director']}\n {pelicula['genero']}\n {pelicula['valoracion']}\n")
    sc.pausar_pantalla()

def listarColeccion():
    listarLibros()
    listarMusica()
    listarPeliculas()

