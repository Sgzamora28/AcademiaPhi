#Ejercicio 1
# Escriba un programa que pregunte cuantos números se van a introducir, permita el
# ingreso de dichos números y muestre por pantalla cuantos números son pares y la suma
# de todos los impares.

# #Pedir la cantidad de datos
cantidad=int(input("Ingrese la cantidad de numeros: "))

#Escribir los datos
numeros=[]
for i in range(cantidad):
  numero=input("Ingrese un numero: ")
  #condiciones correctas---> numero.isdigit()
  while not(numero.isdigit()):
    numero=input("Ingrese unicamente numeros: ")

  numero=int(numero)
  numeros.append(numero)

#Categorizar los datos
pares=0 #contador de numeros pares
impares=0 #variable que acumula la suma
for n in numeros:
  if n%2==0:
    pares+=1
    # pares=pares+1

  else:
    impares+=n
    # impares=impares+n

print(pares)
print(impares)



#Ejercicio 2

# Simular el lanzamiento de un dado. Muestre el resultado en cada intento. Finalice
# cuando salga el número 3 e imprima al final cuantos números se generaron hasta el 3.
import random as rd
dado=0
#condicin correcta---> dado==3 ---> not(dado==3) = dado!=3
repeticiones=0
while dado!=3:
  #randint---> [a,b]
  #ranrange---> [a,b)
  dado=rd.randint(1,6)
  print(dado)
  repeticiones+=1

print("repeticiones:",repeticiones)



#Ejercicio 3

#El sistema debe pedir un usuario y una contrassenia numerica de 5 digitos
#El sistema debe sumar los digitos de la contrasenia, la suma de digitos se debe repetir hasta que solo quede un digito:
#Si el numero es un numero primo le indicara que es una contasenia valida
#Si el numero no es primo, debera ingresar de nuevo la contrasenia

primos=[2,3,5,7]
usuario=input("Ingreses su usuario: ")


#condiciones correctas---> contra.isdigit() and len(contra)==5
validacion=False #esta variable valida la contrasenia
#condicion correcta---> validacion

while not(validacion):
  contra=input("Ingrese su contrasenia: ")
  while not(contra.isdigit() and len(contra)==5):
    contra=input("La contrasenia solo debe tener 5 numeros: ")

  suma=0
  verificador=int(contra)
  while verificador>=10:
    for digito in str(verificador):
      suma+=int(digito)
    
    verificador=suma
    if suma>=10:
      suma=0

  if suma in primos:
    validacion=True
    print("Contrasenia valida")

  else:
    validacion=False
    print("Contrasenia invalida")