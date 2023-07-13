#################################
#Ejercicio 1
#################################

# #Usted tiene 3 listas que contienen la informacion de varios pokemons
# pokemons= ["omanyte","blastoise","venomoth","alakazam","vulpix","rapidash"]
# pa=[150,89,140,130,145,200]
# pd=[90,100,85,105,125,90]


# # Implemente un programa en Python que diseñe una “calculadora Pokémon” la cual, dada una lista con los nombres de los especímenes,
# # pida al usuario que ingrese el nombre del pokemon. Calcule sus puntos de combate (PC) con la siguiente fórmula:
# # PC= (PA+PD)*1.2
# # Muestre por pantalla el PC del pokemon

# usuario=input("Ingrese el nombre del pokemon: ")#alakazam
# indice=pokemons.index(usuario)#3

# pc=(pa[indice]+pd[indice])*1.2
# print("Los puntos de compate para",usuario,"son:",pc)


#################################
#Ejercicio 2
#################################

#Pida al usuario que ingrese los nombres de asignaturas separadas por comas y cree una lista con esas mismas asignaturas, por ejemplo

#ingreso= Calculo,Quimica General,Algebra
#lista= [Calculo, Quimica General, Algebra]

#split---> 

# ingreso=input("Ingrese las materias separadas por una coma (','): ")
# print(ingreso)
# lista=ingreso.split(",")
# print(lista)