# Algoritmo para determinar el número mayor entre un número aleatorio y 
#otro definido por el usuario
# 1.	Generar el número aleatorio (1-20)
# 2.	Pedir un número al usuario
# 3.	Comparar los números
# 4. Mostar true si el numero del usuario es mayor y false en caso contrario


# import random as rd

# aletorio=rd.randint(1,20) 
# # randint ----> [1,20] 
# # ranrange ---> ranrange(10) [0,10)  // ranrange(1,10) [1,10)
# print(aletorio)
# usuario=int(input("Ingrese un numero: ")) #---> str 
# # 10 ---> "10"
# resultado=usuario>aletorio
# print("El numero proporcionado por el usuario es mayor al aletorio: {}".format(resultado))



######################################################################
######################################################################
# Desarrolle un programa que permita el ingreso por teclado de sus nombres y apellidos, 
# edad, estatura, color de ojos y de cabello. Luego, su programa mostrará todos los datos 
# con el siguiente formato:


#Bienvenid@ [nombres] [apellidos].
#Tienes [edad] anios.
#Mides [estatura] y pesas [peso]. Por lo tanto tu IMC [imc]
#Tu color de ojos es [ojos] y de tu cabello es [cabello].
# nombres=input("Ingrese sus nombres: ")
# apellidos=input("Ingrese sus apellidos: ")
# edad=input("Ingrese su edad: ")
# estatura=input("Ingrese su estatura: ")
# peso=input("Ingrese su peso")
# imc=float(peso)/(float(estatura)**2)
# ojos=input("Ingrese su color de ojos: ")
# cabello=input("Ingrese su color de cabello: ")
# print("Bienvenid@ {} {}.\nTienes {} anios.\nMides {} m y pesas {} kg. Por lo tanto tu IMC es {:.2f}.\
# \nTu color de ojos es {} y de tu cabello es {}".format(nombres,apellidos,edad,estatura,peso,imc,ojos,cabello))

######################################################################
######################################################################
# En Ecuador somos aproximadamente 17244437 personas en 2020, de acuerdo al INEC. 
#Ud. va a escribir un programa que nos permita calcular la población después en una 
# cantidad de años determinados. Para esto, usará la siguiente información:
# 1. Cada 98 segundos, nace una persona. 
#   segundos         nacimientos
#      98                 1
#   31536000              x
# segundos del anio/98 --> nacimientos por anio
#86400/98----> 881*365---> nacimientos por anio
# 2. Cada 348 segundos, muere una persona.
#86400/348---> 248*365---> muertes por anio
# 3. Cada año tiene 365 días.
# Escriba un programa que pida un numero de años (entre 1 y 10), y que 
#muestre la población aproximada para dicho año. Muestre el año y la cantidad de 
#personas para dicho año:
# Años a futuro: 7
# Población en 2025: 18400313

#Datos
# anio=int(input("Anios a futuro: "))
# actual=17244437
# muertes=(365*24*60*60)/348
# nacimientos=(365*24*60*60)/98
# poblacion=actual+(nacimientos*anio)-(muertes*anio)
# print("Poblacion en {}: {:.0f}".format(2020+anio,poblacion))

######################################################################
######################################################################
#Cree un programa que permita el ingreso de una palabra e indique por pantalla, 
#mediante un True o un False, si es la palabra es palíndroma. 
#Una palabra es palíndroma cuando se lee igual de izquierda a derecha y de derecha a izquierda, 
#por ejemplo: “KAYAK” o “RECONOCER”. Al ingresar estas palabras, sus palabras mostrarán un 
#mensaje con el valor de True.
#Por otro lado, sí ingresa la palabra “CASA”, su programa mostrará un mensaje 
# con el valor de False, dado que no es una palabra palíndroma.

# palabra=input("Ingrese una palabra: ")
# #Slicing----> "casa"   ----> "asac"
# resultado=palabra==palabra[::-1]
# print("La palabra {} es palindroma: {}".format(palabra,resultado))

######################################################################
######################################################################
# Quieres escribir un programa para manipular el DNA, 
# que son secuencias de letras A, T, C y G. 
# Quieres extraer un parte de una secuencia, y buscar si esta aparece en otra secuencia. 
# Por ejemplo:
# Secuencia original: ATCCGTAGCGTAATCCATGCATTATC
# Extraer desde posición: 4
# Extraer hasta posición 9
# Secuencia extraída: GTAGCG
# Secuencia a BUSCAR: TTGACTATAGCCAAGCGTAGCGAAAAAATTC
# Se encontró la secuencia extraída en la secuencia a buscar: true

# original=input("Ingrese una secuencia de ADN: ")
# inicial=int(input("Extraer desde la posicion: "))
# final=int(input("Extraer hasta la posicion: "))
# extraida=original[inicial:final+1]
# busqueda=input("Secuencia a BUSCAR: ")
# busqueda=extraida in busqueda #True/False
# print("Secuencia extraida: {}".format(extraida))
# print("Se encontró la secuencia extraída en la secuencia a buscar: {}".format(busqueda))

######################################################################
######################################################################
# Diseñar un algoritmo que imprima con un cartel <True> según el siguiente caso: 
# si el numero N es múltiplo de 5 y se encuentra entre los 25 primeros números. 
# N debe ser obtenido aleatoriamente entre números del 1 al 1000. Primero debe mostrar N.

# import random as rd

# n=rd.randint(1,1000)
###################
##Division entera #
##10//3---> 3     #
#                 # 
##Modulo (Residuo)#
##10%3 ---> 1     #
###################

# resultado= n%5==0 and n<=25
# print("El numero aletorio es:",n)
# print("<{}>".format(resultado))

######################################################################
######################################################################
# Describa el algoritmo para determinar si un estudiante ha aprobado el curso académico de 
# Fundamentos de programación teniendo en cuenta que el estudiante tendrá tres calificaciones
# teorico ---> 70 (2 parcial)
# practico---> 30 
# Las notas deben ser ingresadas por el usuario. El promedio final debe mostrarse, 
# así como el mensaje de si aprobó o no (promedio>6).

# parcial1=float(input("Ingrese su nota de primer parcial: "))
# parcial2=float(input("Ingrese su nota de segundo parcial: "))
# practico=float(input("Ingrese su nota del practico: "))
# promedio=(((parcial1+parcial2)/2)*0.7)+(practico*0.3)
# print("El promedio del usuario es {:.1f}".format(promedio))
# print("Aprobo la materia:",promedio>=60)


# Considere una secuencia de DNA, formada por la combinación de nucleobases A, T, C y G. 
# Por ejemplo
# ATTGGCAGTACCGATTA
# Escriba un programa, que pida una secuencia de DNA, 
# una posición en dicha secuencia (las posiciones empiezan en 0 desde izquierda a derecha) 
# y nueva secuencia a insertar, y genere la secuencia modificada. Por ejemplo:
# Secuencia original: ATTGGCAGTACCGATTA
# Posición donde insertar nueva secuencia: 10
# Nueva secuencia a insertar: TTTGGAAA
# Nueva secuencia: ATTGGCAGTATTTGGAAACCGATTA

# ATTGGCAGTACCGATTA
#

original=input('Ingrese una secuencia de ADN: ')
posicion=int(input("Posición donde insertar nueva secuencia: "))
nueva=input("Nueva secuencia a insertar: ")
secuencia_nueva=original[:posicion]+nueva+original[posicion:]
print("Nueva secuencia:",secuencia_nueva)