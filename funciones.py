import json
import time
import os
from menu import generosmenu, paisesmenu
global generos, artistas, paises
def leercodigos():
    with open("codigos.json","r") as file:
        codigos=json.load(file)
    return codigos

def escribircodigos():
    with open("codigos.json","w") as file:
        json.dump(codigos, file)
#########
#####Funciones generos########
def leergenero():
    with open ("generos.json","r") as file:
        generos=json.load(file)
    return generos

def escribirgenero():
    with open ("generos.json", "w") as file:
        json.dump(generos, file, indent=4)

generos=leergenero()
codigos=leercodigos()

def añadir_genero():
    existe=False
    nombrege=input("Ingrese el nombre del genero: ").upper().capitalize()
    for gen in generos:
        if nombrege in gen.keys():
            existe=True
    if existe==True:print("El genero ingresado ya existe: ")
    else: 
        codigo="GEN"+str(codigos[0])
        generos[0][nombrege]=codigo
        escribirgenero()
        codigos[0]+=1
        escribircodigos()
        print(f"El genero se ha guardado correctamente con el codigo {codigo}")

def eliminar_genero():
    existe=False
    nombrege=input("Ingrese el nombre del genero: ").upper().capitalize()
    for gen in generos:
        if nombrege in gen.keys():
            existe=True
    if existe==False:print("El genero ingresado no existe: ")
    else: 
        generos[0].pop(nombrege)
        escribirgenero()
        print("El genero seleccionado ha sido eliminado correctamente")

def consular_genero():
    existe=False
    nombrege=input("Ingrese el nombre del genero: ").upper().capitalize()
    for gen in generos:
        if nombrege in gen.keys():
            existe=True
            print(f"El codigo del genero es {gen[nombrege]}")
    if existe==False: print("El genero que ingresò no existe")
        
def generosmain():
    while True:
        op=generosmenu()
        match op:
            case "1":añadir_genero()
            case "2":eliminar_genero()
            case "3":consular_genero()
            case "4":
                print("Volviendo")
                break
            case _: print("Ingrese una opcion valida")

######Funciones paises########

def leerpaises():
    with open ("paises.json","r") as file:
        paises=json.load(file)
    return paises

def escribirpaises():
    with open("paises.json","w") as file:
        json.dump(paises, file, indent=4)

paises=leerpaises()

def añadir_paises():
    existe=False
    nombrepa=input("Ingrese el nombre del pais: ").upper().capitalize()
    for pa in paises:
        if nombrepa in pa.keys():
            existe=True
    if existe==True:print("El pais ingresado ya existe")
    else: 
        codigoiso=(nombrepa[0:2]+str(codigos[1])).upper()
        codigoiso3=(nombrepa[0:3]+str(codigos[1])).upper()
        paises[0][nombrepa]=[codigoiso, codigoiso3]
        escribirpaises()
        codigos[1]+=1
        escribircodigos()
        print(f"El pais se ha guardado correctamente con los codigos {codigoiso}---{codigoiso3}")

def eliminar_paises():
    existe=False
    nombrepa=input("Ingrese el nombre del pais: ").upper().capitalize()
    for pa in paises:
        if nombrepa in pa.keys():
                existe=True
    if existe==False:print("El pais ingresado no existe")
    else: 
        paises[0].pop(nombrepa)
        escribirpaises()
        print("El pais seleccionado ha sido eliminado correctamente")

def consultar_pais():
    existe=False
    nombrepa=input("Ingrese el nombre del pais: ").upper().capitalize()
    for pa in paises:
        if nombrepa in pa.keys():
            existe=True
            print(f"Los codigos del pais son:")
            print("ISO           ISO3")
            for dato in pa[nombrepa]:
                print(dato,end="           ")
    if existe==False: print("El genero que ingresò no existe")

def paisesmain():
    while True:
        op=paisesmenu()
        match op:
            case "1": añadir_paises()
            case "2": eliminar_paises()
            case "3": consultar_pais()
            case "4":
                print("Saliendo")
                break
            case _: print("Ingrese una opcion valida")
#####Funciones artistas##########

def leerartistas():
    with open("artistas.json","r") as file:
        artistas=json.load(file)
    return artistas

def escribirartistas():
    with open ("artistas.json","w") as file:
        json.dump(artistas, file, indent=4)

artistas=leerartistas()


def añadir_artista():
    existe=False
    listageneros=[]
    nombreart=input("Ingrese nombre del artista: ")
    for artista in artistas:
        if nombreart in artista["Nombre del artista"]:
            existe=True
    if existe==False:
            paisor=input("Ingrese pais de origen: ")
        
            añocomienzo=input("Ingrese año en que comenzò: ")
            añoactivo=input("Ingrese año en que retomaron: ")
            ultimoaño=input("Ingrese ultimo año de actividad: ")
            while True:
                try:
                    primerdisco=int(input("Ingrese el año de lanzamiento de su primer disco: "))
                    break
                except: print("Ingrese un numero valido")
            while True:
                generoexiste=False
                op=input("Ingrese 1 para añadir genero, cualquie otra tecla para dejar de añadir: ")
                if op=="1":
                    genero=input("Ingrese el genero(s) musicales: ").capitalize()
                    for tema in generos:
                        for nombr, codigo in tema.items():
                            if nombr==genero:
                                cod=codigo
                                generoexiste=True
                                listageneros.append({genero:cod})
                                print("Genero añadido correctamente")
                    if generoexiste==False: print("El genero ingresado no existe")
                else: 
                    print("Generos añadidos")
                    break        
            unida=input("Ingrese unidades certificadas totales: ")
            ventasrec=input("Ingrese ventas reclamadas: ")
            while True:
                actividad=input("Ingrese 1 si esta actvo, 2 sino: ")
                if actividad=="1": 
                    activo=True
                    break
                elif actividad=="2":
                    activo=False
                    break
                else:print("Ingrese una opcion valida")
            artistas.append({"Nombre del artista":nombreart,
                            "Pais de origen":paisor,
                            "Anios de actividad":(f"{añocomienzo}\\/u{añoactivo}-{ultimoaño}"),
                            "Anio de lanzamiento primer disco":primerdisco,
                            "Genero":listageneros,
                            "Unidades Certificadas":unida,
                            "Ventas Reclamadas":ventasrec
                            })
            escribirartistas()
            print("Artista añadido correctamente")
    else: print("El artista ya existe")


