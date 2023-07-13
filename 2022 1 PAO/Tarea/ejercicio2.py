# Elabore un programa en Python que realice los cálculos generales de figuras geométricas: (20 puntos)
# • Cálculos geométricos:
# o Crear una lista con los siguientes elementos: [“Cuadrado”, “Triángulo”, “Rectángulo”, “Círculo”]
# o Mostrar la lista al usuario e indicar que deben escoger una figura geométrica. La puede escoger ingresando el nombre o en índice.
# ▪ Si ingreso el nombre, el sistema debe aceptar cualquier forma de escribirlo: Cuadrado, CUADRADO, cuadrado, CUAdraDO, etc .lower()
# o Según la figura seleccionada debe pedir los datos para calcular el área y el perímetro de la figura y mostrarlo al usuario.
# 3.
["Cuadrado", "Triángulo", "Rectángulo", "Círculo"]
from math import pi, sqrt

figuras=['Cuadrado', 'Triangulo', 'Rectangulo', 'Circulo']#---> 0 1 2 3 ----> range(len(figuras))

print('Las figuras disponibles para realizar los calculos son: ',figuras)
opcion=input('Ingrese el nombre o el indice de la figura a calcular: ').capitalize()#123----> '123'
#condicion correcta----> opcion.isalpha() or opcion.isdigit()
while not(opcion.isalpha() or opcion.isdigit()):
    opcion=input('Ingrese solamente numeros o solamente el nombre de la figura: ')


if opcion.isalpha():
    #condicion correcta----> opcion in figuras
    while not(opcion in figuras):
        opcion=input('Ingrese correctamente el nombre de la figura: ').capitalize()
    opcion=opcion.capitalize()

elif opcion.isdigit():
    #range(5)----> 0 1 2 3 
    #condicion correcta----> int(opcion) in range(len(figuras))
    while not(int(opcion) in range(len(figuras))):
        opcion=input('Ingrese correctamente el indice: ')
    opcion=int(opcion)


if opcion=='Cuadrado' or opcion==0:
    lado=input('Ingrese la longitud de los lados del cuadrado: ')
    while not(lado.isdigit()):
        lado=input('Ingrese correctamente la longitud: ')
    lado=int(lado)
    p=4*lado
    a=lado**2

elif opcion=='Triangulo' or opcion==1:
    print('Asumiremos que el triangulo es rectangulo')
    base=int(input('Ingrese la base del triangulo: '))
    altura=int(input('Ingrese la altura del triangulo: '))
    lado3=sqrt(base**2+altura**2)
    a=base*altura/2
    p=base+altura+lado3


elif opcion=='Rectangulo' or opcion==2:
    base=int(input('Ingrese la base del rectangulo: '))
    altura=int(input('Igrese la altura del rectangulo: '))
    p=(2*base)+(2*altura)
    a=base*altura


else:
    radio=int(input('Ingrese el radio del ciruclo: '))
    p=2*pi*radio
    a=pi*(radio**2)

if type(opcion)==int:
    print('Para la figura "{}" el perimetro es {:.2f} y el area es {:.2f}'.format(figuras[opcion],p,a))

else:
    print('Para la figura {} el perimetro es {:.2f} y el area es {:.2f}'.format(opcion,p,a))






    