# El juego de mesa Scrabble es un juego donde se forman palabras en un tablero, a las cuales se les
# asigna un puntaje. Las palabras pueden crearse cruzándolas con palabras ya existentes en el tablero. El
# ganador es quien más puntos haya obtenido:

# A su equipo se le ha encargado la implementación de este juego. En particular, tiene que implementar un
# programa que asigne puntaje a las palabras​. Cada letra tiene una puntuación, mostrada abajo:



letras=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
puntos=[1,3,3,2,1,4,2,4,1,9,5,1,3,1,1,3,10,1,1,1,1,4,4,9,4,10]



#"CAS*A*,S*ASTR*E*,R*EY*,A*ZOTE*"

# Las letras compartidas entre palabras reciben el doble de puntos​. Su programa recibirá una secuencia
# de palabras, separadas por comas​, ingresada por el usuario por teclado y determinará el puntaje de
# cada una. Para denotar una letra compartida, la misma será sucedida por el símbolo “*”. ​Asuma que
# todas las palabras terminan con una letra compartida​. 
# Todas las letras ingresadas deben ser
# mayúsculas. Si se ingresa un letra minúscula, esta es ignorada (puntuación de 0 para dicha letra)​.
# Finalmente, se debe determinar/mostrar la palabra con mayor puntaje.

usuario=input("Ingrese las palabaras a verificar, recuerde separarlas por comas: ")
#condicion---> usuario.count(",")>=1
secuencia=usuario.split(",")#["CAS*A*","S*ASTR*E*","R*EY*","A*ZOTE*"]
puntajes=[]#---> paralela a secuencia
for palabra in secuencia:#"CAS*A*"
  puntaje=0
  for i in range(len(palabra)):
    letra=palabra[i]
    if letra.isupper() and letra!="*":#"C"
      x=letras.index(letra)#2
      p=puntos[x]

      if palabra[i+1]=="*":
        p*=2

      puntaje+=p

  puntajes.append(puntaje)

maximo=max(puntajes)#---> se puede usar max solo para listas de numeros
i_maximo=puntajes.index(maximo)
ganador=secuencia[i_maximo]#"CAS*A*"
g=ganador.replace("*","").lower()
print(g)

    

