#FUNCIONES -----> HERRAMIENTAS PARA CONSTRUIR
#print ---> mostrar por pantalla un valor 
#input ---> ingresar datos al programa
#round ---> redondea

#VARIABLES
saludo="Hola que hace"
edad=21
nombre="Steven Zamora"

# print("Hola Mundo")
# print(saludo)

ancho=30
largo=40
# print(ancho,largo)
ancho=40
# print(ancho,largo)

anio=2020
# print(anio)
anio=anio+1#2021
anio+=1#2022
# print(anio)
# print(edad)
edad-=10#11
# print(edad)
edad/=2#5.5
# print(edad)



#CONVERTIR DATOS

#todo tipo de dato se puede transformar a string

anio=str(anio) #casting

#String ---> entero
x="2038284299293jdhfsajfs.-," #NO SE PUEDE
# x=int(x)
y="20.94" #NO SE PUEDE
# y=int(y)

z="2039" #SI SE PUEDE
# z=int(z)
# print(z)


#String ---> decimal
# x=float(x)
a="20.94"
a=float(a) #SI SE PUEDE
# print(a)

b="20,94" #NO SE PUEDE
# b=float(b) 

c="20.95.3" #NO SE PUEDE
# c=float(c)

d="21"
d=float(d) #SE PUEDE PASAR INT A FLOAT
# print(d)

e=20.55
e=int(e)
# print(e)


#De String a Bool

x=""
x=bool(x)
# print(x)
y=" "
y=bool(y)
# print(y)


#MANEJO DE ENTRADA Y SALIDA

#SECUENCIA DE SALIDA ---> print()

#SECUENCIA DE ENTRADA ---> input()


# nombre=input("Ingrese un nombre: ")
# print("El nombre del usuario es",nombre)

# edad=input("Ingrese su edad: ")
# edad=int(edad)
# print("La edad del usuario es:",edad)

# anio_nacimiento=2023-edad
# print("El anio de nacimiento del usuario es",anio_nacimiento)


# Ejercicio 1
# Escriba un programa, que pida el numero de galones de gasolina, 
# y nos muestre sus equivalencias de litros, barriles de petróleo, libras de CO2, precio en dólares. 
# Las equivalencias son:
# 1. Un galon son 3.785 litros
# 2. Un barril de petróleo produce 19.5 galones de gasolina
# 3. Un galon de gasolina produce 20 libras de CO2
# 4. Un galon de gasolina cuesta$2.98
# Por ejemplo:
# Numero de galones: 57
# 57 galones equivalen a:
# - 215.75 litros
# - 2.92 barriles de petróleo
# - 1140 libras de CO2
# - $169.86

# galones=input("Ingrese los numeros de galones: ")
# galones=float(galones)
# litros=galones*3.785
# barriles=galones/19.5
# barriles=round(barriles,2)
# libras_CO2=galones*20
# precio=round(galones*2.98,2)
# print("Numero de galones: ",galones)
# print(litros,"litros")
# print(barriles,"barriles")
# print(libras_CO2,"libras de CO2")
# print("$",precio)



#Se pide que usted cree una calculadora que permita ingresar dos numeros y muestre las operaciones basicas
#entre esos dos numeros (suma,resta,multiplicacion,division)


num1=int(input("Ingrese el primer numero: "))
num2=int(input("Ingrese el segundo numero"))
suma=num1+num2
resta=num1-num2
multiplicacion=num1*num2
division=round(num1/num2,2)
print("Se ingresaron los numeros",num1,"y",num2)
print("La suma entre los dos numeros es igual a",suma)
print("La resta entre los dos numeros es igual a",resta)
print("La multiplicacion entre los dos numeros es igual a",multiplicacion)
print("La division entre los dos numeros es igual a",division)

