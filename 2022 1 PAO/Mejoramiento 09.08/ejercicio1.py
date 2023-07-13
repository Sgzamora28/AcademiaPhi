import random as rd
# from random import *
# 4. Elabore un programa en Python que realice el Juego a continuación: (30 puntos)
# • Cruzar el camino:
# o El camino se cruza avanzando 5 pasos, los pasos serán realizados por medio de la generación de un número aleatorio entre 1 y 3.
# o Con cada número aleatorio se avanza en el camino, pero si el número pasa el tamaño del camino se regresa los pasos que le sobre.
# o Se generar hasta 4 números aleatorios para tratar que se cruce el camino.
# o Si cruza el camino de forma exacta, deja de generar los números aleatorios y le indica al usuario que se logró cruzar el camino
# o Si se generaron los 4 números aleatorios y no lograr el camino, se le indica que no logró pasar el camino.
# • Consideraciones:
# o Al inicio se muestra al usuario de bienvenida, nombre del juego. Indicando las instrucciones.
# o Para iniciar el juego le pedirá que ingrese un carácter y se genera el primer número aleatorio si se muestra el avance
# o Para generar cada número aleatorio se seguirá pidiendo que deban ingresa un carácter. 
# (Se repite hasta que gane o se generen los 5 números aleatorios).


print("Juego: Cruzar el camino")
print("Instrucciones:\no El camino se cruza avanzando 5 pasos, los pasos serán realizados por medio de la generación de un número aleatorio entre 1 y 3.")
print("o Con cada número aleatorio se avanza en el camino, pero si el número pasa el tamaño del camino se regresa los pasos que le sobre.") 
print("o Se generar hasta 4 números aleatorios para tratar que se cruce el camino.") 
print("o Si cruza el camino de forma exacta, deja de generar los números aleatorios y le indica al usuario que se logró cruzar el camino") 
print("o Si se generaron los 4 números aleatorios y no lograr el camino, se le indica que no logró pasar el camino.\n")

print("o _ _ _ _ _")

posicion=0
intentos=4
#condiciones del game over---> intentos==0 or posicion==5
#intentos!=0 and posicion!=5
while not(intentos==0 or posicion==6):
  camino=["_"]*7 #['-','-','-','-','-','-']--->len()=7 i=6
  jugador=input("Ingrese su ficha: ")
  movimiento=rd.randint(1,3)
  posicion+=movimiento
  if posicion>6:
    retroceso=posicion-6 #excedente de pasos
    print("El sistema genero {} paso(s) y regreso {} posicion(es)".format(movimiento,retroceso))
    posicion=6-retroceso
  else:
    print("El sistema genero {} pasos(s)".format(movimiento))

  camino[posicion]=jugador
  print("Camino"+" ".join(camino))

  intentos-=1

  if posicion==6:
    print("Lograstes cruzar el camino")

  else:
    print("Siguelo intentando")

  if intentos==0:
    print("Game Over. No lograste cruzar el camino")
  