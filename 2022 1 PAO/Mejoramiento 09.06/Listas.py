#Una lista es una coleccion de elementos

from cmath import pi


x=[9,8,83,"Steven",True,False] #---->len=cantidad de elementos
#  0 1  2    3       4    5
# 
# print(x[3:])
# print(8 in x)


###########################################
#Ejercicio 1
###########################################

# Se tiene una lista de datos con la información de la cantidad de personas que ha inmigrado de cada país y su capital. 
# Un ejemplo de lista es: 
lst_datos = ["España|132|Madrid", "EEUU|242|Washington", "Italia|354|Roma", "Ecuador|324|Quito" ] 
# Implementar un programa en Python que, utilizando la lista de datos, muestre por pantalla otra lista con el total de inmigrantes de 3 países 
# solicitados al usuario por teclado. Por ejemplo, si el usuario quiere saber el total de inmigrantes de Ecuador, Italia, y Brasil,
#  la respuesta podría ser: [324,354,123]


x=["Miguel","Menendez","FCV"]
nombre,apellido,facultad=x


# paises=input("Ingrese tres paies separados por espacios: ")#String
# # print(paises)
# l_paises=paises.split(" ")
# # print(l_paiess)
# resultado=[]
# for datos in lst_datos:
#   print(datos)
#   lista=datos.split("|")
#   pais,inmigrantes,capital=lista
#   if pais in l_paises:
#     resultado.append(int(inmigrantes))

# print(resultado)


###########################################
#Ejercicio 2
###########################################
figuras=["Cuadrado","Rectangulo","Triangulo","Circulo"]
print(figuras)

opcion=input("Ingrese el nombre de la figura o su indice: ")


if opcion=="0" or opcion=="Cuadrado":
  lados=int(input("Ingrese la longitud de los lados"))
  perimetro=lados*4
  area=lados**2
  print("El area es",area,"Y el perimetro es igual a",perimetro)

elif opcion=="1" or opcion=="Rectangulo":
  base=input("Ingrese la base")
  altura=input("Ingrese la alutra")
  perimetro=(base*2)+(altura*2)
  area=base*altura
  print("El area es igual a",area,"El perimetro es igual a",perimetro)

elif opcion=="2" or opcion=="Triangulo":
  base=int(input("Ingrese la base"))
  altura=int(input("Ingrese su altura"))
  area=(base*altura)
  perimetro=((base**2+altura**2)**(1/2))*3
  print("El area es",area,"Y el perimetro es igual a ",perimetro)

else:
  radio=int(input("Ingrese el radio del circulo"))
  perimetro=2*pi*radio
  area=pi*radio**2
  print("El area es",area,"El perimetro es igual a",perimetro)

