#Tipos de datos

##############
#String---> Cadenas de texto
##############
"Steven ZAmora"
'Fundamentos de Programacion'
"El anio actual es 2022"

##############
#Integer (int)---> Numeros enteros
##############
123
2022
102345112


##############
#Float---> Decimales
##############
12.5
25.0945
12.20


##############
#Boolean ---> Valores de Verdad
##############
True
False


#Ingreso y salida de datos
# nombrePersona=int(input("Ingrese aqui su nombre: "))

x=123.2
nombre="Steven"
verificacion=True

# print("El tipo de dato de la variable es",type(nombrePersona))


#####################################################################
#Ejercicio 1
#####################################################################
# Un cliente compra un libro en una tienda localizada en la frontera con Canadá en 41.27 dólares canadienses. 
# El cliente le da al vendedor 40 dólares americanos (USD) conociendo que el dólar americano tiene un cambio mayor que el canadiense. 
# La política de la tienda es retornar el cambio con el mismo tipo de moneda con la cual paga el cliente. 
# Suponga que un dólar canadiense cuesta 0.72 dólares americanos.

totalPagar=41.27 #Canadienses
efectivo=40 #USD
conversion=0.72

totalPagarUSD=round(41.72*0.72,2)
vuelto=40-totalPagarUSD
# print("El total a pagar en USD es",totalPagarUSD,"El vuelto es igual a",vuelto)

#Digamos que queremos automatizar el proceso de conversion y pago. Cree un programa que dado un valor USD y un total a pagar en CAN Retorne el vuelto en la moneda de pago
# totalPagar=float(input("Ingrese el total a pagar en CAN:"))#34--->34.0
# efectivo=float(input("Ingrese cuanto pago: "))
# tP=round(totalPagar*conversion)
# vuelto=efectivo-tP
# print("El vuelto por su compra es:",vuelto)



#####################################################################
#Ejercicio 2
#####################################################################
# Implemente un programa en Python que solicite al usuario un número que representará una tabla de multiplicar, y mostrar la tabla solicitada entre el 1 y 12. Por ejemplo:
# El usuario elige la tabla del 8: 
# 1 x 8 = 8
# 2 x 8 = 16
# …
# 12 8 = 96

numero=int(input("Ingrese el numero del cual quiere la tabla: "))
print("1 x",numero,"=",1*numero)
print("2 x",numero,"=",2*numero)
print("3 x",numero,"=",3*numero)
print("4 x",numero,"=",4*numero)
print("5 x",numero,"=",5*numero)
print("6 x",numero,"=",6*numero)
print("7 x",numero,"=",7*numero)
print("8 x",numero,"=",8*numero)
print("9 x",numero,"=",9*numero)
print("10 x",numero,"=",10*numero)
print("11 x",numero,"=",11*numero)
print("12 x",numero,"=",12*numero)

