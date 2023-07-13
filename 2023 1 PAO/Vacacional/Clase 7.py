##################################################
#EJERCICIO 1
##################################################
# Escriba un programa que lea la cantidad de Kw que ha consumido una familia en su hogar por el
# consumo de energía eléctrica mensual. Dado que, el precio de 1 Kw es de $0.15. Si el consumo es
# mayor a 700, incremente el precio en 5% solo para el exceso de Kw sobre 700 (Si el consumo es de
# 734, el exceso será 34). Muestre el valor total a pagar.

#100%--> 1
#15%--> 0.15
#5% --> 0.05

# kw=float(input("Ingrese una cantidad de Kw: "))
# precioXkw=0.15
# if kw>700:
#     excendente=kw-700
#     print(excendente)
#     total_pagar=(700*precioXkw)+(excendente*(precioXkw*0.05))

# else:
#     total_pagar=kw*precioXkw

# print("Usted debe pagar ${:.2f} en total".format(total_pagar))



##################################################
#EJERCICIO 2
##################################################

# Se tiene una lista de datos con la información de la cantidad de personas que ha inmigrado de
# cada país y su capital. Un ejemplo de lista es:
lst_datos = ["España|132|Madrid", "EEUU|242|Washington",
"Italia|354|Roma","Ecuador|200|Quito","España|50|Madrid" ]
#pais|cantidad de inmigrantes|capital del pais
# Implementar un programa en Python que, utilizando la lista de datos, muestre por pantalla otra
# lista con el total de inmigrantes de 3 países solicitados al usuario por teclado.
# Por ejemplo, si el usuario quiere saber el total de inmigrantes de Ecuador, Italia, y Brasil, la
# respuesta podría ser:
# [324,354,123]
# #cada valor representa a Ecuador, Italia y Brasil respectivamente

# ingreso=input("Ingrese tres paises separados por comas: ")
# #"Ecuador,Italia,Brasil" ---> split
# paises=ingreso.split(",")#["Ecuador","Italia","Brasil"]
# inmingrantes=[0]*3 #---   [    0,        0,       0   ]
# for i in range(len(paises)):#Ecuador
#     for datos in lst_datos:#"Ecuador|132|Quito"
#         p,cantidad,capital=datos.split("|")#["Ecuador","132","Quito"]
#         cantidad=int(cantidad)#"132"---> 132
#         if paises[i]==p:
#             inmingrantes[i]+=cantidad

# print(inmingrantes)


##################################################
#EJERCICIO 3
##################################################
# Se necesita calcular el sueldo a pagar a un empleado por un día de trabajo. Para esto se solicita
# al usuario el ingreso de un valor a pagar por una hora de trabajo, el total de horas trabajadas
# ese día y si fue feriado o no. Si el empleado trabaja 8 horas o menos, el sueldo a pagar es el
# total de horas multiplicado por el valor de la hora. En caso contrario, las primeras 8 horas se
# pagan al valor normal y las horas restantes se pagan a valor normal * 1.5
# Si el día fue feriado, cada hora se paga al valor normal * 1.8
# Implemente un programa en Python que muestre por pantalla el total a pagar al empleado, con
# los datos ingresados y bajo las condiciones indicadas.


#Ingreso/datos
# valorXhora=float(input("Ingrese el valor a pagar por hora: "))
# horas=int(input("Ingrese la cantidad de horas trabajadas: "))
# feriado=input("Las horas trabajadas fueron en feriado?: ").lower()

# #Desarrollo
# if feriado=="si":
#     totalPagar=horas*(valorXhora*1.8)

# elif feriado=="no":
#     if horas<=8:
#         totalPagar=horas*valorXhora

#     else:
#         excendente=horas-8
#         totalPagar=(8*valorXhora)+(excendente*(valorXhora*1.5))
# else:
#     print("No ingreso una opcion valida en el feriado")
#     totalPagar=0

# print("El empleado trabajo un total de {} horas. El valor por hora es ${:.2f}. Entonces se\
# le pagara un total de ${:.2f}".format(horas,valorXhora,totalPagar))

##################################################
#EJERCICIO 4
##################################################
# El juego de mesa Scrabble es un juego donde se forman palabras en un tablero, 
# a las cuales se les
# asigna un puntaje. Las palabras pueden crearse cruzándolas con palabras ya existentes 
# en el tablero. El ganador es quien más puntos haya obtenido

# A su equipo se le ha encargado la implementación de este juego. En particular, 
# tiene que implementar un
# programa que asigne puntaje a las palabras. 
# Cada letra tiene una puntuación, mostrada abajo:
###################################################
import string
def listAlphabet():
  return list(string.ascii_uppercase)

abc=listAlphabet()
puntos=[1,3,3,2,1,4,2,4,1,9,5,1,3,1,1,3,10,1,1,1,1,4,4,9,4,10]
###################################################

# Las letras compartidas entre palabras reciben el doble de puntos . 
# Su programa recibirá una secuencia
# de palabras, separadas por comas , ingresada por el usuario por teclado y 
# determinará el puntaje de
# cada una. Para denotar una letra compartida, la misma será 
# sucedida por el símbolo “*”. Asuma que
# todas las palabras terminan con una letra compartida . 
# Todas las letras ingresadas deben ser
# mayúsculas. Si se ingresa un letra minúscula, esta es ignorada (puntuación de 0 para dicha letra) .
# Finalmente, se debe determinar la palabra con mayor puntaje.

# Una corrida ejemplo del programa sería:
# Ingrese las palabras a calificar: CAS*A*,S*ASTR*E*,R*EY*,A*ZOTE*
# Las calificaciones de las palabras son:
# casa: 8
# sastre: 9
# rey: 11
# azote: 16
# La palabra con mayor puntaje es AZOTE (16 puntos).


#Ingreso de datos
palabras=input("Ingrese las palabras a calificar: ")#"CAS*A*,S*ASTR*E*,R*EY*,A*ZOTE*"
palabras=palabras.split(",")#[CAS*A*,S*ASTR*E*,R*EY*,A*ZOTE*]
puntos_totales=[]
print("Las calificaciones de las palabras son:")
for palabra in palabras:
  puntaje=0
  for i in range(len(palabra)): #0 --->C
    if palabra[i]!="*":
      indice=abc.index(palabra[i])
      pts=puntos[indice]
      if palabra[i+1]=="*":
        pts*=2
      puntaje+=pts
  palabra=palabra.replace("*","").lower()
  puntos_totales.append(puntaje)
  print("{}: {}".format(palabra,puntaje))

maximo=max(puntos_totales)
indice_maximo=puntos_totales.index(maximo)
palabraGrande=palabras[indice_maximo]
palabraGrande=palabraGrande.replace("*","")
print("La palabra con mayor puntaje es {} ({} puntos).".format(palabraGrande,maximo))