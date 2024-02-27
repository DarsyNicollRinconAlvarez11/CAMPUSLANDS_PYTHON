import menus as m 
import funciones as f 
if __name__ == '__main__':
  pass

while True:
    f.borrarPant()
    print(m.titulo)
    print(m.menuPrin)
    opMenu = input(":> ")

    if opMenu == "1":
         f.nuevaCiudad()
    elif opMenu == "2":
        ciudad = f.buscarCiudad()
        if ciudad:
            f.nuevoSismo(ciudad)
    elif opMenu == "3":
        ciudad = f.buscarCiudad()
        if ciudad:
            print(f"Lista de Sismos de {ciudad[0]}: {ciudad[1]}")
            f.paussPant()
        else: 
            print ("Ciudad no encontrada")
            f.paussPant()
    elif opMenu == "4":
        for ciudad in f.ciudades:
            rango = ciudad[2]
            if rango <= 2.5:
                print(f"{ciudad[0]}: Amarillo (Sin riesgo)")
            if rango >= 2.6 and rango <= 4.5:
                print(f"{ciudad[0]}: Naranja (Riesgo medio)")
            if rango > 4.5:
                print(f"{ciudad[0]}: Rojo (Riesgo alto)")
        f.paussPant()
    elif opMenu == "5":
        break
    else:
        print("Opción no reconocida")