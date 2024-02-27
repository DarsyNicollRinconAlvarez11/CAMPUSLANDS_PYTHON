def AddEquipo(equipos: dict):
  while True:
      nombre = input('Ingrese el nombre del Equipo: ')
      resultEquipos = {
          'nombre': nombre,
          'PJ': 0,
          'PG': 0,
          'PP': 0,
          'PE': 0,
          'GF': 0,
          'GC': 0,
          'TP': 0
      } 
      equipos[nombre] = resultEquipos  # Usar directamente el nombre como clave
      
      

      op = input("Desea agregar un nuevo equipo. Cualquier letra(SI) o n(NO): ")
      if op.lower() == "":
        continue  # Volver al inicio del bucle para agregar otro equipo
      elif op.lower() == "n" or op.lower() == "N":
        break
  
def AddFecha(equipos: dict):
    titfecha = """
        +++++++++++++++++++++++++++++
        + REGISTRAR EN LIGA BETPLAY +
        +++++++++++++++++++++++++++++
    """
    print(titfecha) 
    
    local = input('Escriba el equipo Local: ')
    visitante = input('Escriba el equipo Visitante: ')
    golesLocal = int(input('Ingrese los goles del equipo Local: '))
    golesVisitante = int(input('Ingrese los goles del equipo Visitante: '))
    equipos[local]['PJ'] += 1
    equipos[visitante]['PJ'] += 1
    equipos[local]['GF'] += golesLocal
    equipos[local]['GC'] += golesVisitante
    equipos[visitante]['GF'] += golesVisitante
    equipos[visitante]['GC'] += golesLocal
    
    if golesLocal > golesVisitante:
        equipos[local]['PG'] += 1
        equipos[visitante]['PP'] += 1
        equipos[local]['TP'] += 3
        print(f' El ganador fue {local}')
    
    elif golesLocal < golesVisitante:
        equipos[visitante]['PG'] += 1
        equipos[local]['PP'] += 1
        equipos[visitante]['TP'] += 3
        print(f'El ganador fue , {visitante}')
    
    else:
        equipos[local]['PE'] += 1
        equipos[visitante]['PE'] += 1
        equipos[local]['TP'] += 1
        equipos[visitante]['TP'] += 1
        print(f'Hubo un empate entre {local} y {visitante}')


def ReportesEquipos(equipos: dict):
    titulo = """
    *****************************************
    *       REPORTES DE LIGA BETPLAY        *
    *****************************************
    """
  
    print(titulo)
  
    equipoMasGoles = ""
    maxGoles = 0
    equipoMasPuntos = ""
    maxPuntos = 0
    pGanados= ""
    masPartidosGanados = 0
    totalGoles = 0
    totalPartidos= 0
  
    for clave, valor in equipos.items():
        goles = valor['GF']
        puntos = valor['TP']
        partidos_ganados = valor['PG']
      
        # A. Equipo con más goles anotados: 
        if goles >= maxGoles:
            maxGoles = goles
            equipoMasGoles = clave
      
        # B. NOMBRE DEL EQUIPO QUE MAS PUNTOS TIENE
        if puntos >= maxPuntos:
            maxPuntos = puntos
            equipoMasPuntos= clave
      
        # C. NOMBRE DEL EQUIPO QUE MAS PARTIDOS GANO
        if partidos_ganados >= masPartidosGanados:
            masPartidosGanados = partidos_ganados
            pGanados= clave
      
        # D. TOTAL DE GOLES ANOTADOS POR TODOS LOS EQUIPOS
        totalGoles += goles
      
        # E. PROMEDIO DE GOLES ANOTADOS EN EL TORNEO
        totalPartidos += valor['PJ']
      
    # Imprimir resultados fuera del bucle
    print(f"A. El equipo que más goles anotó fue: {equipoMasGoles}")
    print(f"B. El equipo que más puntos tuvo fue: {equipoMasPuntos}")
    print(f"C. El equipo que más partidos ganó: {pGanados}")
    print(f"D. El total de goles anotados por todos los equipos fue: {totalGoles}")
    promedio_goles = totalGoles / totalPartidos if totalPartidos > 0 else 0
    print(f"E. El promedio de goles anotados en el torneo: {promedio_goles}")


  