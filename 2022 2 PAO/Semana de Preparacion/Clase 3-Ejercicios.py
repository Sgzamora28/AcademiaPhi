
############################
#Ejercicio 1
############################

# Elabore un programa en Python que realice los cálculos generales de figuras geométricas: (20 puntos)
# • Cálculos geométricos:
# o Crear una lista con los siguientes elementos: [“Cuadrado”, “Triángulo”, “Rectángulo”, “Círculo”])
# o Mostrar la lista al usuario e indicar que deben escoger una figura geométrica. (La puede escoger ingresando el nombre o en índice.
# ▪ Si ingreso el nombre, el sistema debe aceptar cualquier forma de escribirlo: Cuadrado, CUADRADO, cuadrado, CUAdraDO, etc
# o Según la figura seleccionada debe pedir los datos para calcular el área y el perímetro de la figura y mostrarlo al usuario.

# figuras=["Cuadrado", "Triangulo", "Rectangulo", "Ciruculo"]
# # .upper      ---> TODO EN MAYUS
# # .lower      ---> todo en minuscula
# # .capitalize ---> La primera letra en mayus
# # .title      ---> Todas Las Primeras Letras en Mayus
# print(figuras)
# opcion=input("Ingrese una figura de la lista por su nombre o por su indice: ").capitalize()

# area=0
# perimetro=0

# if opcion=="Cuadrado" or opcion=="0":
#   lado=int(input("Ingrese la longitud del lado del cuadrado: "))
#   area=lado**2
#   perimetro=lado*4

# elif opcion=="Triangulo" or opcion=="1":
#   print("Triangulo rectangulo")
#   base=int(input("Ingrese la base del triangulo: "))
#   altura=int(input("Ingrese la altura del triangulo: "))
#   area=round((base*altura)/2,2)
#   hipotenusa=((base**2)+(altura**2))**(1/2)
#   perimetro=base+altura+hipotenusa

# elif opcion=="Rectangulo" or opcion=="2":
#   base=int(input("Ingrese la base del rectangulo"))
#   altura=int(input("Ingrese la altura del rectangulo"))
#   area=base*altura
#   perimetro=(2*base)+(2*altura)

# elif opcion=="Circulo" or opcion=="3":
#   radio=int(input("Ingrese el radio del circulo: "))
#   area=round(3.1416*(radio**2),2)
#   perimetro=round(2*3.1416*radio,2)

# else:
#   print("No ingreso ninguna figura ni ningun indice valido")

# print("El area y el perimeto de la figura son:",area,perimetro)


############################
#Ejercicio 2
############################
# En una base de datos tiene listas con elementos que almacenan los siguientes datos: 
universidadesCosta=["ESPOL", "UTMACH", "UG", "UEES", "UTM", "UTB"] 
ciudadesUC=["Guayaquil", "Machala", "Guayaquil", "Guayaquil","Portoviejo", "Babahoyo"] 

universidadesSierra=["ESPE", "UTPL", "UPN", "UDLA", "UAZUAY", "UTN"] 
ciudadesUS=["Quito", "Loja", "Quito", "Quito", "Cuenca", "Ibarra"]

# 1.Cree una lista con las universidades de Quito y Guayaquil. Ordene sus nombres de la Z-A
# 2.Cree un listado de ciudades únicas ordenadas (todas las regiones), luego imprima por cada ciudad sus nombres de universidades y 
# cuantas existen en total
# 3.De la siguiente tupla de ciudades ("Loja", "Manta", "Machala", "Salinas", "Esmeraldas","Ibarra") indique cuantas universidades 
# existen para cada ciudad
# 4.De la misma lista de ciudades (ejercicio 2) imprima los nombres de las universidades que noaparecen según la tupla de ciudades

#Punto 1
universidadesQG=[]
for i in range(len(universidadesCosta)):
  if ciudadesUC[i]=="Guayaquil":
    universidadesQG.append(universidadesCosta[i])

for i in range(len(universidadesSierra)):
  if ciudadesUS[i]=="Quito":
    universidadesQG.append(universidadesSierra[i])

print(universidadesQG)#['ESPOL', 'UG', 'UEES', 'ESPE', 'UPN', 'UDLA']
print()
#Punto 2
ciudades=ciudadesUC+ciudadesUS
ciudadesUnicas=[]
for ciudad in ciudades:
  if ciudad not in ciudadesUnicas:
    ciudadesUnicas.append(ciudad)

print(ciudadesUnicas)#['Guayaquil', 'Machala', 'Portoviejo', 'Babahoyo', 'Quito', 'Loja', 'Cuenca', 'Ibarra']

for ciudad in ciudadesUnicas:
  print(ciudad)
  for i in range(len(ciudadesUC)):
    if ciudad==ciudadesUC[i]:
      print(universidadesCosta[i])
  
  for i in range(len(ciudadesUS)):
    if ciudad==ciudadesUS[i]:
      print(universidadesSierra[i])
  print()
