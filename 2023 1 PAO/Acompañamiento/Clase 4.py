##############################################
#Listas 
##############################################
#Nos permiten guardar datos heterogeneos
#son indexables (adminten indexacion y slicing)
#son mutables

lista=["Steven","Mecatronica",21,True]
#         0            1      2    3  ----> len()-1
#         -4          -3     -2   -1

# nombre=lista[0]
# carrera=lista[-3]
# edad=lista[2]
# isRegular=lista[3]
# copia_lista=lista[::-1]
# print(copia_lista)

# Desarrolle un programa que funcione como un adivinador de cartas. 
# Para esto, su programa contendrá una lista de nombres de cartas: “AS”, “1”, “2” … “Q”, “K”. 
# Primero, su programa seleccionará al azar una de las cartas de la lista. 
# Luego, su programa permitirá el ingreso de un nombre de carta para adivinar. 
# Finalmente, su programa mostrará sí adivinó el nombre de la carta o no, 
# mediante un mensaje que contenga True o False, según sea el caso.

# import random as rd
# cartas=['AS', 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K'] #14
# #         0   1  2  3  4  5  6  7  8  9  10  11    12   13
# carta=rd.choice(cartas)
# print(carta)
# usuario=input("Ingresa la carta que crees que salio: ").upper()
# #'1' ----> '1'
# resultado=str(carta)==usuario
# print("Adivinasta la carta?",resultado)
#Numeros aleatorios
#randint ---> randint(inicial,final)  ----> [inicial,final]
#ranrange---> ranrange(inicial,final) ----> [inicial,final)
#             ranrange(final)         ----> [   0   ,final)




# Dada la lista lista1= [8,9,10]. 
# Escriba las instrucciones que permitan ejecutar las siguientes acciones: 
# 1. Realice una copia de la lista lista1 que se aloje en la variable lista2.
# 2. En lista1, insertar como segundo elemento el valor de 17.
# 3. Añadir 4, 5, y 6 al final de la lista1.
# 4. Remover el primer elemento de la lista2.
# 5. Ordenar la lista lista2 de forma ascendente.
# 6. Buscar el segundo elemento de lista2 en lista1. Muestre en pantalla en qué índice lo encontró. 
# (ojo: el segundo elemento NO ESTÁ en el índice 2)

# lista1=[8,9,10]
# lista2=lista1.copy()
# lista1.insert(1,17)
# lista1=lista1+[4,5,6]
# print(lista1)
# lista2=lista2[1:]
# lista2.sort()
# print(lista2)
# elemento2=lista2[1]#10
# indice=lista1.index(elemento2)
# print(indice)


#Listas paralelas
#Conjunto de listas que contienenen datos relacionados
#Los elementos de estas listas estan relacionados por indices
#Todas tienen la misma longitud

nombres= ["Steven","Azucena","Fernando"]
carreras=["Mecatronica","Ocenografia","Electronica y Automatizacion"]
edades=  [21,19,20]
