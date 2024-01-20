from  pathlib import Path
from os import system , mkdir

def suma_final():
    lista_final =[]
    categorias= Path("C:/Users/karen/OneDrive/Escritorio/Recetas")
    for carpetas in categorias.iterdir():  # iterar sobre los elementos de la ruta
        if carpetas.is_dir(): # mira  si es una carpeta o no y retorna false o true
            for subcarpetas in carpetas.iterdir():
                if subcarpetas.is_dir():
                    for archivo in subcarpetas.iterdir():
                        if archivo.is_file(): #comprueba que sea un archivo
                            lista_final.append(archivo.name)
    return len(lista_final)
cantidad_de_archivos = suma_final()
#________________________________________________________________________________________________________
def imprimir_menu():
    Lista_menu = ["Leer receta" , "Crear receta" , "Crear categoria" , "Eliminar receta" , 
"Eliminar categoria" , "Finalizar o salir de programa"]
    print("MENU DE OPCIONES:")
    print()
    for indice, opcion_menu in enumerate(Lista_menu, 1):
        print(f"{indice}. {opcion_menu}")
    print()
    opcion= int(input("Ingresa una opcion del _ 1 _ al _6_ :   "))
    if opcion == 1:
        leer_receta()
    elif opcion == 2:
        crear_receta()
    elif opcion == 3:
        crear_categoria()
    elif opcion == 4:
        eliminar_receta()
    elif opcion == 5:
        eliminar_categoria()
    elif opcion == 6:
        Finalizar()
#__________________________________________________________________________________________________________
print("Hola! en este programa podras encontrar recetas culinarias que podras leer , Crear o eliminar a tu gusto")
print(f"En el momento tienes {cantidad_de_archivos} recetas") 
print()
#______________________________________________________________________________________

#FUNCION PARA ENCONTRAR LAS CATEGORIAS
def calcular_categorias(ruta): #Defino una funcion donde puedo ingresar la ruta
    mi_ruta = Path(ruta)
    lista_categorias = [] #Lista donde se va almacenaer todas las categorias que sean carpet
    for archivo in mi_ruta.iterdir():  # iterar sobre los elementos de la ruta
        if archivo.is_dir(): # mira  si es una carpeta o no y retorna false o true
            lista_categorias.append(archivo.name) # añado nuevos a lista vacia
           
    return lista_categorias #retornamos la lista
#_________________________________________________________________________________
#FUNCION PARA ENCONTRAR LAS RECETAS
def calcular_receta(ruta): #Defino una funcion donde puedo ingresar la ruta
    mi_ruta = Path(ruta)
    lista_recetas = [] #Lista donde se va almacenaer todas las categorias que sean carpet
    for receta in mi_ruta.iterdir():  # iterar sobre los elementos de la ruta
        if receta.is_file(): # mira  si es una carpeta o no y retorna false o true
            lista_recetas.append(receta.name) # añado nuevos a lista vacia
           
    return lista_recetas #retornamos los archivos
#_________________________________________________________________________________
def leer_receta():
    leer = Path("C:/Users/karen/OneDrive/Escritorio/Recetas")
    categorias = calcular_categorias('C:/Users/karen/OneDrive/Escritorio/Recetas') #llamamos la funcion creada anteriormente
    categorias_minuscula = [n.lower() for n in categorias] #vuelvo todo elemento minuscula
    eleccion_Categoria= input(f"Las categorias disponibles en el momento son: \n{" "+"\n ".join(categorias)}\n  \n Escribe aqui cual deseas leer:  ").lower()
    print()
    if eleccion_Categoria in categorias_minuscula:
        tipo_receta = calcular_categorias(f'C:/Users/karen/OneDrive/Escritorio/Recetas/{eleccion_Categoria}')
        tipo_receta= [x.lower() for x in tipo_receta]
        eleccion_receta= input(f"Las recetas disponibles en el momento son:\n\n{" "+"\n ".join(tipo_receta)}\n  \n Escribe aqui cual deseas leer:  ").lower()#Tipos de carnes o tipos de ensaladas
        if eleccion_receta in tipo_receta:
            lista_recetas= calcular_receta(f'C:/Users/karen/OneDrive/Escritorio/Recetas/{eleccion_Categoria}/{eleccion_receta}')
            print(f"Las recetas de {eleccion_receta} que tenemos disponibles son las siguientes:\n")
            for indice, receta in enumerate(lista_recetas, 1):
                print(f"{indice}.{receta}")
            print()
            receta_elegida= int(input("Escriba el numero de la receta que desea leer:       \n"))
            if receta_elegida >0 and receta_elegida < len(lista_recetas):   
                print()
                mi_archivo = Path(f"C:/Users/karen/OneDrive/Escritorio/Recetas/{eleccion_Categoria}/{eleccion_receta}/{lista_recetas[receta_elegida-1]}")
                if mi_archivo.exists():
                    with open(mi_archivo, "r") as archivo:
                        contenido = archivo.read()
                        print(contenido)  
            else:
                print("La opcion que a ingresado no es correcta o no a sido encontrada, Por favor intente nuevamente")
                imprimir_menu()
                  
        else:
            print("La opcion que a ingresado no es correcta o no a sido encontrada, Por favor intente nuevamente")
            imprimir_menu()
            print()       
    else:
        print("La opcion que a ingresado no es correcta o no a sido encontrada, Por favor intente nuevamente")
        
        imprimir_menu() 
#_______________________________________________________________________________________
def crear_receta():
    crear_recetas_nuevas = Path("C:/Users/karen/OneDrive/Escritorio/Recetas")
    categorias = calcular_categorias('C:/Users/karen/OneDrive/Escritorio/Recetas') #llamamos la funcion creada anteriormente
    categorias_minuscula = [n.lower() for n in categorias] #vuelvo todo elemento minuscula
    eleccion_Categoria= input(f"Las categorias disponibles en el momento son: \n{" "+"\n ".join(categorias)}\n  \n Elija sobre que categoria desea crear nueva receta:  ").lower()
    
    print()
    if eleccion_Categoria in categorias_minuscula:
        tipo_receta = calcular_categorias(f'C:/Users/karen/OneDrive/Escritorio/Recetas/{eleccion_Categoria}')
        print(f"Las recetas disponibles en el momento son:\n\n{" "+"\n ".join(tipo_receta)}\n  \n ")
        elegir_categoria= str(input("En que categoria desea crear la nueva receta?:   ")).lower()
        tipo_receta = [n.lower() for n in tipo_receta]
        if elegir_categoria in tipo_receta:
            nombre_receta_nueva= str(input("Ingrese el nombre de la receta : ")).lower()
            tipo_receta.append(nombre_receta_nueva)
            añadir_receta = open (f"C:/Users/karen/OneDrive/Escritorio/Recetas/{eleccion_Categoria}/{elegir_categoria}/{nombre_receta_nueva}.txt" , "w")
            añadir_receta.write(str(input(f"Añada la receta de {nombre_receta_nueva}:   ".lower())))
            print("Creada satisfactoriamente")
            añadir_receta.close()
    imprimir_menu()
#_________________________________________________________________________________________
def crear_categoria():
    crear_categorias_nuevas = Path("C:/Users/karen/OneDrive/Escritorio/Recetas")
    categorias = calcular_categorias(crear_categorias_nuevas)
    categorias_minuscula = [n.lower() for n in categorias]
    
    nueva_categoria = input("Ingrese el nombre de la categoría que va a crear:   ").lower()
    print()
    if nueva_categoria not in categorias:
        categorias.append(nueva_categoria)
        nueva_categoria_path = crear_categorias_nuevas / nueva_categoria
        nueva_categoria_path.mkdir()

        nombre_de_categoria_nueva = input(f"Añada el nombre de la nueva receta de {nueva_categoria}:  ").lower()
        nombre_de_categoria_nueva_path = nueva_categoria_path / (f"{nombre_de_categoria_nueva}.txt")

        with open(nombre_de_categoria_nueva_path, "w") as archivo:
            nueva_receta = input(f"Añada la receta de {nombre_de_categoria_nueva}:   ").lower()
            archivo.write(nueva_receta)
        print("Categoría y receta nueva creadas exitosamente.")
        
    else:
        print("Esta categoría ya existe, por favor inténtelo nuevamente.") 
        imprimir_menu()
#_______________________________________________________________________________________________________
import os
from pathlib import Path

def eliminar_receta():
    crear_categorias_nuevas = Path("C:/Users/karen/OneDrive/Escritorio/Recetas")
    categorias = calcular_categorias(crear_categorias_nuevas)
    categorias_minuscula = [x.lower() for x in categorias]
    eleccion_Categoria_eliminar= input(f"Las categorias disponibles en el momento son: \n{" "+"\n ".join(categorias_minuscula)}\n  \n Ingrese el nombre de la categoría a eliminar:  ").lower()
    print()
    if eleccion_Categoria_eliminar not in categorias_minuscula:
        print("La categoría ingresada no existe. Intente nuevamente :)")
        imprimir_menu()
    else:
        tipo_receta = calcular_categorias(f'C:/Users/karen/OneDrive/Escritorio/Recetas/{eleccion_Categoria_eliminar}')
        tipo_receta= [x.lower() for x in tipo_receta]
        eleccion_receta_ELIMINAR= input(f"Las recetas disponibles en el momento son:\n\n{" "+"\n ".join(tipo_receta)}\n  \n Escribe aqui cual deseas ELIMINAR:  ").lower()#Tipos de carnes o tipos de ensaladas
        
        if eleccion_receta_ELIMINAR in tipo_receta:
            lista_recetas= calcular_receta(f'C:/Users/karen/OneDrive/Escritorio/Recetas/{eleccion_Categoria_eliminar}/{eleccion_receta_ELIMINAR}')
            print(f"Las recetas de {eleccion_receta_ELIMINAR} que tenemos disponibles son las siguientes:\n")
            
            for indice, receta in enumerate(lista_recetas, 1):
                print(f"{indice}.{receta}")
                print()
            receta_elegida= int(input("Escriba el numero de la receta que desea ELIMINAR:   ")) 
            print()          
            if receta_elegida>0 and receta_elegida <= len(lista_recetas):
                mi_archivo = Path(f"C:/Users/karen/OneDrive/Escritorio/Recetas/{eleccion_Categoria_eliminar}/{eleccion_receta_ELIMINAR}/{lista_recetas[receta_elegida-1]}")
                if mi_archivo.exists():
                    os.remove(f"C:/Users/karen/OneDrive/Escritorio/Recetas/{eleccion_Categoria_eliminar}/{eleccion_receta_ELIMINAR}/{lista_recetas[receta_elegida-1]}")
                    print(f"Receta de '{mi_archivo}' eliminado exitosamente.")
                else:
                    print("La opcion que a ingresado no es correcta o no a sido encontrada, Por favor intente nuevamente")
        else:
            print("La opcion que a ingresado no es correcta o no a sido encontrada, Por favor intente nuevamente")
            imprimir_menu()
    imprimir_menu()
#___________________________________________________________________________________________________________
import shutil
def eliminar_categoria():
    crear_categorias_nuevas = Path("C:/Users/karen/OneDrive/Escritorio/Recetas")
    categorias = calcular_categorias(crear_categorias_nuevas)
    categorias_minuscula = [n.lower() for n in categorias]
    
    eliminar_categoria = input("Ingrese el nombre de la categoría que desea eliminar:   ").lower()
    print()
    if eliminar_categoria in categorias_minuscula:
        confirmacion =input(f"¿Está seguro de que desea eliminar la categoria COMPLETA '{eliminar_categoria}'? SI o NO:  ").lower()
        eliminar_categoria_path = crear_categorias_nuevas / eliminar_categoria
        if confirmacion == "si":
            shutil.rmtree(Path(eliminar_categoria_path))
            print("Categoria eliminada exitosamente.")
        
    else:
        print("Esta categoría ya existe, por favor inténtelo nuevamente.") 
        imprimir_menu()
#______________________________________________________________________________________________________________
def Finalizar():
    print("Gracias por usar nuestra app de cocina, Te esperamos pronto :) ")
#_____________________________________________________________________________________________________________
def imprimir_menu():
    Lista_menu = ["Leer receta" , "Crear receta" , "Crear categoria" , "Eliminar receta" , 
"Eliminar categoria" , "Finalizar o salir de programa"]
    print("MENU DE OPCIONES:")
    print()
    for indice, opcion_menu in enumerate(Lista_menu, 1):
        print(f"{indice}. {opcion_menu}")
    print()
    opcion= int(input("Ingresa una opcion del _ 1 _ al _6_ :   "))
    if opcion == 1:
        leer_receta()
    elif opcion == 2:
        crear_receta()
    elif opcion == 3:
        crear_categoria()
    elif opcion == 4:
        eliminar_receta()
    elif opcion == 5:
        eliminar_categoria()
    elif opcion == 6:
        Finalizar()
imprimir_menu()
print()
 

