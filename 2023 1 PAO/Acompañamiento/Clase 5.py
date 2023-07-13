###################################
#FUNCIONES
###################################


#Funciones ya definidas
# print()
# input()
# list()
# str()
# max()

#Como definimos funciones

#def [nombre de la funcion]([lista de parametros]):
#--> (bloque de codigos)
#--> (bloque de codigos)
#--> (bloque de codigos)
#--> return [el valor que devuelve nuestra funcion]

#Funciones
def suma(num1,num2,num3=5):
    resultado=(num1+num2)*num3
    return resultado

def cuadrado(num1:int):
    num2=num1**2
    return(num2)

#MAIN
# numero1=int(input("Ingrese el primer numero: "))
# numero2=int(input("Ingrese el segundo numero: "))
# numero3=int(input("Ingrese el tercer numero: "))
# resultado=suma(numero1,numero2)
# print(resultado)

def maximo(lista:list[int]):
    resultado=max(lista)
    lista[-1]=5
    return resultado


#MAIN
# numeros=[1,6,7,9,10,23]
# maxima=maximo(numeros)
# print(maxima)
# print(numeros)

#####################################################
#EJERCICIO 1
#####################################################
#Multiplicar alternadamente por 1 o 3, los primeros 12 digitos de izquierda a derecha
#Sumar todas esas multiplicaciones
#Obtener el residuo de dividir por 10 el resultado de la suma
#Se va a restar 10-residuo
#Si el valor final es 10, entonces el digito verificador es 0, caso contrario sera el resultado anterior
#FUNCION
def verificacion(isbn:str):#9783161484100
    suma=(int(isbn[0])*1)+(int(isbn[1])*3)+(int(isbn[2])*1)+(int(isbn[3])*3)+(int(isbn[4])*1)+(int(isbn[5])*3)+(int(isbn[6])*1)+(int(isbn[7])*3)+(int(isbn[8])*1)+(int(isbn[9])*3)+(int(isbn[10])*1)+(int(isbn[11])*3)
    residuo=suma%10
    resultado=10-residuo
    if(resultado==10):
      verificador=0
    else:
      verificador=resultado

    final=int(isbn[-1])==verificador
    return final



# x=verificacion("9783161484100")
# print(x)



# A usted lo ha contratado una clínica veterinaria para procesar datos que tienen en su 
# sistema para poder graficarlos más tarde, tranquilo/a, usted solo solo va a procesar los datos. 
# Los datos que trabajar lucen algo parecido a los siguientes: 
nombres = ["Morty", "Venus", "Pikachu", "Piolin", "Chumi"] 
especie = ["Gato", "Perro", "Hamster", "Ave", "Tortuga"] 
peso = [4.6, 11.0, 0.04, 0.3, 1] 
edad = [4, 3, 1.5, 3, 2]
# Estas listas son paralelas. Es decir, todos los datos en el índice i en las cuatro listas 
# pertenecen a la misma mascota.
# Nota: Todos estos son datos referenciales y no representan datos reales, 
# usted no sabe los datos ni la longitud de las listas, 
# solo conoce el tipo de información guardada en cada una de ellas.


#Implementar funcion que con el nombre de la mascota, mostrara todos sus datos

   
def showInfo(nombre:str,nombres=nombres,especies=especie,pesos=peso,edades=edad):
   indice=nombres.index(nombre)
   print("La mascota es un:",especies[indice])
   print("La mascota pesa {} lbrs".format(pesos[indice]))
   print("La mascota tiene {} anios".format(edades[indice]))



