import time
import random

# ? Función para medir el tiempo de ejecución de otra función
def time_total(func, args):
  inicio_tiempo =  time.perf_counter()  # Inicia el contador de tiempo
  funcion_a_ejecutar = func(*args)
  fin_tiempo =  time.perf_counter()  # Finaliza el contador de tiempo
  print(f"Tiempo de ejecución de {func.__name__}: {fin_tiempo - inicio_tiempo:.8f} segundos")
  return funcion_a_ejecutar
  
# ? GENERAR LISTAS DE DNI
def generate_random_list(size, start, end):
    return random.sample(range(start, end), size)

# ? Lista desordenada de 20.000 números aleatorios entre 1 y 20.000
lista_dni_desordenada = generate_random_list(20000, 1, 20001)

  
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

#*--------------------------------------------------------------

# * El algoritmo de quicksort es un algoritmo de ordenamiento eficiente que utiliza el enfoque de divide y vencerás. Selecciona un elemento como pivote y particiona la lista en dos sublistas: una con elementos menores que el pivote y otra con elementos mayores. Luego, aplica recursivamente el mismo proceso a las sublistas. Su complejidad promedio es O(n log n), lo que lo hace adecuado para listas grandes.
def ordenamiento_quicksort(lista):
    if len(lista) <= 1:
        return lista
    else:
        pivote = lista[len(lista) // 2]
        izquierda = [x for x in lista if x < pivote]
        medio = [x for x in lista if x == pivote]
        derecha = [x for x in lista if x > pivote]
        return ordenamiento_quicksort(izquierda) + medio + ordenamiento_quicksort(derecha)


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
  



#! ---- EJECUCIÓN DE LAS PRUEBAS ---- #!

def main():
  opcion = input('Seleccione una opción:\n1. Ordenamiento\n2. Búsqueda\n3. Salir\nOpción: ')
  if opcion == '1':
    ordenamiento_opcion = input("---- ORDENAMIENTO ---- \n1. Ordenamiento por selección\n2. Quicksort \n3. Salir \nOpción: ")
    
    if ordenamiento_opcion == '1':
      print( "Primeros 10 numeros para corroborar el orden: ", time_total(ordenamiento_seleccion, [lista_dni_desordenada[:]])[:10])  # Muestra los primeros 10 elementos de la lista ordenada
    elif ordenamiento_opcion == '2':
      print( "Primeros 10 numeros para corroborar el orden: ", time_total(ordenamiento_quicksort, [lista_dni_desordenada[:]])[:10])
    elif ordenamiento_opcion == '3':
      print("Saliendo del programa.")
      return
    else:
      main()  # Vuelve al menú principal

  elif opcion == '2':
    elemento = int(input("Ingrese el numero a buscar entre 1 y 20.000: "))
    
    busqueda_opcion = input("---- INGRESE EL ALGORITMO DE BÚSQUEDA QUE PREFIERA ---- \n1. Búsqueda lineal\n2. Búsqueda binaria\n3. Búsqueda por interpolación\n4. Salir\nOpción: ")
    
    if busqueda_opcion == '1':
      resultado = time_total(busqueda_lineal, [lista_dni_desordenada, elemento])
      print(f"Resultado de la búsqueda lineal: { 'no se encuentra el numero ' + str(elemento) if resultado == -1 else resultado }")
      
    elif busqueda_opcion == '2':
      lista_ordenada = ordenamiento_quicksort(lista_dni_desordenada[:])
      resultado = time_total(busqueda_binaria, [lista_ordenada, elemento])
      print(f"Resultado de la búsqueda binaria: {'no se encuentra el numero ' + str(elemento) if resultado == -1 else resultado}")
      
    elif busqueda_opcion == '3':
      lista_ordenada = ordenamiento_quicksort(lista_dni_desordenada[:])  
      resultado = time_total(busqueda_interpolacion, [lista_ordenada, elemento])
      print(f"Resultado de la búsqueda por interpolación: {'no se encuentra el numero ' + str(elemento) if resultado == -1 else resultado}")
    elif busqueda_opcion == '4':
      print("Saliendo del programa.")
      return
      
    else:
      main()
      
  elif opcion == '3':
    print("Saliendo del programa.")
    return
    
  else:
    main()
    
if __name__ == "__main__":
  main()
  
