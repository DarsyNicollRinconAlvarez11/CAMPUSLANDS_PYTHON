import menu as m # m de menu
import equipos as e
equipos = {}
opcion = 0

while(True):
  opcion = m.CrearMenu()
  if opcion == 1:
    e.AddEquipo(equipos)
  elif opcion == 2:
    e.AddFecha(equipos)
  elif opcion == 3:
    e.ReportesEquipos(equipos)
  elif opcion == 4:
    print("Saliendo del programa...")
    break
