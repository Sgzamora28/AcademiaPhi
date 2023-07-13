##########################################################
#FOR#
##########################################################

#For por indice
#(0 1 2 3 4)
# for patito_feo in range(5):
  # print(patito_feo)


# print(range(5))

#For por contenido
string="Domenica"
# for caracter in string:
  # print(caracter)


lista=["pera","manzana","sandia","mango"]
# for fruta in lista:
#   print(fruta)


#####################################################################
#Ejercicio 2 MEJORADO
#####################################################################
# Implemente un programa en Python que solicite al usuario un número que representará una tabla de multiplicar, y mostrar la tabla 
# solicitada entre el 1 y 12. Por ejemplo:
# El usuario elige la tabla del 8:
numero=int(input("Ingrese un numero: "))
# 1 x 8 = 8
# 2 x 8 = 16
# …
# 12 8 = 96

for i in range(12):
  print(i+1,"x",numero,"=",(i+1)*numero)