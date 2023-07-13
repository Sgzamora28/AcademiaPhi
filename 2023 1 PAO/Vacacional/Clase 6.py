########################################################
########################################################
             #ESTRUCTURAS ITERATIVAS#
########################################################
########################################################
#ESTRUCTURA DEL FOR
#for [variable] in [objeto iterable]
# for letra in "palabra":
#     print(letra)

#Objetos iterables ---> objeto que se puede dividir en partes pequenias
#rango ---> range(10) [0,10) / range(1,10) [1,10)
#str
#listas
#todas las colecciones


#Programa que simule una tabla de multiplicar del 1 al 10. El usuario ingresa el numero de la
#tabla a mostrarse
# for i in range(10): #[0,10)
#     x=i+1
#     print("{}x{}={}".format(numero,x,x*numero))


########################################################
#EJERCICIO 1#
########################################################

# La lista mostrrada en el ejemplo contiene los URLs de diferentes sitios Web que han 
# sido visitados.
lista = ["www.espol.edu.ec","www.google.com","www.sri.gob.ec","www.fiec.espol.edu.ec","www.uess.edu.ec", 
  "www.FIEC.espol.edu.ec","www.fict.espol.edu.ec","www.fcnm.Espol.edu.ec","www.ucsg.edu.ec",
  "www.Stanford.edu","www.harvard.edu","www.stanford.edu","www.UCSG.edu.ec","www.google.com.ec",
  "www.facebook.com","www.opensource.org","www.educacionbc.edu.mx"]
# Los URLs normalmente se repiten y corresponden algunas veces a universidades de Ecuador y 
# otros países.
# Note que los URLs no diferencian entre mayúsculas y minúsculas.
# Por ejemplo: www.espol.edu.ec y www.ESPOL.edu.ec corresponden al mismo sitio.
# Escriba un programa en Python que dada una lista realice lo siguiente:

# a. Muestre los nombres o siglas de las universidades que aparecen en la lista (sin repetir).
universidades=[]
for url in lista:
    # print(url)
    if ".edu" in url:
        datos=url.split(".")
        #                0       1       2       3      4
        # print(datos) #['www', 'fiec', 'espol', 'edu', 'ec']
                       #['www', 'UCSG', 'edu', 'ec']
                       #   0       1      2      3
        indice=datos.index("edu")-1
        universidad=datos[indice].upper()
        # print(universidad)
        if universidad not in universidades:
            universidades.append(universidad)
# print(universidades)
# b. Muestre la cantidad y los nombres/siglas de universidades de Ecuador que aparecen en la lista.
uEcuador=[]
for url in lista:
    if ".edu" in url and ".ec" in url:
        datos=url.split(".")
        indice=datos.index("edu")-1
        universidad=datos[indice].upper()
        if universidad not in uEcuador:
            uEcuador.append(universidad)
    
# print("Hay {} universidades en Ecuador. Estas son: ".format(len(uEcuador)))
#FOR POR CONTENIDO
#for [variable] in [objeto ibterable]
# for uni in uEcuador:
#     print(uni)

#FOR POR INDICE
#Cuando nos interesa el indice de los elementos del objeto iterable
#Cuando queremos reordear un elemento iterable
#Cuando tenemos listas paralelas

#for [i] in range(len(el objeto iterable))
# for i in range(len(uEcuador)):
#     print("{}. {}".format(i+1,uEcuador[i]))

# c. Dado un usuario y el nombre o sigla de la universidad, imprima el correo electrónico asignado.
#nickname@universidad.edu.ec
# nickname=input("Ingrese su usuario: ").lower()
# u=input("Ingrese su universidad: ").lower()
# print("{}@{}.edu.ec".format(nickname,u))

########################################################
#EJERCICIO 2
########################################################
# Implementar un programa en Python que calcule el puntaje de las películas contenidas en 
# la lista de películas para determinar la mejor: (6 puntos)
films = ["wonder woman", "la bella y la bestia", "harry potter", "star wars", 
"superman", "el señor de los anillos"]
# El programa pide al usuario que ingrese sus puntos en música (M), libreto (L) y 
# efectos especiales (E) de cada película. Los puntos deberán estar 
# dados por valores entre 0 y 10, lo que permitirá realizar la conversión a estrellas 
# posteriormente. El programa debe calcular los puntos de la película (PP) a 
# través de la siguiente fórmula:
# PP = 0.3*L + 0.5*M + 0.2*E
# El programa muestra por pantalla los puntos por película (PP) y el nombre 
# de la película con mayor puntaje 

puntos=[]
for pelicula in films:
    print(pelicula.title())
    print("Para cada parametro, ingrese un puntaje del 0 al 10")
    m=int(input("Ingrese el puntaje para la banda sonora: "))
    l=int(input("Ingrese el puntaje para el libreto: "))
    e=int(input("Ingrese el puntaje para efectos especiales: "))
    print()
    pp=0.3*l+0.5*m+0.2*e
    puntos.append(pp)

mayor=max(puntos) #aqui obtengo el puntaje mayor
indice_mayor=puntos.index(mayor) #aqui obtengo el indice del puntaje mayor
pelicula_ganadora=films[indice_mayor]
print("La pelicula {} con un puntaje de {:.2f} es la mejor puntuada".format(pelicula_ganadora,mayor))

#LISTAS PARALELAS
#Listas relacionadas por el indice
#Comparten longitud