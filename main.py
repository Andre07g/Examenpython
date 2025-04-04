import json, time, os
from funciones import escribircodigos, escribirgenero, leercodigos, leergenero, codigos, generos, añadir_genero, eliminar_genero, generosmain, paisesmain, añadir_artista, editar_artista, eliminar_artista
from menu import saludo, limpiar, menuprincipal, artistasmenu
from funciones import *
from menu import *
saludo()
while True:
    op=menuprincipal()
    match op:
        case "1":
            limpiar()
            artistas_main()
        case "2":
            limpiar()
            generosmain()
        case "3":
            limpiar()
            paisesmain()
        case "4":
            print("Saliendo...")
            break
        case _: 
            limpiar()
            print("Ingrese una opcion valida")