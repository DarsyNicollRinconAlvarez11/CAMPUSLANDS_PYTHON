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

if __name__ == '__main__':
  pass
listNumbers  = []
pares = 0
menorA10= 0
numEntre = 0
mayorA100 = 0

titulo = """
          BIENVENID@
  ++++++++++++++++++++++++++++
  |     NUMEROS ENTEROS      |
  |        POSITIVOS         |
  ++++++++++++++++++++++++++++
"""
print(titulo)
while (True):
      try:
        num= int(input("Ingrese un numero (0 para terminar) \n :> "))
        if (num > 0):
            listNumbers.append(num)
            if(num % 2 == 0):
                pares += 1
            if(num > 100):
                mayorA100 += 1
            if(num < 10):
                menorA10 += 1
            if(num > 20) and (num < 50):
              numEntre += 1
      except ValueError:
          print("ERROR: Dato ingresado invalido. Solo numeros enteros positivos.  \n :> ")
      else:
        if (num <= 0):
            paussPant()
            borrarPant()
            print("ERROR: \n :> ")
           
            print("""
                     +++++++++++++++++++++++++++++
                     |     REPORTE DE NUMEROS    | 
                     |      ENTEROS POSITIVOS    |
                     +++++++++++++++++++++++++++++
                  """)
            cantNum = len(listNumbers)
            print(f" La cantidad de números ingresados es : {cantNum}")
          
            print(f" La cantidad de números pares ingresados es : {pares}")
            promedio = (pares / cantNum) * 100 if cantNum > 0 else 0
            print(f" El promedio de numeros pares es: {promedio:.2f}% ")
            print(f" El promedio de numeros impares es: {100 - promedio:.2f}%")
            print(f" La cantidad de números que son menores a 10 son: {menorA10} ")
            print(f" La cantidad de números están entre 20 y 50 son: {numEntre} ")
            print(f" La cantidad de números que son mayores a 100 son: {mayorA100} ")
            break
