################################################
#Funciones de Entrada y Salida
################################################
#-------------------------------------
#funciones que me permiten interactuar con el programa (Salida)
nombre="Kyra Azucena"
#la que me muestra las cosas en la pantalla
# print(nombre,"es hermosa") 
#mostrar numeros, cadenas de texto, lo que contengan las variables
#-------------------------------------

#-------------------------------------
#la que me permite ingresar cosas al programa (Entrada)
# edad=input("Ingrese su edad: ")
#-------------------------------------

################################################
#Actulizacion de Variables
################################################

# print(nombre)
# nombre="Steven Zamora" #Actualizacion por completo
# nombre=nombre+" Franco Jaramillo" #Actualizacion utilizando un valor anterior
nombre+=" Franco Jaramillo"
# print(nombre)


################################################
#Conversion/Casting
################################################

#Reglas de las conversiones
#1. Cualquier dato se puede transformar a string
#2. Cuando convierto un str a int. El str solo debe tener numeros enteros
#3. Cuando convierto un str a float. El str solo puede tener numeros y un solo punto decimal
#4. Se puede convertir de float a int pero no se redondeara el numero 
#5. Siempre puedo convertir int a float 

#Como se realiza una conversion
#1. Se usa el identificador del dato al que quiero convertir
#. Si quiero convertir a string ---> str
#. Si quiero convertir a entero ---> int
#. Si quiero convertir a float --->  float
#2. Se pone entre parentesis el dato que quiero convertir

edad=input("Ingrese su edad: ") #El input siempre me devuelve un string
edad=int(edad)

nacimiento=2023-edad #2023-21
print("El anio de nacimiento es",nacimiento)


