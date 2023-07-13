# Pedir por teclado los 2 nombres y almacenarlos en una variable con el nombre adecuado. 
# Pedir los 2 apellidos y almacenarlos en una variable. 
# Pedir la fecha de nacimiento con el formato dia, mes y años en dígitos (dd/mm/aaaa) 
# Pedir el número de matrícula 
# Pedir la calificación del parcial sobre 100 
# Pedir la calificación del final sobre 100 
# Pedir la calificación del componente práctico sobre 100 

# Al nombre y apellido ingresados debe colocarlos en mayúsculas 
# A la fecha de nacimiento debe obtener con split el año, luego convertirlo en 
# entero y calcular la edad del estudiante 
# Con la matrícula debe obtener los primeros 4 caracteres convetirlos a entero y 
# calcular cuantos años lleva en la universidad, tome en cuenta el año actual también. 
# Con las calificaciones de los parciales debe promediarlas y mostrar el valor redondeado. 
# Para calcular el promedio general debe tomar en cuenta que la nota teórica se debe 
# multiplicar por 70% y la práctica por 30%, luego debe convertirlo para que esté sobre 10 y 
# mostrar el resultado con 2 decimales de presición. 
# Finalmente, detenrmine si aprobó o no con una expresión booleana (nota mayor o igual a 6.0)

#FORMATO DE SALIDA
# ************* REPORTE DE CALIFICACIONES ************* 
# ----------------------------------------------------- 
# Estudiante.... : ..........VERA GONZALEZ MARIA CAMILA 
# Edad.......... : ................21.................. 
# Años en la U.. : ................2................... 
# Teoría........ : ................56.................. 
# Práctica...... : ................78.................. 
# Promedio...... :                                 6.26 
# Aprobó........ : True  

#DATOS DE INGRESO
# nombres=input("Ingrese sus dos nombres: ").upper() #Steven ZAmora ----> STEVEN ZAMORA
# apellidos=input("Ingrese sus dos apellidos: ").upper()
# fecha_nacimiento=input("Ingrese su fecha de nacimiento (dd/mm/aaaa): ") #"28/05/2002"  ---split("/")---> ["28","05","2002"]
# lista_fecha=fecha_nacimiento.split("/") #["28","05","2002"]
# #                                          -3   -2     -1
# #                                           0    1      2
# anio=int(lista_fecha[-1]) #'2002'  ----> 2002
# edad=2023-anio 
# matricula=input("Ingrese su numero de matricula: ") #---> '202101713'
# anio_ingreso=int(matricula[:4]) #--> 2021
# anios_enEspol=2023-anio_ingreso


# parcial1=float(input("Ingrese la calificacion del primer parcial: ")) 
# parcial2=float(input("Ingrese la calificacion del segundo parcial: "))
# promedio_teorico=(parcial1+parcial2)/2
# practico=float(input("Ingrese su cafificacion del componente practico: "))
# #Componente Teorico ---> 70%
# #Componente Practico --> 30%
# nota_final=((promedio_teorico*0.7)+practico*0.3)/10
# aprobacion=nota_final>=6

# #SALIDA
# print("{:*^53}".format("REPORTE DE CALIFICACIONES"))
# print("-"*53)
# print("Estudiante....: {1:.>20} {0}".format(nombres,apellidos))
# print("Edad: {}".format(edad))
# print("Anios en la U: {}".format(anios_enEspol))
# print("Teorico: {}".format(promedio_teorico))
# print("Practico: {}".format(practico))
# print("Promedio: {:.2f}".format(nota_final))
# print("Aprobo: {}".format(aprobacion))

#MODULO RANDOM
import random as rd

#RANDINT/RANRANGE
a1=rd.randint(1,10) #----> [1,10] ---> 1,2,3,4,5,6,7,8,9,10

#cuando queremos aleatoridad con indices de str/listas
a2=rd.randrange(10) #----> [0,10) ---> 0,1,2,3,4,5,6,7,8,9

palabra="Hola mundo" #len---> 10 
#        0        9

palabra=palabra[:-1]+"a"
# print(palabra)
#SIEMPRE EL ULTIMO INDICE SERA LA LONGITUD-1
# print(len(palabra))

#Generar una letra aleatoria de la palabra
# indice=rd.randrange(len(palabra)) #randrange(10)----> [0,10) 0,1,2,3,4,5,6,7,8,9
# print(indice)
# letra1=palabra[indice]
# print(letra1)
# indice2=rd.randint(0,len(palabra)-1) #randint(0,10)----> [0,10] 0,1,2,3,4,5,6,7,8,9,10
# print(indice2)
# letra2=palabra[indice2]
# print(letra2)

# #CHOISE
# letra3=rd.choice(palabra)
# print(letra3)


#########################################
#Listas
#########################################

nombres=["Steven","Kyra","Fernando","Alexander"]
#           0       1        2           3
#          -4      -3       -2          -1
# print(nombres)
#longitud----> len(nombres)---> 4

#Permiten indexacion
nombre1=nombres[0] #Steven
# print(nombres[0][1])

#Permiten slicing ----> lista mas chiquita
nombres2=nombres[1:3] #["Kyra","Fernando"]

#Son mutables (modificables)
nombres[2]="Daniel"
nombres[-1]="Jared"
# print(nombres)


# La compañía ACME S.A. está desarrollando un nuevo método para detectar especies
#  en base a su ADN. Para representar una especie por su ADN se utiliza una secuencia 
# S compuesta únicamente de las letras A, C, G y T.
# Se tienen como datos:
# Una lista L de secuencias S y una cadena de referencia R que identifica de forma única a 
# la especie buscada. R no tiene letras repetidas.
# Implemente un programa en Python que muestre todas las secuencias S que pertenecen a 
# la especie buscada y los índices en la inversa de S (INV) donde aparece la cadena de 
# referencia R.
# Para realizar esta tarea, por cada secuencia S en L:
# Forme la cadena inversa (INV) de la secuencia S.
# Si S pertenece a la especie buscada, muestre la secuencia S y los índices. Ejemplo:
lista = ['ATTTGCTTGCTATTTAAACCGGTTATGCATAGCGC', 'ATTAGCCGCTATCGA']
referencia = 'TA'
# Índices: [0, 2, 25, 29]
indices=[]
indice=int(input("Ingrese un indice para escoger la secuencia: "))
secuencia=lista[indice][::-1]
coincidencia=secuencia.find(referencia)
indices.append(coincidencia)
print(indices)