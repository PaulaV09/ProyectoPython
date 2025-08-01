# Proyecto de Biblioteca Multimedia

## 📝 Descripción

Este es un sistema de gestión de una **Biblioteca Multimedia**, una aplicación de consola desarrollada en Python. Permite a los usuarios organizar y explorar colecciones de libros, música y películas de forma interactiva. La información se almacena en archivos JSON, lo que facilita su manipulación y extensión.

## 🚀 Tecnologías Utilizadas

* **Lenguaje:** Python 3.x

  **Librerías de terceros:**

  - `tabulate`: Para formatear los datos de la biblioteca en tablas.

  **Librerías estándar:**

  - `json`: Para la lectura y escritura de los archivos de datos.
  - `os`, `sys`: Para la gestión de rutas de archivos y reconocer el sistema operativo.
  - `typing`: Para la declaración de tipos de datos en el código.

## 📂 Estructura del Proyecto

El proyecto está organizado de la siguiente manera:

```
ProyectoPython/
├── app/
│   ├── mainmenu.py               # Módulo con el menú principal de la aplicación.
│   └── submenus.py               # Módulo con los submenús para cada función.
├── controllers/
│   ├── anadirElemento.py         # Módulo para añadir un elemento a la colección.
│   ├── buscarElemento.py         # Módulo para buscar elementos por título, autor o género.
│   ├── editarElemento.py         # Módulo para editar un elemento existente.
│   ├── eliminarElemento.py       # Módulo para eliminar elementos por título o ID.
│   └── verElemento.py            # Módulo para listar elementos por tipo.
├── data/
│   ├── libros.json               # Base de datos de libros.
│   ├── musica.json               # Base de datos de música.
│   └── peliculas.json            # Base de datos de películas.
├── utils/
│   ├── corefiles.py              # Funciones para la manipulación de archivos JSON.
│   ├── screenControllers.py      # Funciones para el manejo de la interfaz de consola.
│   └── validateData.py           # Funciones para validar la entrada de datos del usuario.
├── .gitignore                    
├── config.py                     # Archivo de configuración para las rutas de los datos.
└── main.py                       # Punto de entrada principal de la aplicación.  
└── README.md          		      
```

## Formato de los Datos

Los datos de la biblioteca se encuentran en la carpeta `data/` en formato JSON. Cada archivo (`libros.json`, `musica.json`, `peliculas.json`) contiene un objeto principal con una clave que representa la categoría (ej. "libros") y cuyo valor es un diccionario de elementos.

Cada elemento tiene una estructura similar:

-   **`id`**: Identificador único del elemento.
-   **`titulo`**: Título del libro, canción o película.
-   **`genero`**: Género al que pertenece.
-   **`valoracion`**: Puntuación o calificación (de 1 a 5).
-   **Campos específicos**:
    -   Para libros: `autor`.
    -   Para música: `artista`.
    -   Para películas: `director`.

### Ejemplo de un libro (`libros.json`):

```json
{
    "id": "1",
    "titulo": "1984",
    "autor": "George Orwell",
    "genero": "Ciencia ficción",
    "valoracion": 4.7
}
```

### Ejemplo de una película (`peliculas.json`):

```json
{
    "id": "1",
    "titulo": "El Padrino",
    "director": "Francis Ford Coppola",
    "genero": "Crimen",
    "valoracion": 5.0
}
```

### Ejemplo de una canción (`musica.json`):

```json
{
    "id": "1",
    "titulo": "Bohemian Rhapsody",
    "artista": "Queen",
    "genero": "Rock",
    "valoracion": 5.0
}
```

- **Carga de datos:** Carga dinámica y automática de los catálogos de libros, música y películas desde los archivos JSON. 
- **Visualización:** Muestra listas completas de los elementos y detalles individuales. 
- **Búsqueda:** Permite buscar elementos por título, autor, artista, director o género. 
- **Filtrado:** Los catálogos se pueden filtrar por por tipo de elemento (libro, película o canción). 
- **Gestión de datos:** Ofrece funcionalidades completas para añadir, editar y eliminar elementos de cada categoría.

## Requisitos 

- Asegúrate de tener **Python** instalado en tu máquina.

- Para instalar las dependencias necesarias, ejecuta el siguiente comando:

  ```bash
  pip install tabulate
  ```

## Instalación y Ejecución

Para poner en marcha este proyecto en tu máquina local, sigue estos pasos:

1. **Clona el repositorio:**

   ```bash
   git clone https://github.com/PaulaV09/ProyectoPython.git
   cd ProyectoPython
   ```

2. **Ejecuta la aplicación:**

    ```bash
   python main.py
   ```