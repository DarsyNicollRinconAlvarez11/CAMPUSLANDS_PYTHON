if __name__ == '__main__':
  pass

listNumbers  = []
suma = 0

while (len(listNumbers) < 3):
    try:
        numero = int(input("Ingresa un Numero Positivo \n :> "))
    except ValueError:
        print("Solo números enteros positivos. \n :>")
    else:
        #Comprobacion si es positivo
        if (numero >= 0):
            suma += numero
            listNumbers.append(numero)
        else:
            print("Solo números enteros positivos. \n :>")
print("La suma de los numeros es \n :> ", suma)
