import sys
from os import system 
ciudades = []

def nuevaCiudad():
    while len(ciudades) < 5:
        nombre = str(input("Ingresa el nombre de la ciudad: ")).lower()
        ciudades.append([nombre, [], 0.0])
        print("Ciudad creada correctamente")
        opcion = input("¿Desea ingresar otra ciudad? Si(s) / No(Enter): ").lower()
        if opcion.lower() != "s":
            break
    if len(ciudades) ==5:
        print("Lo siento, alcanzó el límite máximo para registrar ciudades (5).")
        system("pause")

def nuevoSismo(ciudad):
    sismo = float(input(f"Ingrese la magnitud del sismo para la ciudad {ciudad[0]}: "))
    ciudad[1].append(sismo)
    cantidad_sismos = len(ciudad[1])
    riesgo = sum(ciudad[1]) / cantidad_sismos
    ciudad[2] = riesgo
    cant_sismo(cantidad_sismos)

def cant_sismo(cantidad_sismos):
    for ciudad in ciudades:
        sismos = len(ciudad[1])
        if sismos < cantidad_sismos:
            print("La cantidad de sismos entre ciudades no coincide, por favor.")
            nuevoSismo(ciudad)

def buscarCiudad():
    nombre = input("Ingresa el nombre de la ciudad: ")
    for ciudad in ciudades:
        if nombre == ciudad[0]:
            return ciudad
    print("Ciudad no encontrada")



def borrarPant():
    if sys.platform == "linux" or sys.platform == "darwin" :
       system("clear")
    else:
      system("cls")

def paussPant():
    if sys.platform == "linux" or sys.platform == "darwin":
        input('Enter para continuar...')
    else: 
        system("pause")