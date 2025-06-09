import time
import random

# ? Función para medir el tiempo de ejecución de otra función
def time_total(func, args):
  inicio_tiempo =  time.perf_counter()  # Inicia el contador de tiempo
  func(*args)
  fin_tiempo =  time.perf_counter()  # Finaliza el contador de tiempo
  print(f"Tiempo de ejecución de {func.__name__}: {fin_tiempo - inicio_tiempo:.8f} segundos")
  
# ? GENERAR LISTAS DE DNI
def generate_random_list(size, start, end):
    return random.sample(range(start, end), size)

# ? Lista desordenada de 100.000 números aleatorios entre 1 y 100.000
lista_dni_desordenada = generate_random_list(10000, 1, 100001)

  
#! ---- ALGORITMOS DE ORDENAMIENTO ---- #!

# * El algoritmo de seleccion es un algoritmo de ordenamiento simple que divide la lista en dos partes: la parte ordenada y la parte desordenada. En cada iteración, encuentra el elemento más pequeño de la parte desordenada y lo mueve a la parte ordenada. Aunque es fácil de entender e implementar, no es eficiente para listas grandes debido a su complejidad O(n^2).
def ordenamiento_seleccion(lista):
    for i in range(len(lista)):
        min_index = i
        for j in range(i + 1, len(lista)):
            if lista[j] < lista[min_index]:
                min_index = j
        lista[i], lista[min_index] = lista[min_index], lista[i]
    return lista





#! ---- ALGORITMOS DE BÚSQUEDA ---- #!

# * Búsca elemento por elemento en una lista desordenada (búsqueda lineal)
# Ineficiente para listas grandes, pero simple de implementar.
def busqueda_lineal(lista, elemento):
    for i in range(len(lista)):
        if lista[i] == elemento:
            return i
    return -1
  
#*--------------------------------------------------------------
 
# * Búsca un elemento de la lista partiendola en dos y luego compara el elemento con el del medio.
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

#*--------------------------------------------------------------

# * Similar a la búsqueda binaria pero más eficiente en listas ordenadas uniformemente distribuidas.
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

#*--------------------------------------------------------------
  

#! ---- EJECUCIÓN DE LAS PRUEBAS ---- #!

# lista_ordenada = ordenamiento_seleccion(lista_dni_desordenada[:])
# print("Lista ordenada:", lista_ordenada[:10])

# time_total(ordenamiento_seleccion, [lista_dni_desordenada[:]])  # Mide el tiempo de ejecución del algoritmo de ordenamiento