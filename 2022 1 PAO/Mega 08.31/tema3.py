# a. Implemente una función buscar(listaAnidada, valor) que recibe una lista de listas y retorna verdadero o falso si valor existe en listaAnidada. 
# (2.5 puntos)

def buscar(anidada,valor):
  for nivel1 in anidada:
    for nivel2 in nivel1:
      if valor==nivel2:
        return True

  return False

# b. Utilice la función buscar del literal a para determinar si el valor X existe en la lista anidada L y mostrar por pantalla ‘Valor si existe’ o ‘Valor no existe’. (2.5 puntos)
L = [[3, 2, 5], [1], [7, 9]]
# X = int(input("Ingrese valor por teclado: "))

# comprobacion=buscar(L,X)
# if comprobacion:
#   print("Valor si existe")

# else:
#   print("Valor no existe")
# #su código aquí



# c. Implemente una función que sume o multiplique valores enteros almacenados en una lista anidada. Si se invoca a la función únicamente con la lista como argumento, 
# la función debe retornar la suma de los valores. Si se invoca a la función con un segundo argumento con valor ‘multiplicar’, 
# la función debe retornar la multiplicación de los valores. Para cualquier otro valor para el segundo argumento, la función deberá retornar -1. (5 puntos)


def calcular(anidada,operacion="suma"):
  x=0
  for nivel1 in anidada:
    for nivel2 in nivel1:
      if operacion=="suma":
        x+=nivel2

      elif operacion=="multiplicar":
        if x==0:
          x+=1
        x*=nivel2

      else:
        return -1

  return x

print(calcular(L,"multiplicar"))