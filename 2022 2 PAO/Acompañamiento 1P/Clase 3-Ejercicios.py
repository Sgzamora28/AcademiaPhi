import math as mth
#Ejercicio 1

# sector|tienda|categoria|producto|totalVentas|dia-mes-año
transacciones = [ 'centro|Bahia|futbol|zapatos-Adidas|290.78|25-03-2013',
                  'centro|Malecon2000|natacion|chaleco-Fins|110.92|01-02-2014',
                  'sur|MallDelSur|natacion|gafasPiscina-Swingo|90.07|13-05-2014',
                  'centro|Bahia|natacion|zapatos-Nike|315.72|13-12-2015',
                  'norte|CityMall|natacion|gafasPiscina-Adidas|310.19|31-05-2016',
                  'norte|RiocentroCeibos|basquetball|balon-Nike|300|29-05-2016',
                  'norte|RiocentroCeibos|futbol|zapatos-Adidas|450|28-05-2016',
                  ]
                  

# Escriba sentencias un programa en Python que, usando la información dada, genere la siguiente
# información:
# 1. Tres listas (sur,centro,norte) cuyos elementos son los nombres únicos de las tiendas: una lista
# por cada sector.
sur=[]
centro=[]
norte=[]

#---> x=['Steven','Mecatronica','202101713']
#nombre,carrera,matricula=x
#nombre=x[0]
#carrera=x[1]
#matricula=x[2]    
for transaccion in transacciones:
  lista=transaccion.split("|") #-----> [sector,tienda,categoria,producto,totalVentas,fecha]

  sector=lista[0]
  tienda=lista[1]

  # tienda in lista ---> True/False

  if sector=='centro' and tienda not in centro:
    centro.append(tienda)

  elif sector=='sur' and tienda not in sur:
    sur.append(tienda)

  elif sector=='norte' and tienda not in norte:
    norte.append(tienda)

# print(sur)
# print(norte)
# print(centro)


# 2. El total de ventas de los productos Adidas en el mes de mayo del año ingresado por teclado.

# anio1=input("Ingrese el anio deseado: ") #---> '2018'
# totalVentas=0
# for trans in transacciones:
#   sector,tienda,categoria,producto,ventas,fecha=trans.split("|")
#   #Fecha---- dia-mes-anio
#   #fecha[-4:]---- 2019-2018-2022
#   dia,mes,anio2=fecha.split('-')
  
#   #condicion---> producto sea Adidas y fecha este en anio ingresado 
#   #condicion---> producto=="Adidas" and fecha==anio XXXXXXXXX
#   #condicion---> 'Adidas' in producto and anio1==anio2 :D
#   if 'Adidas' in producto and anio1==anio2:
#     totalVentas+=float(ventas) #---> '450'


# print("El total de ventas para los productos Adidas para el anio",anio1,"es:",totalVentas)



#Ejercicio 2

# Elabore un programa en Python que realice los cálculos generales de figuras geométricas: (20 puntos)
# • Cálculos geométricos:
# o Crear una lista con los siguientes elementos: [“Cuadrado”, “Triángulo”, “Rectángulo”, “Círculo”])
# o Mostrar la lista al usuario e indicar que deben escoger una figura geométrica. (La puede escoger ingresando el nombre o en índice.
# ▪ Si ingreso el nombre, el sistema debe aceptar cualquier forma de escribirlo: Cuadrado, CUADRADO, cuadrado, CUAdraDO, etc
# o Según la figura seleccionada debe pedir los datos para calcular el área y el perímetro de la figura y mostrarlo al usuario.

figuras=["Cuadrado", "Triángulo", "Rectángulo", "Circulo"]
print(figuras)

#"KYRA AZUCENA"----> .title()---> "Kyra Azucena"
#"KYRA AZUCENA"----> .capitalize()---> "Kyra azucena"

opcion=input("Ingrese el nombre de una figura o su indice: ").title() #---> Cuadrado

area=0
perimetro=0

if opcion=="Cuadrado" or opcion=='0':
  lado=float(input("Ingrese la longitud de los lados del cuadrado: "))
  perimetro=lado*4
  area=lado**2

elif opcion=='Triangulo' or opcion=='1':
  base=float(input("Ingrese la base: "))
  altura=float(input("Ingre la altura: "))
  c=(base**2+altura**2)**(1/2)
  perimetro=base+altura+c
  area=(base*altura)/2

elif opcion=="Rectangulo" or opcion=="2":
  base=float(input("Ingrese la base: "))
  altura=float(input("Ingre la altura: "))
  perimetro=2*base+2*altura
  area=base*altura

elif opcion=='Circulo' or opcion=='3':
  radio=float(input("Ingrese el radio del circulo: "))
  area=mth.pi*(radio**2)
  perimetro=mth.pi*(2*radio)


print("El area y el perimetro calculados son:",round(area,2),round(perimetro,2))
