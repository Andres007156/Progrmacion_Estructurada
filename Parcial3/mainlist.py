'''
Crear un proyecto que permita gestionar (administrar) peliculas. Colocar un menu de opciones: Agregar, Borrar, Modificar, Mostrar, Buscar, Limpiar una lista de peliculas.

Notas: 
1.- Utilizar funciones y mandar llamar desde otro archivo (modulo)
2.- Utilizar dict para almacenar los atributos (nombre,categoria,clasificacion,genero,idioma) de peliculas
3.- Utilizar o implementar BD relacional con MySQL para guardar la información

'''
from peliculaslist import peliculas
import funcioneslist

pelis=[]

opc=""

while opc!="7":
    funcioneslist.borrarPantalla()
    opc=peliculas.menuPrincial()
    match opc:
        case "1":
            funcioneslist.borrarPantalla()
            peliculas.agregarPeliculas(pelis)
        case "2":
            funcioneslist.borrarPantalla()
            peliculas.borrarPeliculas(pelis)
        case "3":
            funcioneslist.borrarPantalla()
            peliculas.modificarPeliculas(pelis)
        case "4":
            funcioneslist.borrarPantalla()
            peliculas.mostrarPeliculas(pelis)
        case "5":
            funcioneslist.borrarPantalla()
            peliculas.buscarPeliculas(pelis)
        case "6":
            funcioneslist.borrarPantalla()
            peliculas.limpiarPeliculas(pelis)
        case "7":
            funcioneslist.borrarPantalla()
            funcioneslist.terminarSistema()
        case _:
            funcioneslist.opcionInvalida()
