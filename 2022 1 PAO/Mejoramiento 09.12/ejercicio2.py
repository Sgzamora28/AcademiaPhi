##############################################################################################################
##############################################################################################################
import random as rd
def perteneceCategoria(palabra,categoria):
  categorias={"Transportes":["Automovil","Bicicleta","Autobus","Tranvia","Ferrocarril","Tren","Metro","Avion"
                             "Helicoptero","Avion","Carruaje","Lancha","Avioneta","Barco","Yate","Buque","Submario"],
              "Deportes":   ["Futbol","Tenis","Pingpong","Natacion","Boxeo","Apnea","Buceo","Baloncesto","Judo","Jiujitsu",
                             "Golf","Gimnasia","Volleyball","Waterpolo","Sumo","Karate","Croquet","Danza"],
              "Alimentos":  ["Pera","Manzana","Sandia","Atun","Sardina","Zapayo","Mango","Arroz","Pollo","Res",
                             "Bacalao","Ajo","Zanahoria","Yogurt","Trucha","Tomate","Semola","Requeson","Quinoa","Pistacho"]}

  if palabra in categorias[categoria]:
    return True
  
  return False


c=['Transportes','Alimentos','Deportes']
puntajes={'Transportes':{"a":9,"b":21,"c":7,"d":5,"e":27,"f":19,"g":13,"h":28,"i":15,"j":25,"k":12,"l":17,"m":21,"n":4,"o":20,"p":30,
                         "q":5,"r":5,"s":27,"t":16,"u":12,"v":26,"w":2,"x":15,"y":10,"z":5},
          'Deportes':   {"a":1,"b":25,"c":19,"d":10,"e":3,"f":26,"g":12,"h":11,"i":9,"j":2,"k":25,"l":1,"m":4,"n":5,"o":22,"p":27,
                         "q":22,"r":9,"s":21,"t":5,"u":22,"v":21,"w":28,"x":28,"y":22,"z":10},
          'Alimentos':  {"a":26,"b":3,"c":8,"d":11,"e":28,"f":29,"g":25,"h":2,"i":21,"j":2,"k":12,"l":27,"m":17,"n":29,"o":9,"p":26,
                         "q":12,"r":20,"s":8,"t":16,"u":28,"v":12,"w":19,"x":29,"y":28,"z":25}}
##############################################################################################################
##############################################################################################################


# Escriba un programa de Python que implemente un juego de adivinanzas de palabras.
# Considere que para su programa ya están definidas las siguientes variables y función:
# 1. Una lista C de las categorías para el juego.
# C = ['Transportes', 'Alimentos', 'Deportes', ...],
# 2. La función perteneceCategoria(palabra, categoria) que retorna True si palabra pertenece a la categoria,
# False en caso contrario.
# 3. El diccionario puntajes con el siguiente formato:
# puntajes = {'Transportes':{'a':10, 't':4, 'f':5, ...},
# 'Deportes': {'a':3, 'z':5, 't':10, ...},
# ... }
# Para la implementación del juego considere las siguientes reglas:
# 1. El jugador tiene cinco turnos para jugar
# 
# Para cada turno:
# 2. El programa selecciona aleatoriamente una categoría de la lista C
# 3. El programa le pide al jugador que ingrese una palabra para la categoría seleccionada en el paso 2
# 4. Si la palabra pertenece a la categoría dada y no ha sido ingresada en un turno anterior, calcule los puntos
# totales para la palabra. El puntaje de la palabra es la suma de los puntajes de cada una de sus letras. De
# acuerdo al diccionario puntajes, una letra tendrá puntajes distintos dependiendo de la categoría del paso 2.
# a. Si la palabra no cumple con las condiciones, el jugador no obtiene puntos en ese turno
# 5. En cada turno, muestre el puntaje obtenido para la palabra ingresada y el puntaje acumulado
# Al final de los cinco turnos:
# 6. El jugador habrá ganado si completa un mínimo de 500 puntos, muestre el mensaje correspondiente
# “Ganó” o “Perdió”.
jugadas=[]
puntaje=0
for i in range(5):
  print("Turno #0{}".format(i+1))
  aleatorio=rd.randrange(len(c))#indice aleatorio de la lista #(0,n-1)
  categoria=c[aleatorio]
  # print(categoria)
  palabra=input("Ingrese una palabra que pertezca al grupo de {}: ".format(categoria)).title()
  comprobacion=perteneceCategoria(palabra,categoria)

  p=0
  if comprobacion and palabra not in jugadas:
    for caracter in palabra.lower():
      p+=puntajes[categoria][caracter]
    puntaje+=p
    print("El puntaje obtenido para su palabra es:",p)


  else:
    print("La palabra no pertenece a la categoria o ya fue jugada")
  

  print("Usted tiene un total de {} punto(s)".format(puntaje))


if puntaje>=500:
  print("Gano")

else:
  print("Perdio")