

import numpy as np
import json
import random
import statistics

valores = []
sueldo = [300000, 2.500000]
dato = statistics.mean(sueldo)
bajo = min(sueldo)
alto = max(sueldo)
descuento_salud = random.uniform(0.07)
descuento__afp = random.uniform(0.12)

sueldo_liquido = dato - (dato * descuento_salud) - (dato * descuento__afp)

def agregar_valor(valor):
    valores.append(valor)
    return calcular_mediana()

def calcular_promedio():
    return sum(valores) / len(valores)
                
def calcular_mediana():
    if len(valores) % 2 == 0:
        return (statistics.median(valores[len(valores)//2 - 1:len(valores)//2 + 1]))
    else:
        return statistics.median(valores)
    
matriz_disponibilidad = np.empty((50,6), dtype=object)

trabajadores = ["Juan Perez", "Maria Garcia", " Carlos Lopez", "Ana Martinez", "Pedro Rodriguez", "Laura Hernandez", " Miguel Sanchez", "Isabel Gomez", "Francisco Diaz", "Elena Fernandez"]

def cargar_datos():
    global trabajadores
    try:
        with open('trabajadores.json', 'r', encoding='utf-8') as file:
            trabajadores = [tuple(p) for p in json.load(file)]
        print("Datos cargados correctamente.")
    except IOError:
        print("El archivo no existe.")
    except json.JSONDecodeError:
        print("El archivo está vacío o contiene datos inválidos.")

def salir():
    with open('trabajdores.json', 'w', encoding='utf-8') as file:
        json.dump([list(p) for p in trabajadores], file)

def elergir_sueldo():
    global trabajadores
    for i in range(matriz_disponibilidad.shape[0]):
        for j in range(matriz_disponibilidad.shape[1]):
            if matriz_disponibilidad[i, j] is None:
                matriz_disponibilidad[i, j] = 1
                matriz_disponibilidad[i, j] = 1
                trabajador = (elergir_sueldo(), trabajadores[random.randint(0, len(trabajadores) - 1)][1], trabajadores[random.randint(0, len(trabajadores) - 1)][2], random.randint(18, 65), random.choice(["H", "M"]), trabajadores[random.randint(0, len(trabajadores) - 1)][3],)
                valores.append(trabajador[0])
                print(f"Nombre del empleado: {trabajador[1]}, Nombre del empleado: {trabajador[2]}, Apellido: {trabajador[3]}")
                return
               
def asignar_sueldos():
    global trabajadores
    for i in range(matriz_disponibilidad.shape[0]): 
        for j in range(matriz_disponibilidad.shape[1]): 
            if matriz_disponibilidad[i, j] is None:
                matriz_disponibilidad[i, j] = 1
                trabajador = (elergir_sueldo(), trabajadores[random.randint(0, len(trabajadores) - 1)][1], trabajadores[random.randint(0, len(trabajadores) - 1)][2], random.randint(18, 65), random.choice(["H", "M"]), trabajadores[random.randint(0, len(trabajadores) - 1)][3],)
                valores.append(trabajador[0])
                print(f"Nombre del empleado: {sueldo_base[1]} {descuento_salud[2]} {descuento_afp[3]} {sueldo_liquieod}")
                return
        

def clasificar_sueldos():
    print("--- Sueldos ---")
    for t in trabajadores:
        print(f"Sueldo: {t[0]}")
        print(f"Mediana: {calcular_mediana()}")
        print(f"Valor mínimo: {bajo}")
        print(f"Valor máximo: {alto}")
        print(f"Valor promedio: {statistics.mean(valores)}")

def reportar_de_sueldos():
    print("--- Reporte de sueldos ---")
    trabajador = input("Ingrese el nombre del trabajador: ")
    for t in trabajadores:
        if t[1] == trabajador:
            print(f"Sueldo: {t[0]}")
            break

def mostrar_estadisitica():
    print("--- Estadísticas ---")
    print(f"Trabajadores: {len(trabajadores)}")
    print(f"Valor mínimo: {bajo}")
    print(f"Valor máximo: {alto}")
    print(f"Desviación estándar: {statistics.stdev(valores)}")
    print(f"Valor promedio: {statistics.mean(valores)}")
    print(f"Valor máximo (sin el trabajador): {max(valores)}")
    print(f"Valor mínimo (sin el trabajador): {min(valores)}")

def salir():
    salir()
    print(f"Finalizando programa...Desarrollado por Jose Luis Medina, Rut: 13.731.386-3")

def menu():
    cargar_datos()
    print("--- Bienvenido al sistema de asignacion de sueldo ---")
    
    while True:
        print('--- Menú ---')
        print("1. Asignacion de sueldos")
        print("2. Clasificar sueldos")
        print("3. Ver estadisiticas")
        print("4. Reporte de sueldos")
        print("5. Salir del programa")
                
        op = input('\n'"Seleccione una opción: ")
        
        if op == "1":
            asignar_sueldos()
        elif op == "2":
            clasificar_sueldos()
        elif op == "3":
            mostrar_estadisitica()
        elif op == "4":
            reportar_de_sueldos()
        elif op == "5":
            salir()
            print(f"Finalizando programa...Desarrollado por Jose Luis Medina, Rut: 13.731.386-3")
            break
        else:
            print("Opción no válida. Intente nuevamente.")
menu()