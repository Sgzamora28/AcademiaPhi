#MATERIALES ----> Tipos de datos

#Texto/Cadena de caracteres

####### STRING (str) #######
#     "Hola"    'Hola'
#            "5"
#           "9.8"

#Numerico

####### INTEGER (int) #######
      #Numeros enteros#
#            10
#             5
#          294723    

####### FLOAT (float) #######
     #Numeros decimales#
#            10.68
#          48274181.1

#Logico


####### BOOLEAN (bool) #######
      #Valores de verdad#
#True
#False


#CONVERSIONES (CASTING)

# Cualquier dato se puede transformar a str
# x=937
# print(type(x))
# x=str(x)
# print(type(x))
#Si quiero convertir un str a int. El str solo debe contener numeros
# x="39489"
# print(type(x))
# x=int(x)
# print(type(x))
#Si quiero convertir un str a float. El str debe tener numeros y UN SOLO PUNTO DECIMAL
# x="3483547.7"
# print(type(x))
# x=float(x)
# print(x)
# print(type(x))
#Cualquier int se puede convertir a float
# x=27463
# print(x,type(x))
# x=float(x)
# print(x,type(x))

#Si convierto un float a int, el float se trunca
# x=38573.565
# y=45.2
# print(x,type(x))
# print(y,type(y))
# x=int(x)
# y=int(y)
# print(x,type(x))
# print(y,type(y))

#Conversiones a boolean
#Str a booleano
# x="Hola"
# y=""
# print(x,type(x))
# print(y,type(y))
# x=bool(x)
# y=bool(y)
# print(x,type(x))
# print(y,type(y))

#Int a bool
# x=0
# y=1868755
# print(x,type(x))
# print(y,type(y))
# x=bool(x)
# y=bool(y)
# print(x,type(x))
# print(y,type(y))


#ETIQUETAS DE LOS MATERIALES ---> Variables


# variable = valor/dato

#RECOMENDACIONES
#1. Las variables no pueden empezar con numero (error)
# XXXXX 1numero XXXXX
# numero1
#2. Las variables no deben empezar con mayus (recomendacion)
# XXXXX Nombre XXXXX
# nomBre 
#3. No se pueden utilizar nombres reservados (error) ---> nombres de funciones (print,input,for,sum)
#4. Las variables no pueden tener espacio o guiones (-) (error)
# XXXXX primer nombre XXXXX
# XXXXX primer-nombre XXXXX
# primerNombre
# primer_nombre


carrera="Mecatronica"
matricula=202101713

#FORMAS DE ASIGNACION DE VARIABLES

# Asignacion en la misma linea
materia1="Fisica"; materia2="Calculo"

#Asignacion multiple (desempaquetamiento)
dia,mes,anio=16,"mayo",2023

#Asignacion del mismo valor
edad1=edad2=21

#Asignacion de intercambio
x=15
y=20
# print(x,y)
x,y=y,x 
# print(x,y)


#Actualizacion de variable
nombre="Steven"
apellido="Zamora"
# print(nombre,apellido,edad1)

nombre="Kyra";edad1=19
# print(nombre,apellido,edad1)

#Actualizacion por acumulacion
promedio=6
# print(promedio*10)
promedio+=2 #promedio=promedio+1 
# print(promedio)


#Operaciones entre tipos de datos
###Numerico### 
#Las mismas operaciones aritmeticas 
#Para expresar potencia:
porcentaje=promedio**2
# print(porcentaje)
#Divison entera ---> Division que no toma los decimales
division=5//3
# print(division)

#Modulo ---> Residuo de una division
residuo=5%3
# print(residuo)

###Cadenas de texto###
#Concatenacion
frase1="Hola"
frase2="que hace"
frase=frase1+", "+frase2
# print(frase)

#Repeticion
frase_repetida=(frase1+" ")*3
# print(frase_repetida)

###Operaciones Logicas### 
#Son operaciones que me devuelven valores de True/False

#Igualdad 
#Comparar dos datos

# a="Hola"
# b="Hola"
# z=a==b
# print(z)

#Desigualdad (diferencia)
# a=1000
# b=1000
# z=a!=b
# print(z)

#Mayor/Menor que (solo para numeros)
# a=10
# b=10
# z=a>b
# print(z)
#Disyuncion (or)
#primisa p
#primisa q
a="Hola"=="HOLA"
b=10>5
z=a or b
# print(a,b,z)

#Conjuncion (and)
a="Hola"=="Hola"
b=10>5
z=a and b
# print(a,b,z)

#Negacion (not)
a=not ("Hola"=="Hola")
# print(a)

#ENTRADA/SALIDA DE DATOS

#SALIDA#
#Para mostrar datos utilizamos el print(dato1,dato2...)
# print(nombre,"Azucena",apellido,edad1)
#ENTRADA#
#Si queremos ingresar algo al programa, utilizamos el input(mensaje para el usaurio)
# materia_favorita=input("Ingresa tu materia favorita: ")
edad=input("Ingresa tu edad: ") #21---> "21"
edad=int(edad)
#OBSERVACION#
#El input ingresa todos los datos como tipo str

# print("La materia favorita de",nombre,"es",materia_favorita)
anio_nacimiento=2023-edad
print("El anio de nacimiento del usuario es",anio_nacimiento)