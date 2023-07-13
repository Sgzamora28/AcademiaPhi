# Escriba un programa en Python que implemente el “Juego de las Ruedas”. 
# Para esto genere aleatoriamente una lista de 12 elementos donde cuatro elementos deben decir “Rueda” y 
# los otros ocho deben decir “X”. Luego el programa deberá pedirle al jugador que ingrese por teclado índices 
# entre 0 y 11 (validar). Asuma que el jugador siempre ingresa índices distintos. Si el índice ingresado por el 
# usuario corresponde al de una “Rueda”, gana $1000. El jugador tiene seis intentos para hallar las cuatro “Ruedas”. 
# 
# En cada intento muestre por pantalla el número total de “Ruedas” encontradas hasta el momento. 
# Si el jugador encuentra las cuatro “Ruedas” se gana un carro. 
# El juego termina cuando encuentra las cuatro “Ruedas” o ha usado todos los intentos. 
# Al final muestre el premio que recibe el jugador (cantidad de dólares o la 
# palabra “carro” si encontró las cuatro ruedas)
import random as rd

juego=["X"]*8+["Rueda"]*4
# print(juego)
rd.shuffle(juego)
# print(juego)
print("Juego de Ruedas")


intentos=6
#Condiciones del Game Over---> intentos==0 or ganar
encontradas=0
premio=0
while not(intentos==0 or encontradas==4):
  print("Has encontrado {} ruedas".format(encontradas))
  indice=input("Ingresa un numero del 0 al 11 para encontrar un rueda: ")#----> "uno"

  #condiciones del dato--> indice.isdigit() and int(indice) in range(12)
  while not(indice.isdigit() and int(indice) in range(12)):
    indice=input("Ingrese el numero en el formato correcto: ")

  indice=int(indice)


  if juego[indice]=="Rueda":
    encontradas+=1
    premio+=1000
    if premio!=4000:
      print("Encontraste un rueda. Vas ganando {} dolares".format(premio))

    else:
      print()
  else:
    print("No hay ninguna ruenda en el indice que marcaste")

  intentos-=1


if encontradas==4:
  print("Usted ha ganado un carro")

elif 1<encontradas<4:
  print("Usted ha ganado {} dolares".format(premio))

else:
  print("Usted no ha ganado ningun premio")