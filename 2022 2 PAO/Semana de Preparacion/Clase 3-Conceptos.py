########################################################
###              ESTRUCTURAS ITERATIVAS              ###
########################################################

#Ciclos o Bucles
#Loops


#Programacion ineficiente
# numero=int(input("Ingrese un numero: "))

# print("El resultado de",numero,"x 1 =",numero*1)
# print("El resultado de",numero,"x 2 =",numero*2)
# print("El resultado de",numero,"x 3 =",numero*3)
# print("El resultado de",numero,"x 4 =",numero*4)
# print("El resultado de",numero,"x 5 =",numero*5)
# print("El resultado de",numero,"x 6 =",numero*6)
# print("El resultado de",numero,"x 7 =",numero*7)
# print("El resultado de",numero,"x 8 =",numero*8)
# print("El resultado de",numero,"x 9 =",numero*9)
# print("El resultado de",numero,"x 10 =",numero*10)


#FOR
#Se utiliza cuando sabemos o tenemos certeza de la cantidad de repeticiones que tendremos
#Sintaxis: for [el nombre de una variable] in [objeto iterable]:

#UN ELEMENTO ITERABLE
nombres=["Steven","Jairo",'Kyra',"Fernando","Alex","Isabel"] #Una lista es un elemento iterable
edades=[20,19,19,25,17,50]
#        0         1       2       3         4       5         range(len(lista))
"Fundamentos de Programacion" #Es un elemento conformado de caracteres
range(3) #---> Nos devuelve un rango-intervalo de numeros enteros----> [0,3) = 0,1,2

#Los elementos que pueden utilizar indices son iterables
#Todas las colecciones son iterables

# print(lista[0])
# print(lista[1])
# print(lista[2])
# print(lista[3])
# print(lista[4])


#FOR POR INDICES
#Se utiliza para listas paralelas
#Se utiliza cuando me importa el indice del elemento o su orden
# for i in range(len(nombres)):
  #La edad de [nombre de la persona] es [edad de la persona]
  # print(i)
  # print("La edad de",nombres[i],"es",edades[i])



#FOR POR CONTENIDO
#Cuando quiero el contenido directament
# for nombre in nombres:
#   print(nombre)



#WHILE
#Se utiliza cuando no sabemos cuantas repeticiones habran o para VERIFICACIONES
#Sintaxis:
# while [valor booleano]:
# (actualizar el valor booleano)


#Crear un programa que verifique que el usuario ingresa un numero de cedula correcto
cedula=input("Ingrese su cedula: ")
#Pasos para crear una verificacion:
# 1. Conocer las condiciones correctas del dato que ingresa---> 
# String solo contenga numeros Y String solo de numeros contenga 10 digitos
#          .isdigit()         and              len()==10
# cedula.isdigit() and len(cedula)d
# 2. Negarlas ---> not(cedula.isdigit() and len(cedula))

while not(cedula.isdigit() and len(cedula)==10):
  cedula=input("Ingrese una cedula con el formato correcto: ")


