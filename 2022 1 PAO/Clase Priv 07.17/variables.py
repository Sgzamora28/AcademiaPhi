#Strings ---> Cadenas de texto
x="Hola Mundo"
y='Adios Mundo'

z=x+y
# print(z)
z=x*2
# print(z)

#Integers---> int/numeros enteros
x=1345
# print(x)

multiplicacion=5*2
# print(multiplicacion)

division=10/4
# print(division)

entera=10//4
# print(entera)

potencia=10**entera
# print(potencia)

modulo=10%4#---> el residuo de una division
# print(modulo)

divisible=8%4
# print(divisible)
# print(type(x))

#Floats---> numeros decimales

x=15.4
# print(type(x))


#Booleans---> bool/valores de verdad
x=True
y=False
# print(type(x),type(y))

#Asignacion

patito=True
patito_numero=98
Patito='patito'
# "Steven"=nombre---> no se puede hacer

#Asignacion en una misma linea
num1=10; num2=15; num3=20

#Asignacion multiple
dia,mes,anio=17,7,2022

#Asignacion del mismo valor
alto=ancho=60

#Asignacion de intercambio
x=10
y=15

x,y=y,x

#Conversiones
# entero=35 #----> decimales y cadenas
# e1=str(entero)
# e2=float(entero)
# print(e1,e2)

# decimal=15.95 #---> cadenas
# d1=str(decimal)
# d2=int(round(decimal,0))
# print(d1,d2)

cadena="20" #---->int/float
c1=float(cadena)

cadena="20.563"#---->float
c2=float(cadena)

cadena=""#---> Solo cuando esta vacio retorna False
c3=bool(cadena)
print(c3)


valor_verdad=True


#Entrada y salida de datos

# nombre=input("ingrese su nombre: ")#---> a traves del input, todo lo que se escriba se guardara como str
# edad=input("Ingrese su edad: ")

# anio_nacimiento=2022-int(edad)
# print(anio_nacimiento)


#Operaciones relacionales
# nombre="Steven"
# nombre2=input("Ingrese un nombre: ")
#igualdad
# verificacion=nombre==nombre2
# print(verificacion)

# num=input('Ingrese un numero: ')#10.0
# verificacion=10==float(num)
# print(verificacion)

#desigualdad
# materia=input("Ingrese una materia: ")
# verificacion='Calculo'!=materia
# print(verificacion)

#Mayor,menor
# numero1=int(input('Ingrese un numero: '))
# verificacion=numero1<100
# print(verificacion)

#conectores logicos
# edad=20
# nombre='Steven'
# ed=int(input('Ingrese la edad: '))
# nom=input("Ingrese el nombre: ")
# verificacion=edad==ed or nombre==nom
# print(verificacion)

# estudiantes=45
# cantidad=int(input("Ingrese una cantidad de estudiantes: "))
# verificacion=not(estudiantes==cantidad)#---> estudiantes!=cantidad #and---> or   #> ----> <=
# print(verificacion)

