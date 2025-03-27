import json, time, os
from funciones import escribircodigos, escribirgenero, leercodigos, leergenero, codigos, generos, añadir_genero, eliminar_genero, generosmain, paisesmain, añadir_artista
from menu import saludo, limpiar, menuprincipal
from funciones import *
from menu import *
saludo()
while True:
    op=menuprincipal()
    match op:
        case "1":
            print("Añadir artista")
            añadir_artista()
            
        case "2":
            generosmain()
        case "3":
            paisesmain()
        case "4":
            print("Saliendo...")
            break
        case _: print("Ingrese una opcion valida")