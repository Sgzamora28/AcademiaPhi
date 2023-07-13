# from cmath import pi


# figuras=['Cuadrado','Triangulo','Ciruclo','Rectangulo']
# print(figuras)

# opcion=''
# while opcion!='*':
#   opcion=input("Ingrese el nombre o el indicie de la figura a calcular: ").title()#CuaDRAdo---> Cuadrado

#   if opcion.isdigit():
#     opcion=int(opcion)

#   print(opcion)


#   if opcion=='Cuadrado' or opcion==0:
#     print('La figura es un cuadrado\nA continuacion, ingrese los lados del cuadrado.')
#     lados=input()
#     area=int(lados)**2
#     perimetro=4*int(lados)

#   elif opcion=='Triangulo' or opcion==1:
#     print('La figura es un triangulo rectangulo\nA continuacion, ingrese los lados del rectangulo.')
#     cateto1=int(input('Ingrese la medida del cateto 1:'))
#     cateto2=int(input('Ingrese la medida del cateto 2:'))
#     hipotenusa=((cateto1**2)+(cateto2**2))**(1/2)
#     perimetro=hipotenusa+(cateto1)+(cateto2)
#     area=(cateto1*cateto2)/2  

#   elif opcion=='Circulo' or opcion==2:
#     radio=input("Ingrese el radio del ciuculo: ")
#     perimetro=2*float(radio)*pi
#     area=pi*(float(radio)**2)


#   elif opcion=='Rectangulo' or opcion==3:
#     base=input("Ingrese la base del rectangulo: ")
#     altura=input("Ingrese la altura del rectangulo: ")
#     perimetro=(2*int(base))+(2*int(altura))
#     area=int(base)*int(altura)

#   if opcion!='*':
#     print("La figura escogida tiene un perimetro de {:.2f} y un area de {:.2f}".format(perimetro,area))




#EJERCICIO 2
# lst_poblacion1=[1983778292993,1029384919913,193842991883,39485849,393948588299]
# lst_poblacion2=[192838489,19293994005,92899190304,239400039,3049589010]

# promedio=sum(lst_poblacion1+lst_poblacion2)/len(lst_poblacion1+lst_poblacion2)
# print(promedio)
# #condiciones correctas---> 500000000>numero>100000
# numero=int(input("ingrese un numero: "))
# while not(500000000>numero>100000):
#   numero=int(input("intente nuevamente"))

# print('FINISH')



#EJERCICIO 3
cedula=input("Ingrese un numero de cedula: ")
ced='2121212120'
result=0
for i in range(len(cedula)):
  x=int(cedula[i])*int(ced[i])
  if x>=10:
    y=str(x)
    x=int(y[0])+int(y[1])
  result+=x
  
resultado=result%10

if resultado!=0:
  resultado=10-resultado

#condiciones correctas-----> (1<=cedula[:2]<=24) and cedula[2]<=6 and cedula[-1]==resultado

while not((1<=int(cedula[:2])<=24) and int(cedula[2])<=6 and int(cedula[-1])==resultado):
  cedula=input("Ingrese un numero de cedula valido: ")

print('Cedula valida')