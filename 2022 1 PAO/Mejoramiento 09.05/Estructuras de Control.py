
#/////////////////////////////////////Operaciones logicas/////////////////////////////////////


#------------------Con numeros------------------

x=10
y=5
z=10

#Igualdad y Desigualdad
igualdad=x==y
desigualdad=x!=y
# print("Igualdad",igualdad)
# print("Desigualdad",desigualdad)

#Mayor y Menor
mayor=x>=z
# print("Mayor que",mayor)

menor=x<z
# print("Menor que",menor)


#Conjunciones 
conjuncion= mayor and menor

#Disyunciones
disyunciones= mayor or menor


#------------------Con cadenas------------------

#Igualdad y Desigualdad
#Hay qeu cuidar mayusculas y minusculas

#Pertenencia
str1="Hola me llamo Steven"
str2="Steven"
pertenencia=str2  in str1
# print("Pertenencia",pertenencia)


#Negacion
negacion_igualdad=not(igualdad)
# print("Negada",negacion_igualdad)


#/////////////////////////////////////Estructuras Logicas/////////////////////////////////////

#------------------Estructuras Condicionales------------------

#########################################
#Ejercicio 1
#########################################
# Implementar un programa en Python que permita el ingreso de cualquier peso (kilogramos) y cualquier estatura (metros) 
# para calcular el índice de masa corporal (IMC). Para obtener el IMC, utilice la siguiente fórmula IMC = peso / estatura2. 
# Su programa deberá mostrar si tiene bajo peso, peso normal o sobrepeso, 
# para lo cual debe comparar el valor del IMC con los siguientes valores de referencia:
# bajo peso (IMC < 18,5), peso normal (IMC entre 18,5 y 24,99) y sobrepeso (IMC >= 25,00)

peso=input("Ingrese su peso en kg: ")
altura=input("Ingrese su altura en metros: ")
print("Se calculara su IMC")
imc=float(peso)/float(altura)**2

print("Su imc es igual a",round(imc,2))
if imc<18.5: #imc----> 18.4999999
  print("Usted tiene bajo peso")

elif 18.5<=imc<25: #imc----> 18.5 imc----> 24.9999999
  print("Usted tiene un peso normal")

else:
  print("Usted tiene sobrepeso")

#########################################
#Ejercicio 2
#########################################
#Usted tiene un sistema de verificacion de Cedulas de identidad. El programa pide al usuario que ingrese su CI y usted debe verificarlo.
#En caso de que la CI tenga el formato correcto, se imprimira una confirmacion. 
# Caso contrario, se mostrara por pantalla el mensaje "Formato Incorrecto" 

ced=input("Ingrese su cedula de identidad: ")#----> "09" ----> 9
#primera--> 10 digitos ---> len()
#segunda ---> solo sean numeros
if len(ced)==10 and ced.isdigit():
  print("Cedula valida")

else:
  print("Formato de cedula incorrecto")

