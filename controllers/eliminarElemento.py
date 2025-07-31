import utils.corefiles as cf
import utils.screenControllers as sc
import utils.validateData as vd
import config as cfg

def eliminarPorTitulo():
    sc.limpiar_pantalla()
    libros_data = cf.readJson(cfg.DB_LIBROS)
    peliculas_data = cf.readJson(cfg.DB_PELICULAS)
    musica_data = cf.readJson(cfg.DB_MUSICA)
    print("==============================================")
    print("         Eliminar un Elemento por Título      ")  
    print("==============================================")      
    if not libros_data and not peliculas_data and not musica_data:
        print("No hay elementos en la colección.")
        sc.pausar_pantalla()
        return
    
    titulo_buscar = vd.validate_string("Ingrese el título del elemento a eliminar: ").title().strip()
    if not titulo_buscar:
        print("ERROR: El título no puede estar vacío.")
        sc.pausar_pantalla()
        return
    
    for libro in libros_data.get("libros", {}).values():
        if libro.get("titulo", "").lower() == titulo_buscar.lower():
            elemento_id = libro['id']
            del libros_data["libros"][elemento_id]
            cf.writeJson(cfg.DB_LIBROS, libros_data)
            msg = f"Libro '{titulo_buscar}' eliminado con éxito."
            sc.pausar_pantalla()
            return
        else:
            msg = f"No se encontró ningún libro con el título '{titulo_buscar}'."
        
    for pelicula in peliculas_data.get("peliculas", {}).values():
        if pelicula.get("titulo", "").lower() == titulo_buscar.lower():
            elemento_id = pelicula['id']
            del peliculas_data["peliculas"][elemento_id]
            cf.writeJson(cfg.DB_PELICULAS, peliculas_data)
            msg = f"Película '{titulo_buscar}' eliminada con éxito."
            sc.pausar_pantalla()
            return
        else:
            msg = f"No se encontró ninguna pelicula con el título '{titulo_buscar}'."
    
    for cancion in musica_data.get("canciones", {}).values():
        if cancion.get("titulo", "").lower() == titulo_buscar.lower():
            elemento_id = cancion['id']
            del musica_data["canciones"][elemento_id]
            cf.writeJson(cfg.DB_MUSICA, musica_data)
            msg = f"Canción '{titulo_buscar}' eliminada con éxito."
            sc.pausar_pantalla()
            return
        else:
            msg = f"No se encontró ninguna canción con el título '{titulo_buscar}'."
    
    if msg:
        print(msg)
    else:
        print(f"No se encontró ningún elemento con el título '{titulo_buscar}'.")
    sc.pausar_pantalla()
    return

def eliminarPorID():
    sc.limpiar_pantalla()
    libros_data = cf.readJson(cfg.DB_LIBROS)
    peliculas_data = cf.readJson(cfg.DB_PELICULAS)
    musica_data = cf.readJson(cfg.DB_MUSICA)
    print("=========================================")
    print("        Eliminar un Elemento por ID      ")  
    print("=========================================")      
    if not libros_data and not peliculas_data and not musica_data:
        print("No hay elementos en la colección.")
        sc.pausar_pantalla()
        return
    siConoce = vd.validateBoolean("¿Conoce el ID del elemento a eliminar? (S/N): ")
    if not siConoce:
        eliminarPorTitulo()
        return
    id_buscar = vd.validateInt("Ingrese el ID del elemento a eliminar: ")
    if not id_buscar:
        print("ERROR: El ID no puede estar vacío.")
        sc.pausar_pantalla()
        return
    
    for libro in libros_data.get("libros", {}).values():
        if libro.get("id", "") == id_buscar:
            elemento_id = libro['id']
            del libros_data["libros"][elemento_id]
            cf.writeJson(cfg.DB_LIBROS, libros_data)
            msg = f"Libro '{id_buscar}' eliminado con éxito."
            sc.pausar_pantalla()
            return
        else:
            msg = f"No se encontró ningún libro con el ID '{id_buscar}'."
        
    for pelicula in peliculas_data.get("peliculas", {}).values():
        if pelicula.get("id", "") == id_buscar:
            elemento_id = pelicula['id']
            del peliculas_data["peliculas"][elemento_id]
            cf.writeJson(cfg.DB_PELICULAS, peliculas_data)
            msg = f"Película '{id_buscar}' eliminada con éxito."
            sc.pausar_pantalla()
            return
        else:
            msg = f"No se encontró ninguna pelicula con el ID '{id_buscar}'."
    
    for cancion in musica_data.get("canciones", {}).values():
        if cancion.get("id", "") == id_buscar:
            elemento_id = cancion['id']
            del musica_data["canciones"][elemento_id]
            cf.writeJson(cfg.DB_MUSICA, musica_data)
            msg = f"Canción '{id_buscar}' eliminada con éxito."
            sc.pausar_pantalla()
            return
        else:
            msg = f"No se encontró ninguna canción con el ID '{id_buscar}'."
    
    if msg:
        print(msg)
    else:
        print(f"No se encontró ningún elemento con el ID '{id_buscar}'.")
    sc.pausar_pantalla()
    return