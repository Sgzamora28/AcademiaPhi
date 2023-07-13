#*****************************Adivina las letras de una palabra ************)
#El sistema debe generar una palabra aleatoria de 15 letras usando solo las letras: A, C, B, O ,L ,M, N, I, P, E.
#El sistema pedirá al usuario ingresar 3 letras (puede repetir): A, C, B, O ,L ,M, N, I, P, E.
#El sistema le dará un punto por cada vez alguna de las letras ingresadas se repita en la palabra.
#Si obtiene más de 7 puntos, le muestra el siguiente mensaje “Usted es un gran adivino”
#Si obtiene desde 3 hasta 7 puntos, le muestra el siguiente mensaje “Usted debe seguir practicando para mejorar”
#Si obtiene menos de 3, le muestra el siguiente mensaje “Usted debe buscar otro juego”
#Debe mostrar la palabra generada aleatoriamente al final.
import random as rd

letras=['A','C','B','O','L','M','N','I','P','E']
palabra=""
for i in range(15):
  x=rd.choice(letras)
  palabra+=x

print(palabra)
total=0
for i in range(3):
  ingreso=input("Ingrese una letra: ").upper()
  conteo=palabra.count(ingreso)
  total+=conteo

if total>7:
  print("Usted es un gran adivino")

elif 3<total<=7:
  print("Usted debe seguir practicando para mejorar")

else:
  print("Usted debe buscar otro juego")


print(palabra)