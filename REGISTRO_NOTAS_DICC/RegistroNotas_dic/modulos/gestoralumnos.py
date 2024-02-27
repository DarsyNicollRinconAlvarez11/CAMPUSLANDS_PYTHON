from tabulate import tabulate
alumno = {}
def AddStudent(alumnos:dict):
    id = input('Ingrese el id : ')
    nombre = input('Ingrese el nombre : ')
    edad =int(input(f'Ingrese su edad de {nombre} : '))
    email = input(f'Ingrese el email {nombre}: ')
    alumno = {
        'id' : id ,
        'nombre' : nombre,
        'edad' : edad,
        'email' : email,
        'calificaciones' : {}
    }
    #coja dicc global(alumnos)... permite añadir y editar info
    #el primer parametro seria(str a zfill) o sea llave...alumno es el valor
    alumnos.update({id:alumno})
    print(alumnos)
    
def searchstudent(alumnos:dict):
    id = input('ingrese el numero de estudiante : ')
    data = alumnos.get(id,False) #el id es la llave 
    if (type(data) == dict): #type para saber la variable de que tipo es 
        print(data)
    elif ((type(data) == bool) and (data == False)):
        print('el estudiante no se encunetra registrado ')
        #get me devuelve su valor y su tipo
def listdata(alumnos:dict):
    info =[]
    for key,value in alumnos.items():
        info.append(value)
    print(tabulate(info,headers="keys",tablefmt='grid'))
def validatestudent(alumnos : dict,id)->bool:
    return bool(alumnos.get(id,''))

def delstudent(alumnos : dict):
    id = input('ingrese el numero de estudiante : ')
    if (validatestudent(alumnos,id)):
        alumnos.pop(id)
    else:
        print(f'el estudiante con id {id} no esta registrado')
def delbyname(alumnos : dict):
    nombre = input('ingrese el numero del estudiante: ')
    for llave,valor in alumnos.items():
        if (nombre in valor['nombre']):
            alumnos.pop(llave)
            break

def AddGrades(alumnos: dict):
    id_alumno = input("Ingrese el ID del alumno al que desea agregar las notas: ")
    alumno = alumnos.get(id_alumno)
    if alumno:
        # Solicitar las notas de parciales, quices y trabajos
        parciales = input("Ingrese las notas de parciales separadas por espacios: ").split()
        quices = input("Ingrese las notas de quices separadas por espacios: ").split()
        trabajos = input("Ingrese las notas de trabajos separadas por espacios: ").split()

        # Convertir las notas a tipo float
        parciales = [float(nota) for nota in parciales]
        quices = [float(nota) for nota in quices]
        trabajos = [float(nota) for nota in trabajos]

        # Actualizar las calificaciones del alumno
        alumno['calificaciones'] = {
            'parciales': parciales,
            'quices': quices,
            'trabajos': trabajos
        }
        print("Notas agregadas correctamente.")
    else:
        print("El alumno con el ID ingresado no existe.")
    print(alumno)
