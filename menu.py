import time
import os

def limpiar():
    os.system('cls' if os.name=='nt' else 'clear')

def saludo():
    print("="*50)
    print(" "*20,"Limeware")
    print("="*50)
    print("Bienvenido al sistema de artistas")
    time.sleep(1)
    print("Cargando sistema...")
    time.sleep(2)
    print("Sistema cargado correctamente")
    time.sleep(2)
    limpiar()

def menuprincipal():
    menupr="""
    *******Menu Principal*******
    1.Artistas
    2.Generos
    3.Paises
    4.Salir
    """
    print(menupr)
    return input("Ingrese una opciòn: ")

def generosmenu():
    menugen="""
    *****Generos******
    1.Añadir genero
    2.Eliminar genero
    3.Consultar codigo genero
    4.Salir
    """
    print(menugen)
    return input("Ingrese una opcion: ")

def paisesmenu():
    menupai="""
    ******Paises*******
    1.Añadir pais
    2.Eliminar pais
    3.Consultar codigos pais
    4.Salir
    """
    print(menupai)
    return input("Ingrese una opcion: ")

def artistasmenu():
    menuart="""
    ******Artistas*****
    1.Añadir artista
    2.Eliminar artista
    3.Consultar artistas
    4.Salir
    """
    print(menuart)
    return input("Ingrese una opcion: ")

