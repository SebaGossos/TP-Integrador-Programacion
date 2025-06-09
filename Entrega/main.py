import time
import random

# * Función para medir el tiempo de ejecución de otra función
def time_total(func, args):
  inicio_tiempo =  time.perf_counter()  # Inicia el contador de tiempo
  func(*args)
  fin_tiempo =  time.perf_counter()  # Finaliza el contador de tiempo
  print(f"Tiempo de ejecución de la función: {fin_tiempo - inicio_tiempo:.6f} segundos")
  
  
#* GENERAR LISTAS DE DNI
def generate_random_list(size, start, end):
    return random.sample(range(start, end), size)

# * Lista desordenada de 10 millones de números aleatorios entre 1 y 10 millones
lista_dni_desordenada = generate_random_list(10000000, 1, 10000001)


#! ---- ALGORITMOS DE BÚSQUEDA ---- #!

#? Búsca elemento por elemento en una lista desordenada (búsqueda lineal)

def busqueda_lineal(lista, elemento):
    for i in range(len(lista)):
        if lista[i] == elemento:
            return i
    return -1
  
time_total(busqueda_lineal,[lista_dni_desordenada, 5000000])
  # Realiza la búsqueda lineal
  
  
  
  
  
  
#! ---- ALGORITMOS DE ORDENAMIENTO ---- #!



#! ---- EJECUCIÓN DE LAS PRUEBAS ---- #!