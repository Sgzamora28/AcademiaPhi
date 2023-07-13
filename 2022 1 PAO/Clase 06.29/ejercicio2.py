# El juego de mesa Scrabble es un juego donde se forman palabras en un tablero, a las cuales se les
# asigna un puntaje. Las palabras pueden crearse cruzándolas con palabras ya existentes en el tablero. El
# ganador es quien más puntos haya obtenido:

# A su equipo se le ha encargado la implementación de este juego. En particular, tiene que implementar un
# programa que asigne puntaje a las palabras​. Cada letra tiene una puntuación, mostrada abajo:

letras=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
puntos=[1,3,3,2,1,4,2,4,1,9,5,1,3,1,1,3,10,1,1,1,1,4,4,9,4,10]


# Las letras compartidas entre palabras reciben el doble de puntos​. Su programa recibirá una secuencia
# de palabras, separadas por comas​, ingresada por el usuario por teclado y determinará el puntaje de
# cada una. Para denotar una letra compartida, la misma será sucedida por el símbolo “*”. ​Asuma que
# todas las palabras terminan con una letra compartida​. 
# Todas las letras ingresadas deben ser
# mayúsculas. Si se ingresa un letra minúscula, esta es ignorada (puntuación de 0 para dicha letra)​.
# Finalmente, se debe determinar la palabra con mayor puntaje.

#CAS*A*,S*ASTR*E*,R*EY*,A*ZOTE*
usuario=input('Ingrese las palabras a calificar, recuerde separlas por comas: ')
secuencia=usuario.split(',')
verificadas=[]
puntuacion=[]
for palabra in secuencia:#CAS*A*
  puntaje=0
  cadena=''
  for i in range(len(palabra)-1):
    letra=palabra[i]
    if letra.isupper() and letra!='*':
      x=letras.index(letra)
      p=puntos[x]
      cadena+=letra.lower()
      if palabra[i+1]=='*':
        p*=2
      puntaje+=p
  puntuacion.append(puntaje)
  # palabra=palabra.replace('*','')#solo si tenemos la certeza de lo que vamos a reemplazar
  verificadas.append(cadena)


print(verificadas)
print(puntuacion)

mayor=max(puntuacion)
i_m=puntuacion.index(mayor)
print('La palabra con mayor puntacion es:',verificadas[i_m])
    
