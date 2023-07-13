
def adivinar():
  from random import choice
  letras=['A','C','B','O','L','M','R','I','P','E']
  adivinar=''
  for i in range(15):
      adivinar+=choice(letras)

  #intentos
  puntos=0
  for i in range(3):
    usuario=input('Ingrese una letra de la lista: {}\n'.format(letras)).upper()
    while usuario not in letras:
      usuario=input('Debe ingresar solamente una de las letras dentro de la lista. Intente de nuevo: ').upper()
    if usuario in adivinar:
      puntos+=adivinar.count(usuario)

  print('Usted obtuvo {} punto(s)'.format(puntos))
  if puntos>7:
    print('Usted es un gran adivino')
  elif 3<=puntos<=7:
    print('Usted debe seguir practicando para mejorar')
  else:
    print('Usted debe buscar otro juego')


def calcularEdades():
  edad1=0
  edad2=0
  actual=2022
  mayor='Persona 1'
  for i in range(2):
    fecha=input('Ingese su fecha de nacimiento en el formato DD/MES/AAAA: ').upper()
    #condiciones correctas len(fecha)==11 and fecha.count('/')==2 and fecha[-4:].isdigit() and (fecha[:2].isdigit() and int(fecha[:2])<=31)
    while not(len(fecha)==11 and fecha.count('/')==2 and fecha[-4:].isdigit() and int(fecha[-4:])<actual and (fecha[:2].isdigit() and int(fecha[:2])<=31)):
      fecha=input('Ingese correctamente el formato de la fecha: ').upper()
    edad=actual-int(fecha[-4:])
    if i==0:
      edad1=edad
    
    else:
      edad2=edad

  if edad2>edad1:
    mayor='Persona 2'

  elif edad1==edad2:
    mayor='ninguno'

  print('La edad de la persona 1 es {} y la edad de la persona 2 es {}. Por lo tanto {} es mayor'.format(edad1,edad2,mayor))


def ventasVSgastos(listaAnio,listaVenta,listaGasto):
  mayor_venta=max(listaVenta)
  anio1=listaAnio[listaGasto.index(mayor_venta)]
  print('El anio con mayores ventas fue {}, con un total de {} ventas'.format(anio1,mayor_venta))

  menor_gasto=min(listaGasto)
  anio2=listaAnio[listaGasto.index(menor_gasto)]
  print('El anio con menores gastos fue {}, con un total de {} gastos'.format(anio2,menor_gasto))


  mayor_utilidad=0
  anio3=''

  for i in range(len(listaAnio)):
    utilidad=listaVenta[i]-listaGasto[i]
    if utilidad>mayor_utilidad:
      mayor_utilidad=utilidad
      anio3=listaAnio[i]

  print('El anio con mayores utilidades fue {}, con un total de {} utilidades'.format(anio2,mayor_utilidad))


def menu():
  opcion=''
  while opcion!='3':
    listaAnio=[]
    listaVenta=[]
    listaGasto=[]
    opcion=input('Ingrese 0 para jugar "Adivina las letras de la palabra"\nIngrese 1 para calcular edades\nIngrese 2 para ir a ventas/gastos\nIngrese 3 para salir: ')
    while not(opcion.isdigit() and int(opcion) not in range(3)):
      opcion=input('Ingrese 0 para jugar "Adivina las letras de la palabra"\nIngrese 1 para calcular edades\nIngrese 2 para ir a ventas/gastos\nIngrese 3 para salir: ')

    if int(opcion)==0:
      adivinanza=adivinar()
    
    elif int(opcion)==1:
      calculo=calcularEdades()
    
    elif int(opcion)==2:
      ventas_gastos=ventasVSgastos(listaAnio,listaVenta,listaGasto)
    
    else:
      print('Adios')
      


print(menu())
