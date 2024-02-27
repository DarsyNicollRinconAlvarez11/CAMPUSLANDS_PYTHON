import menus as m
# Lista para almacenar los equipos
equipos = []
# FUNCION PARA CREAR EQUIPOS 
def crear_equipos():
    valEquipo = True
    while valEquipo:
        
        nombre = input('Ingrese el nombre del equipo que desea registrar : ')
        equipos.append([nombre,0,0,0,0,0,0,0])
        valEquipo=input('Desea ingresar otro equipos SI(S)o no (ENTER)')
#"
# PJ= Partidos Jugados
# PG= Partidos Ganados
# PP= Partidos Perdidos
# PE= Partidos Empatados
# GF= Goles Favorables
# GC= Goles Contra
# TP= Total Puntos 
# "
# FUNCION PARA LAS FECHAS DE LOS PARTIDOS 
def registrar_fechas(local, visitante, goles_local, goles_visitante):
    for equipo in equipos:
        if equipo[0] == local:
            equipo[1] += 1  
            equipo[5] += goles_local  
            equipo[6] += goles_visitante 
            if goles_local > goles_visitante:
                equipo[2] += 1  
                equipo[7] += 3  
            elif goles_local < goles_visitante:
                equipo[3] += 1  
            else:
                equipo[4] += 1  

    # Actualizamos los datos del equipo visitante de manera similar
    for equipo in equipos:
        if equipo[0] == visitante:
            equipo[1] += 1
            equipo[5] += goles_visitante
            equipo[6] += goles_local
            if goles_visitante > goles_local:
                equipo[2] += 1
                equipo[7] += 3
            elif goles_visitante < goles_local:
                equipo[3] += 1
            else:
                equipo[4] += 1
# REPORTES
def reportes():
    print(m.menu_reportes)
    while True:
        
        opci = input("Seleccione una opción: ")
        if opci == "1":
            max_goles = max(equipo[5] for equipo in equipos)
            equipo_max_goles = [equipo[0] for equipo in equipos if equipo[5] == max_goles]
            print("Equipo con más goles:", equipo_max_goles)
        elif opci == "2":
            max_puntos = max(equipo[7] for equipo in equipos)
            equipo_max_puntos = [equipo[0] for equipo in equipos if equipo[7] == max_puntos]
            print("Equipo con más puntos:", equipo_max_puntos)
        elif opci == "3":
            #print(f.equipos)  
            partidos_ganados = max(equipo[2] for equipo in equipos)
            equipos_max_ganados = [equipo[0] for equipo in equipos if equipo[2] == partidos_ganados]
            print("Equipo con más partidos ganados:", equipos_max_ganados)
        elif opci == "4":
            total_goles = sum(equipo[5] for equipo in equipos)
            print("Total de goles anotados por todos los equipos:", total_goles)
        elif opci == "5":
            total_partidos = sum(equipo[1] for equipo in equipos)
            promedio_goles = total_goles / total_partidos if total_partidos > 0 else 0
            print("Promedio de goles anotados en el torneo:", promedio_goles)
        elif opci == "6":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")
