
# TEMA 3
# Implemente la función buscar_par_descendente(l_numeros) que recibe una lista de números enteros. 
# La función debe encontrar el primer par de elementos adyacentes en
# la lista l_numeros que están en orden descendente y devuelve el índice del primer elemento del par. 
# Si no existe tal par, devuelve None
# Ejemplo:
# Para la lista [1,3,4,6,4,7,6], el retorno sería 3. 
# Para la lista [1,3,4,5,6,7,6], el retorno sería 5. 
# Para la lista [1,3,4,5,6,7,8], el retorno sería None.

def buscar(numeros:list[int]):#[1,3,4,6,4,7,6]
  for i in range(len(numeros)-1):
    if numeros[i]>numeros[i+1]:
      return i

#ejemplo
x=buscar([1,3,4,5,6,7,8])
# print(x)

# Luego, escriba un programa principal que genere una lista de 17 números aleatorios enteros entre 15 y 28 y 
# muestre el resultado de invocar a su función con esta lista.

#main
import random as rd

aleatorios=[]
for i in range(17):
  a=rd.randint(15,28)
  aleatorios.append(a)

print(aleatorios)
print(buscar(aleatorios))