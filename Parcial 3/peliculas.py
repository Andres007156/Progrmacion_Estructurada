import funciones
pelis={
    "nombre":"TOY STORY 5",
    "duracion":"120 MIN",
    "idioma":"ESPAÑOL",
    "clasificacion":"A",
    "genero":"ANIMADA"
}     
def menuPrincial():
    print("\n\t\t...:::: M E N U  P R I N C I P A L ::::...\n")
    opcion=input("\n\t1.- Agregar\n\t2.- Borrar\n\t3.- Modificar\n\t4.- Mostrar\n\t5.- Buscar\n\t6.- Limpiar\n\t7.- Salir\n\t\tEscribe un opcion: ").strip()
    return opcion

def agregarPeliculas(pelis):
    print("\n\t\t...:::: AGREGAR CARACTERISTICAS DE UNA PELICULA ::::...\n")
    caracteristica=input("Introducir el nombre de la caracteristica: ").lower().strip()
    valor=input("Introduce el valor de la caracteristica: ").upper().strip()
    pelis[caracteristica]=valor
    funciones.accionExitosa()

def mostrarPeliculas(pelis):
    print("\n\t\t...:::: MOSTRAR CARACTERISTICAS DE UNA PELICULA ::::...\n")
    print("\tCaracteristica\t\tValor\n")
    if len(pelis)>0:
        for i in pelis:
            print(f"{i}\t\t{pelis[i]}")
        funciones.espereTecla()
    else:
        input("\n\t...¡No hay caracteristicas a mostrar de la pelicula!...")
    
def limpiarPeliculas(pelis):
    if len(pelis)>0:
        opc=""
        while opc!="si" and opc!="no":
            opc=input("¿Deseas borrar TODAS las caracteristicas (Si/No)? ").lower().strip()
            if opc=="si":
                pelis.clear()
                funciones.accionExitosa()
            else:
                input("Accion cancelada: ")
    else:
        input("...¡No hay peliculas que borrar!...") 
        
def buscarPeliculas(pelis):
    print("\n\t\t...:::: BUSCAR UNA CARACTERISTICA DE UNA PELICULA ::::...\n")
    caracteristica=input("Escribir el nombre de la caracteristica: ").upper().strip()
    noencontro=True
    for i in pelis:
        if caracteristica==i:
            print("\tCaracteristica\t\tValor\n")
            print(f"{i}\t\t{pelis[i]}")
            noencontro=False
        funciones.espereTecla()
    if noencontro:
        input("...¡No exite la pelicula que estas buscando, verifique!...")

def borrarPeliculas(pelis):
    print("\n\t\t...:::: BORRAR UNA CARACTERISTICA DE UNA PELICULA::::...\n")
    caracteristica=input("Escribir el nombre de la caracteristica: ").lower().strip()
    noencontro=True
    for i in pelis:
        if caracteristica==i:
            opc=""
            while opc!="si" and opc!="no":
                opc=input("¿Deseas borrar el valor de la caracteristica (Si/No)? ").lower().strip()
            if opc=="si":
                pelis.pop(caracteristica)
                funciones.accionExitosa()
                noencontro=False
    if noencontro:
        input("...¡No exite la caracteristica que estas buscando, verifique!...")
  
def modificarPeliculas(pelis):
    print("\n\t\t...:::: MODIFICAR EL VALOR DE LA CARACTERISTICA DE UNA PELICULA ::::...\n")
    caracteristica=input("Escribir el valor de la caracteristica: ").upper().strip()
    noencontro=True
    if caracteristica in pelis:
        print("\tCaracteristica\t\tValor\n")
        print(f"{caracteristica}\t\t{pelis[caracteristica]}")
        for i in pelis:
            if caracteristica==i:
                opc=""
                while opc!="si" and opc!="no":
                    opc=input("¿Deseas modificar la caracteristica (Si/No)? ").lower().strip()
                if opc=="si":
                    valor=input("Escribe el nuevo valor de la caracteristica: ").upper().strip()
                    pelis.update({caracteristica:valor})
                    noencontro=False
                    funciones.accionExitosa()
                if opc=="no":
                    input("Cancelando accion")
                    noencontro=False
    if noencontro:
        input("...¡No exite la caracteristica que estas buscando, verifique!...")

def modificarPeliculas(pelis):
    print("\n\t\t...:::: MODIFICAR EL VALOR DE LA CARACTERISTICA DE UNA PELICULA ::::...\n")
    caracteristica=input("Escribir el valor de la caracteristica: ").upper().strip()
    noencontro=True
    for i in range(0,len(pelis)):    
        if caracteristica in pelis:
            print("\tCaracteristica\t\tValor\n")
            print(f"{caracteristica}\t\t{pelis[caracteristica]}")
            if caracteristica==i:
                opc=""
                while opc!="si" and opc!="no":
                    opc=input("¿Deseas modificar la caracteristica (Si/No)? ").lower().strip()
                if opc=="si":
                    pelis[caracteristica]=input("Escribe el nuevo valor de la caracteristica: ").upper().strip()
                    noencontro=False
                    funciones.accionExitosa()
                if opc=="no":
                    input("Cancelando accion")
                    noencontro=False
    if noencontro:
        input("...¡No exite la caracteristica que estas buscando, verifique!...")