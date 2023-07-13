#*****************************Ejercicio 1: Adivina las letras de una palabra ************)
#El sistema debe generar una palabra aleatoria de 15 letras usando solo las letras: A, C, B, O ,L ,M, N, I, P, E.
#El sistema pedirá al usuario ingresar 3 letras (puede repetir): A, C, B, O ,L ,M, N, I, P, E.
#El sistema le dará un punto por cada vez alguna de las letras ingresadas se repita en la palabra.
#Si obtiene más de 7 puntos, le muestra el siguiente mensaje “Usted es un gran adivino”
#Si obtiene desde 3 hasta 7 puntos, le muestra el siguiente mensaje “Usted debe seguir practicando para mejorar”
#Si obtiene menos de 3, le muestra el siguiente mensaje “Usted debe buscar otro juego”
#Debe mostrar la palabra generada aleatoriamente al final.




#******************************Ejercicio 2: Calcular días (20puntos)********************+
#El sistema debe pedir la fecha de nacimiento de una persona en el siguiente formato: dd/mm/aaaa y validelo.
nacimiento=input("Ingrese su fecha de nacimiento en el formato dd/mm/aaaa: ")

#nacimiento.count("/")==2 and len(nacimiento)==10

while not(nacimiento.count("/")==2 and len(nacimiento)==10):
  nacimiento=input("Ingrese la fecha en un formato correcto: ")

#Con esa información debe calcular lo siguiente:
#La cantidad de días que ha vivido
#Para facilitar los calcular los días debe considerar que todos los meses tienen 30 días.
actual=[24,11,2022]
fecha=nacimiento.split("/") #---> ["28","05","2002"] --->3
                            #        0    1     2


dia=int(fecha[0])
mes=int(fecha[1])
anio=int(fecha[2])

if actual[1]>mes:
  edad=fecha[2]-anio

elif actual[1]<mes:
  edad=fecha[2]-anio-1

else:
  if dia>=fecha[0]:
    edad=fecha[2]-anio
  else:
    edad=fecha[2]-anio-1

diashastacumple=edad*365



#***************************Ejercicio 3: Ventas vs Gastos (30 puntos)******
#Se tienen tres listas:
listaAnio=["2014", "2015", "2016", "2017", "2018", "2019", "2020" , "2021"]
listaVenta=[9192, 4367, 3768, 7893, 4590, 8320, 9256, 2489]
listaGasto=[2900, 2389, 3980, 3209, 4567, 3498, 2256, 3000]
#Por ejemplo: en el 2014 se vendió 9892 y gastaron 2900
#El sistema buscar o recorrer las listas para mostrar lo siguiente
# El año con mayor venta y el monto de venta #con funcion sort
# El año con menor gasto y el monto de gasto
# El año con mayor utilidad (Venta-Gasto) y el monto de la utilidad.



#********************************EJERCICIO4****************************
#Ejercicio 4: Menú y Funciones (20 puntos)
#Cree un menú de opciones con el detallado a continuación:
#Ingrese 0 para ir al juego “Adivina las letras de la palabra”
#Ingrese 1 para ir a “Calcular edades”
#Ingrese 2 para ir a “Ventas vs Gastos”
#Ingrese 3 para salir
#Adicionalmente debe crear métodos/funciones para las operaciones de:
#Menú
#Juego “Adivina las letras de la palabra”
#“Calcular edades”
#“Ventas vs Gastos


def adivinar():
  print("Adivina las letras de la palabra")

def calcular():
  print("")

def ventasVSgastos():
  print("Ventas vs Gastos")
def menu():
  if opcion=="0":
    adivinar()
  elif opcion=="1":
    calcular()
  elif opcion=="2":
    ventasVSgastos()
  elif opcion=="3":
    print("Bye Bye!")
  else:
    print("Eso no es una opcion valida")

#main
opcion=""
while opcion!="3":
  opcion=input("Ingrese una opcion: ")
  menu()