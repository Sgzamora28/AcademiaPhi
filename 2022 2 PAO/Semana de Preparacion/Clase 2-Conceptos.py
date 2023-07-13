#######################################################
######                   LISTAS                  ######
#######################################################

#Permite datos repetidos
#Son heterogeneas
#Son ordenadas

numero1=34
numero2=19

numeros=[numero1,numero2]
# print(numeros)


x=["Steven","Azucena","Isabel"]
#     0         1         2
#    -3        -2        -1
y=[20,19,21,25,40,40,10,10,10,"Steven",True]


#CANTIDAD DE ELEMENTOS
longitud=len(y)
# print("La longitud de la lista es",longitud)



#Operaciones con listas
#SUMAR
z=x+y
# print(z)


#MULTIPLICACION
z=x*2
# print(z)


#Referenciar-Indexamiento ---- Slicing
listaReves=y
# print(listaReves)

#Para usar index, el emento debe existir
# posicion=y.index("steven")
# print(posicion)

#Pertenencia
comprobacion1="Steven" in y

#No pertenencia
comprobacion2="steven" not in y
# print(comprobacion1)


#Agregar elementos
y=[20,19,21,25,40,40,10,10,10]
# print(y)
#En una posicion especifica
y.insert(2,"Esto es un elemento agregado")
# print(y)

#Final
y.append("Kevin")
# print(y)












#######################################################
###            ESTRUCTURAS CONDICIONALES            ###
#######################################################



#OPERACION BOOLEANAS/LOGICAS

#Numeros
# numero=int(input("Ingrese un numero cualquiera: "))

#IGUALDAD
# op1= numero == 20
# print(op1)

#DESIGUALDAD
# op2=numero != 30
# print(op2)


#MAYOR/MENOR
# op3=numero>40
# op4= 5<=numero

# print(op3)
# print(op4)

# op5= 15<=numero<20    #[15,20)
# print(op5)


#Strings (Cadenas)

#Comprobar longitud
# palabra=input("Ingrese una palabra: ")
# longitud=len(palabra)
# print(longitud)


# op6=len(palabra)>numero
# print(op6)
# print()


#Comprobar pertenencia
# oracion=input("Ingese una oracion: ")
# op7=palabra in oracion
# print(op7)
# print()




#Booleanos
# op8=op6 and op7
# op9=not(op7) or op6
# print("Op8:",op8)
# print("Op9:",op9)


#Estructura
########################
#Programa principal
########################
# numero=int(input("Ingrese un numero: "))
numero=input("Ingrese un numero: ")
#condiciones correctas del dato ---> numero.isdigit()
while not(numero.isdigit()):
  numero=input("Solo puede ingresar numeros: ")

numero=int(numero)
#numero%2==0


########################
#Bloque condicional
########################
if numero%2 == 0:
  print("El numero es divisible para dos")
  numero+=5


elif numero%3 == 0:
  print("El numero es divisible para 3")
  numero*=2

else:
  print("El numero no es divisible para dos")
  numero+=10
  # numero=numero+10


########################
#Programa principal
########################
print(numero)