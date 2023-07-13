# texto=input("Ingrese un oracion: ")#La raiz cuadrada de 36 es 6
# #input()---> str 
# palabras=texto.split(" ") #["La","raiz","cuadrada","de","36","es","6"]
# # print(palabras)
# #for [variable] in [lo que queremos iterar]:

# p=0 #contador de palabras
# n=0 #contador de numeros

# for palabra in palabras:
#     # print(palabra)
#     if palabra.isalpha():
#         p+=1
#     else:
#         n+=1

# #La oracion contiene unicamente palabras n==0
# if n==0:
#     print("El texto ingresado solamente contiene palabras")
# #La oracion contiene unicamente numeros  p==0
# elif p==0:
#     print("El texto ingresado solamente contiene numeros")

# #La oracion contiene numeros y palabras  
# else:
#     print("El texto ingresado contiene numeros y palabras")

# print(f"Total palabras: {p}")
# print(f"Total numeros: {n}")


#########################################################
#########################################################
#Taller 1
#Tema 1

#Cree una funcion que retorne True/False si el numero ingresado es primo
#Un numero primo es divisible SOLAMENTE para si mismo y para el 1
#NUMERO DIVISIBLE---> residuo de ese numero para el numero que estamos comprobando sea 0
#5%2 --> 1
#4%2 --> 0
#def [nombre de funcion]([parametros]):
    #BLOQUE DE CODIGO
    #BLOQUE DE CODIGO
    #BLOQUE DE CODIGO
#   return [valor]

def esPrimo(numero):
    divisores=[]
    for i in range(1,numero+1): #[1,9) 
        if numero%i==0:
            divisores.append(i)
        
    if len(divisores)==2:
        return True
    else:
        return False
    
#Tema 2
import random as rd
# #Generar una lista de 5 numeros primos aletorios entre 100 y 375 
# lista=[]

# #Como crear una estructura de while
# #1. reconocer la condicion del ejercicio
# # len(lista)==5
# #2. negarlo
# # not([condicion]) ---> not(len(lista)==5)
# # len(lista)!=5
# while not(len(lista)==5):
#     aleatorio=rd.randint(100,375)
#     if esPrimo(aleatorio) and aleatorio not in lista:
#         lista.append(aleatorio)

# print(lista)

#Tema 3
#Dada una lista de numeros, cree otra lista solo con los numeros pares
#Numero par=numero es divisible para dos
#x%2 ---> 0
# l_numeros=rd.sample(range(1,101),20)
# print(l_numeros)

# l_pares=[]
# for numero in l_numeros:
#     if numero%2==0:
#         l_pares.append(numero)

# print(l_pares)


###########################################################################
###########################################################################
#Taller 2
#Tema 1
# Implementar un programa en Python que presente al usuario un menú con 5 opciones:
# Sumar, Restar, Multiplicar, Dividir y Salir.
# Solicite al usuario dos números para realizar las operaciones, 
# pero solicite también que el usuario elija solo una opción del menú. 
# Presentar por pantalla el resultado de la operación seleccionada por el usuario, 
# o un mensaje de agradecimiento si elige Salir.

opcion=""

while opcion!="Salir":
    print("[1] Sumar\n[2] Restar\n[3] Multiplicar\n[4] Dividir\n[5] Salir")
    opciones=["Sumar","Restar","Multiplicar","Dividir","Salir"]
    opcion=input("Ingrese su opcion: ").title()
    while opcion not in opciones:
        opcion=input("Ingrese una opcion valida: ").title()

    if opcion!="Salir":
        numero1=int(input("Ingrese el primer numero: "))
        numero2=int(input("Ingrese el segundo numero: "))
        if opcion=="Sumar":
            print("Usted va a sumar")
            resultado=numero1+numero2
        elif opcion=="Restar":
            print("Usted va a restar")
            resultado=numero1-numero2
        elif opcion=="Multiplicar":
            print("Usted va a multiplicar")
            resultado=numero1*numero2
        elif opcion=="Dividir":
            print("Usted va a dividir")
            resultado=numero1/numero2
        print("El resultado de la operacion es",resultado)
    else:
        print("Hasta pronto")