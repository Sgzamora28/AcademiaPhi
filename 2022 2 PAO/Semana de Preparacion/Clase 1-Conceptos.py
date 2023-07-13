##################################
###numericos###
##################################

#enteros (int)
28472
#decimales (float)
123.955
123.08

#operaciones numericas

323+123  #---> resultado sera otro entero
173-193.09 #---> resultado sera un flotante
12*9

172/4  #---> puede salir un flotante
172//4 #no redondea, solo omite decimales
172%3  #residuo de una divison


123**23


##################################
###Texto###
##################################

#String (str) - cadenas de texto
'Steven'
#S esta en el indice 0
#t esta en el indice 1
#e esta en el indice 2


"Kyra"
# "7245" + 5
nombre="Azucena"
nuevoNombre=nombre+nombre#----> "AzucenaAzucena"
"Mecatronica"*2 #---->"MecatronicaMecatronica"


##################################
###Valores de Verdad###
##################################


#Booleanos (bool)
True
False

#Y
#True and False


#Or
#True or False

#Negacion
#not True


##################################
###Asignacion de varibles###
##################################

#Asigncion Directa
rEsultado2=123.955
resultado2=True

#Asignacion multiple
peso1=peso2=59

#Asignacion por refencia
numero1=911
y=numero1


##################################
###Entrada y Salida de Datos###
##################################

#Ingresar Datos
# edad=input("Ingrese su edad: ") #Todo lo que ingrese en el input---> str


#Mostrar Datos
# print("Hola Mundo")
# print("La edad del usuario es",edad)


##################################
###Conversiones - Casting###
##################################

#Todo dato se puede transformar a str
x=2022.9
numeroEn_texto=str(x)
booleano=False
bool_enTexto=str(booleano)

#Entero a Flotante 
y=20
numeroDecimal=float(y) #20.0


#String a Flotante
string="2034.23"
stringDecimal=float(string)




##################################
###Listas###
##################################
datos=["Steven","Zamora",20]
#Indice 0 esta "Steven"
#Indice 1 esta "Zamora"
#Indice 2 esta 20

#Indice -1 esta 20
#Indice -2 esta "Zamora"
#Indice -3 esta "Steven" 

nombre=datos[1][2] 
print(nombre)