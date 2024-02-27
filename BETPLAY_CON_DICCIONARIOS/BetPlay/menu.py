import os

def CrearMenu():
    opc = {
        1: "Agregar equipo",
        2: "Registrar Fecha",
        3: "Reportes",
        4: "Salir"

    }


    titulo = """
        ++++++++++++++++++++++++++++
        +   LIGA BETPLAY MENU      +
        ++++++++++++++++++++++++++++
    """
    print(titulo)
    try:
        opciones = "1. Agregar equipo\n2. Registrar Fecha\n3. Reportes\n4. Salir"
        print(opciones)
        op =int(input('Seleccione una opción :)  '))
        if (op not in opc):
            CrearMenu()
    except ValueError:
        print('Dato invalido')
        CrearMenu()
    else:
        return op