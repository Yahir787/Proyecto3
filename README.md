# Artworks Proyecto 3

## Integrantes
* Gonzalez Dominguez Yahir Emiliano 20211783
* Jimenez Herrera Alan 20211795
* Rosales Espinoza Edgar Uriel 2021
* Sobrado Espinoza Sergio Rosario 20211848

## Capturas de Pantalla 

## Funcionalidades
* El usuario puede inciar sesión
* El usuario puede crear colecciones de pinturas y añardir pinturas a sus colecciones
* El usuario puede editar las caracteriticas de las colecciones
* El usuario puede eliminar las colecciones que le pertenecen
* La pagina carga 12 pinturas de manera aleatoria y puede cargar más con un botón
* La pagina permite buscar pinturas por autores, generos y nombres de pinturas
* Las pinturas muestran el nombre, el autor y la fecha de creación

## Descripción General

Este proyecto consiste en una aplicación para guardar, compartir y coleccionar 
obras de arte o algún otro elemento de interés para los usuarios. La aplicación se inspira en aplicaciones tipo 
Pinterest, FIFA Ultimate Team o HearthStone donde los usuarios coleccionan elementos y los
pueden comartir de alguna manera. La aplicación debe implementar la siguiente funcionalidad:

* Los usarios pueden agregar elementos a diferentes colecciones, por ejeplo 
favoritos, me interesan, en venta, etc. 
* Debes proponer alguna manera de que los usuarios obtengan elementos. Algunas ideas:
    * Que los usuarios compren paquetes los cuales incluyen items seleccionados de manera aleatoria.
    * Los usuarios compran elementos directamente en una tienda.
    * Los usuarios ofrecen creditos en una subasta para conseguir a los elementos.
    * Simplemente los eligen de la página. Esto es parecido a Pinterest.
* Los usuarios pueden gestionar sus colecciones agregando, eliminando, moviendo e intercambiando elementos de las colecciones.
* Los usuarios deben buscar elementos haciendo una búsqueda por facetas o categorías [Ejemplo con PostgreSQL](https://www.youtube.com/watch?v=QFs6qgvyTC4).

Utiliza este repositorio como base.  Ya incluye el regístro básico de usuarios y la capacidad de iniciar sesión. 

Para el proyecto que haremos en clase, utilizaremos como ítems una muestra de 
obras de arte del sitio [wikiart](https://www.wikiart.org/). Puedes basarte en [este repositorio](https://github.com/mariosky/ArtTest) 
para un modelo básico, scripts de [web scraping](https://es.wikipedia.org/wiki/Web_scraping) y carga de los datos a la base de datos.

Una vez que tengamos la base de datos podemos iniciar la implementación de los puntos anteriores. 

## Requerimientos Técnicos

En esta aplicación utilizaremos programación del lado del cliente utilizando las librerías [htmx](https://htmx.org/) y [hyperscript](https://hyperscript.org/).  
De manera opcional puedes utilizar otras librerías o JS.

### Imágenes 
Pagina principal
![Pagina Principal](Imagenes/PantallaPrincipal.png)

Vista Detalla de la pintura
![Vista detallada](Imagenes/artwork.png)

Vista de la busqueda
![Actor](Imagenes/busqueda.png)

Vista detallada de las colecciones
![Actor](Imagenes/colecciones.png)



