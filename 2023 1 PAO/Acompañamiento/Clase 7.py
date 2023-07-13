#WHILE ----> Bucle

#while [condicion]:
#  bloque de codigo
#  bloque de codigo
#  bloque de codigo



###########################################
#VALIDACIONES
###########################################
#Un programa que me permite ingresar un numero para poder dividir con otro numero aleatorio

# import random as rd

# num1=rd.randint(1,20)
# print(num1)
# num2=input("Ingrese su numero: ")
# # "0" != 0  True

# #Pasos para crear validacion
# #1. Identificar cuando el dato es valido
# # que el numero sea un digito Y que el numero no sea 0
# # num2.isdigit() and num2!=0 ---> es que el str solo contenga numeros (True/False)
# #2. Creamos la estructura del while negando el dato valido
# #3. Pedimos nuevamente el dato
# # print(not num2.isdigit() or int(num2)==0) 
# #          1          ^       1      --->
# #        19.
# #       >(p)
# #       >(0)  ---> 1 True

# #        15
# #       >(1) ----> 0 False

# #       >(p V q)   ---> >p ^ >q
# while not num2.isdigit() or int(num2)==0: #not(num2.isdigit() and int(num2)!=0)
#     num2=input("El dato no esta ingresado en un formato valido\nIngrese nuevamente su numero: ")
    

# num2=int(num2)
# resultado=num1/num2
# print(resultado)

###########################################
#MENUES (While/ if-else)
###########################################

#Programar una calculadora que haga las operaciones de suma, resta, multiplicacion, divsion


#1. Inicializar la variable de la opcion
opcion=""
#1.5 Elegir de que manera salimos del menu
#2. Es crear la estructura del while negando la condicion de salida
#not(opcion==0)
while opcion!="0":
  opcion=input("Ingrese una opcion\n[1] Sumar\n[2] Restar\n[3] Multiplicar\n[4]Dividir\n[0] Salir\n")
  #int(opcion) in range(5) [0,5) 0 1 2 3 4
  #3. Es validar la opcion
  while not(opcion.isdigit() and 0<=int(opcion)<5): 
    opcion=input("Ingrese una opcion valida: ")
  #Es crear las opciones del menu --> if-elif-else
  #0 1 2 3 4
  num1=input("Ingrese su primer numero: ")
  num2=input("Ingrese el segundo numero: ")
  #num1.isdigit() and num2.isdigit()
  while not(num1.isdigit() and num2.isdigit()):
    num1=input("Ingrese su primer numero: ")
    num2=input("Ingrese el segundo numero: ")

  num1=int(num1)
  num2=int(num2)
  if opcion=="1":
    print("Suma")
    resultado=num1+num2

  elif opcion=="2":
    print("Resta")
    resultado=num1-num2

  elif opcion=="3":
    print("Multiplicacion")
    resultado=num1*num2

  elif opcion=="4":
    print("Divsion")
    resultado=num1/num2

  else: #elif opcion=="0"
    print("Chao...")

  if opcion!="0":
    print("El resultado es igual a",resultado)

  print("\n")