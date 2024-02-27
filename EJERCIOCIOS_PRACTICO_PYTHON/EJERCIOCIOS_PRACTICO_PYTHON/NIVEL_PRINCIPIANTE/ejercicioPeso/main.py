import sys
from os import system 

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

def getRango_IMC(imc,reporte):
    if (imc >= 18.5) and (imc <= 24.9):
        reporte["peso_ideal"] += 1
        return "Normal"
    elif (imc >= 25) and (imc <= 29.9):
        reporte["sobrepeso"] += 1
        return "Sobrepeso"

    elif(imc >= 30) and (imc <= 34.9):
        reporte["obesidad_grado_1"] += 1
        return "Obesidad 1"

    elif(imc >= 35) and (imc <= 39.9):
        reporte["obesidad_grado_2"] += 1
        return "Obesidad 2"

    elif(imc >= 40):
        reporte["obesidad_grado_3"] += 1
        return "Obesidad 3"
#Diccionario donde se almacena el reporte de los estudiantes segun su IMC
reporte = {
    "peso_ideal": 0,
    "obesidad_grado_1": 0,
    "obesidad_grado_2": 0,
    "obesidad_grado_3": 0,
    "sobrepeso": 0
}
titulo = """
            BIENVENID@
    ++++++++++++++++++++++++++++
    |      CENTRO DE SALUD     |
    |      DE CAMPUSLANDS      |
    ++++++++++++++++++++++++++++

Ingrese los siguientes datos para calcular su IMC(indice de masa muscular)
"""
print(titulo)
estudiantes = []
for i in range(2):
  while True:
    try:
        nombre = input("Ingresa el Nombre del Estudiante \n :> ")
        edad = input(f"Ingrese la edad de {nombre} \n :>")
        peso = float(input("Ingresa el Peso en KG \n :> "))
        altura = float(input("Ingresa la Altura en Metros \n :> "))
        imc = round(peso / (altura * altura), 1)
        imcRango = getRango_IMC(imc, reporte)
        estudiante = {
            "nombre": nombre,
            "edad": f"{edad} años",
            "peso": f"{peso} Kilogramos",
            "altura": f"{altura} metros",
            "imc": imc,
            "rango": imcRango
        }

        for key, value in (estudiante.items()):
                print(f"{key} : {value}")

        estudiantes.append(estudiante)
        paussPant()
        borrarPant()
    except ValueError:
        print("Error Al Ingresar un dato")
    else:
        break



#Punto 2
print(f"""
a. Se encuentran en el peso ideal {reporte['peso_ideal']} Estudiantes
b. Se encuentran en obesidad grado I {reporte['obesidad_grado_1']} Estudiantes
c. Se encuentran en obesidad grado II {reporte['obesidad_grado_2']} Estudiantes
d. Se encuentran en obesidad grado III {reporte['obesidad_grado_3']} Estudiantes
e. Se encuentran en Sobrepeso {reporte['sobrepeso']} Estudiantes
""")