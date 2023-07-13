#Las librerias son paquetes de funciones
#Funciones de aletoridad ---> Libreria random
import random as rd


#Para escoger numeros aletorios

palabra="Fundamentos" #len---> longitud 11
#        012345678910
#SIEMPRE EL ULTIMO INDICE ES el len()-1
#Randint
# x=rd.randint(0,len(palabra)) #---> [0,11] 
# print(x)
#Ranrange
y=rd.randrange(len(palabra)) #---> [0,11) 
# print(y)

a1=palabra[y]
a2=rd.choice(palabra)
# print(a1)
# print(a2)


#Ejercicio 1
# Para esto, su programa contendrá una lista de nombres de cartas: 
# “AS”, “1”, “2” … “Q”, “K”. Primero, su programa seleccionará al azar una de las 
# cartas de la lista. Luego, su programa permitirá el ingreso de un nombre de 
# carta para adivinar. Finalmente, su programa mostrará sí adivinó el nombre de la carta o no, 
# mediante un mensaje que contenga True o False, según sea el caso.

# cartas=['AS', "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", 'J', 'Q', 'K']
# aletorio=rd.choice(cartas)
# print(aletorio)
# usuario=input("Que carta salio? ").upper()
# if aletorio==usuario:
#     respuesta="Usted escogio la carta correcta"
# else:
#     respuesta="Usted no escogio la carta correcta"
# print(respuesta)

# Simulador de lanzamiento de dados Escribir un programa que simule el lanzamiento 
# de cinco dados para un jugador. El programa deberá pedir al usuario que ingrese su nombre. 
# Luego, deberá generar los CINCO números aleatorios, donde cada número representará el 
# lanzamiento de un dado y será aleatorio entre 1 y 6. Luego, debe almacenar esos cinco números 
# en una lista. La salida del programa deberá indicar en que lanzamiento se obtuvo:
# • El número más alto.
# • El número más bajo.
# • El promedio de los números obtenidos.

# 5 numeros aletorios del 1 al 6

#sample 
#rage(1,7) ---> 1,2,3,4,5,6
#range(6) ----> 0,1,2,3,4,5
# lanzamientos=rd.sample(range(1,7),5)
# nombre=input("Ingrese su nombre: ")
# print("Hola {}, los dados dieron los siguientes numeros:\n{}".format(nombre,lanzamientos))
# minimo=min(lanzamientos)
# maximo=max(lanzamientos)
# promedio=sum(lanzamientos)/len(lanzamientos)
# print("El menor lanzamiento fue: {}\nEl mayor lanzamiento fue: {}".format(minimo,maximo))
# print("El promedio de los valores obtenidos es:",promedio)


#ESTRUCTURAS DE CONTROL

#Estructuras condicionales

#Dos opciones

# numero1=int(input("Ingrese el primer numero: "))
# numero2=int(input("Ingrese el segundo numero: "))
# opcion=int(input("Seleccione\n[1] Para sumar\n[2] Para restar\n[3] Para multiplicar\n"))

# if opcion==1:
#     print("Esto es una suma")
#     resultado=numero1+numero2

# else:
#     print("Esto es una resta")
#     resultado=numero1-numero2

# print(resultado)


#Mas de dos opciones
# resultado="sin modificar"
# if opcion==1:
#     print("Esto es una suma")
#     resultado=numero1+numero2

# elif opcion==2:
#     print("Esto es una resta")
#     resultado=numero1-numero2

# elif opcion==3:
#     print("Esto es una multiplicacion")
#     resultado=numero1*numero2

# else:
#     print("opcion no valida")

# print(resultado)

#PIEDRA PAPEL TIJERAS
jugadas=["piedra","papel","tijera"]
#Piedra>Tijera
#Tijera>Papel
#Papel>Piedra

cp1=rd.choice(jugadas)
cp2=rd.choice(jugadas)
print("El jugador 1 escogio",cp1)
print("El jugador 2 escogio",cp2)

if (cp1=="piedra" and cp2=="tijera") or (cp1=="tijera" and cp2=="papel") or (cp1=="papel" and cp2=="piedra"):
    print("Jugador 1 gana la partida")
elif (cp2=="piedra" and cp1=="tijera") or (cp2=="tijera" and cp1=="papel") or (cp2=="papel" and cp1=="piedra"):
    print("Jugador 2 gana la partida")
else:
    print("La partida fue empatada")