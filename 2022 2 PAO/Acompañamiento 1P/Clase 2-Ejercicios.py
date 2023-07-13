##############################################################################################################################################
###############################################
#Ejercicio 1
###############################################
##############################################################################################################################################

import funciones_ej1 as ej1
# A usted lo ha contratado una clínica veterinaria para procesar datos que tienen en su sistema para poder graficarlos más tarde, 
# tranquilo/a, usted solo solo va a procesar los datos. Los datos que trabajar lucen algo parecido a los siguientes: 
nombres = ["Morty", "Venus", "Pikachu", "Piolin", "Chumi","Don Gato","Itadori","Pantera"] 
especie = ["Gato", "Perro", "Hamster", "Ave", "Tortuga","Gato","Gato","Gato"] 
peso = [4.6, 11.0, 0.04, 0.3, 1,5,4.2,4] 
edad = [4, 3, 1.5, 3, 2,5,2,2]

# Estas listas son paralelas. Es decir, todos los datos en el índice i en las cuatro listas pertenecen a la misma mascota.
# Nota: Todos estos son datos referenciales y no representan datos reales, usted no sabe los datos ni la longitud de las listas, 
# solo conoce el tipo de información guardada en cada una de ellas.



# Tema 1
# Implemente la función buscar_por_edades(edad_inferior, edad_superior, l_nombres, l_edades) que recibe dos edades 
# (puede asumir que siempre edad_inferior< edad_superior), una lista de con los nombres de las mascotas y una lista 
# con las edades de esas mascotas. La función retorna una lista con todos los nombres de los animales que estén dentro del rango de las edades.
# tema1=ej1.buscar(4,2,nombres,edad)
# print(tema1)


# Tema 2 
# En su programa principal, pídele al usuario que ingrese el nombre de una mascota y muestre toda la información relacionada a dicha mascota. 
# Verifique que el nombre de la mascota este dentro de la lista de nombres.

# usuario=input("Ingrese el nombre de una mascota: ").title() # MORTY ----> Morty
# #condicion correcta---> usuario in nombres

# #Verificacion
# ####################################################################################
# while not(usuario in nombres):
#   usuario=input("Ingrese un nombre dentro de los datos registrados: ").title()
# ####################################################################################

# indice=nombres.index(usuario) #----> index obitene el indice de una dato especifico dentro de la lista
# print("Para la mascota",usuario)
# print("Su edad es",edad[indice])
# print("Su especie es",especie[indice])
# print("Su peso es",peso[indice])


#Tema 3
# Pídele al usuario una especie, luego:
# •Muestre el promedio del peso de esa especie. 
# Recuerde que el promedio es la suma de varios valores dividido para la cantidad de valores sumados.
# •Imprima en pantalla los nombres de todas las mascotas de esa especie. Si la mascota tiene un peso mayor al promedio de la especie 
# encierre su nombre en *, si tiene un peso menor alpromedio encierre su nombre en - y si son iguales, encierre su nombre en !.

usuario=input("Ingrese el nombre de una especie: ").title()
suma=0
for i in range(len(nombres)):
  if especie[i]==usuario:
    suma+=peso[i]

promedio=suma/especie.count(usuario) #---> count me cuenta la cantidad de veces que se repite un valor en una lista

for i in range(len(edad)):
  if especie[i]==usuario:
    if peso[i]>promedio:
      print("*{}*".format(nombres[i])) #----> *Piolin*
    
    elif peso[i]<promedio:
      print("-{}-".format(nombres[i])) #----> -Piolin-

    else:
      print("!{}!".format(nombres[i])) #----> !Piolin!



