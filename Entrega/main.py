import time
import random

# * Función para medir el tiempo de ejecución de otra función
def time_total(func, args):
  inicio_tiempo =  time.perf_counter()  # Inicia el contador de tiempo
  func(*args)
  fin_tiempo =  time.perf_counter()  # Finaliza el contador de tiempo
  print(f"Tiempo de ejecución de {func.__name__}: {fin_tiempo - inicio_tiempo:.8f} segundos")
  
#* GENERAR LISTAS DE DNI
def generate_random_list(size, start, end):
    return random.sample(range(start, end), size)

# * Lista desordenada de 10 millones de números aleatorios entre 1 y 10 millones
lista_dni_desordenada = generate_random_list(10000000, 1, 10000001)


#! ---- ALGORITMOS DE BÚSQUEDA ---- #!

#? Búsca elemento por elemento en una lista desordenada (búsqueda lineal)
# Ineficiente para listas grandes, pero simple de implementar.

def busqueda_lineal(lista, elemento):
    for i in range(len(lista)):
        if lista[i] == elemento:
            return i
    return -1
  
#? Búsca un elemento de la lista partiendola en dos y luego compara el elemento con el del medio.
# Requiere que la lista esté ordenada, pero es mucho más eficiente que la búsqueda lineal.

def busqueda_binaria(lista_ordenada, elemento):
  izquierda = 0
  derecha = len(lista_ordenada) - 1
  while izquierda <= derecha:
      medio = (izquierda + derecha) // 2
      if lista_ordenada[medio] == elemento:
          return medio
      elif lista_ordenada[medio] < elemento:
          izquierda = medio + 1
      else:
          derecha = medio - 1
  return -1


#? Similar a la búsqueda binaria pero más eficiente en listas ordenadas uniformemente distribuidas.
# Requiere que la lista esté ordenada y es más eficiente que la búsqueda binaria en ciertos casos.

def busqueda_interpolacion(lista_ordenada, elemento):
  izquierda = 0
  derecha = len(lista_ordenada) - 1
  while izquierda <= derecha and elemento >= lista_ordenada[izquierda] and elemento <= lista_ordenada[derecha]:
      if izquierda == derecha:
          if lista_ordenada[izquierda] == elemento:
              return izquierda
          return -1
        
      # Calcular posición estimada
      rango_indices = derecha - izquierda
      rango_valores = lista_ordenada[derecha] - lista_ordenada[izquierda]
      distancia_elemento = elemento - lista_ordenada[izquierda]
      
      # Proporción: ¿qué porcentaje del rango representa el elemento?
      proporcion = float(distancia_elemento) / rango_valores
      pos = izquierda + int(rango_indices * proporcion)
      
      if lista_ordenada[pos] == elemento:
          return pos
      if lista_ordenada[pos] < elemento:
          izquierda = pos + 1
      else:
          derecha = pos - 1
  return -1

  
  
  
  
  
  
#! ---- ALGORITMOS DE ORDENAMIENTO ---- #!



#! ---- EJECUCIÓN DE LAS PRUEBAS ---- #!