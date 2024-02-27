import menus as m
import funciones as f
if __name__=='__main__':
    pass


while True:
    print(m.menu_principal)
    opci = input("Seleccione una opción: ")
    if opci == "1":
        f.crear_equipos()
    elif opci == "2":    
        print("""
          ********************************
          *   REGISTRO DE FECHAS 2024   *
          ********************************  
          """)  
        local = input("Ingrese cual fue el equipo local: ")
        visitante = input("Ingrese cual fue el equipo visitante: ")
        goles_local = int(input("Ingrese los goles que anoto el equipo local: "))
        goles_visitante = int(input("Ingrese los goles que anoto el equipo visitante: "))
        f.registrar_fechas(local, visitante, goles_local, goles_visitante)
    elif opci == "3":
        #print(f.equipos)   
        f.reportes()
    elif opci == "4":
        print("Saliendo del programa...")
        break
    else:
        print("Opción no válida. Por favor, seleccione una opción válida.")