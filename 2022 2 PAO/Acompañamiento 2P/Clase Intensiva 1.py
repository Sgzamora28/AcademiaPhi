#Sets---> Conjunto

#Se manejan tal como los conjuntos matematicos (operaciones matematicas de conjuntos)
#Los elementos dentro del set no se repiten
#Los conjuntos no mantienen orden---> No se pueden indexar


datos={"Steven","Steven",202101713,20,"Steven",20,20,20}

conjunto=set()



#Diccionarios

#Siempre trabajan a manera de clave:valor
#No mantienen orden----> Se indexan de manera especial (A TRAVES DE CLAVES)
#Se trabaja a traves de sus claves

diccionario={"nombre":"Steven","edad":20,"matricula":202101713}

#Siempre se van a generar listas paralelas entre .keys() y .values()
claves=list(diccionario.keys())
valores=list(diccionario.values())

#Tuplas

#Listas que no se pueden modificar
#Que yo no puedo agregar, eliminar ni cambiar valores de la tupla

tupla=(45,"Steven","Maritima")

#########################################################################################
#########################################################################################
#########################################################################################
#########################################################################################
personas = { 'P1021' : {'alegre', 'fumador', 'hacker', 'deportista'},
             'P1002' : {'hacker','alegre','perezosa','matematico'},
             'P1001' : {'farrero', 'deportista', 'programador', 'fabuloso'},
             'P0911' : {'alegre','deportista','matematico','programador','fumador'} }


#INDICE DE TANIMOTO= CARACTERISTICAS EN COMUN/CARACTERISTICAS ENTRE LAS DOS PERSONAS

# 1. [7 puntos] La función hayEmparejamiento(codigoP1, codigoP2, dicPersonas, aceptacion) que recibe el código de 
# dos personas, el diccionario de personas y el nivel de aceptación (entre 0 y 1). 
# Esta función devolverá una tupla con el valor del índice de Tanimoto y un valor de verdad True en el 
# caso de que haya emparejamiento y False en caso contrario. Hay emparejamiento cuando el valor del índice de Tanimoto
# es superior o igual al nivel de aceptación


def emparejamiento(codigo1,codigo2,dicPersonas,aceptacion):
  total=dicPersonas[codigo1].union(dicPersonas[codigo2])
  comun=dicPersonas[codigo1].intersection(dicPersonas[codigo2])
  tanimoto=len(comun)/len(total)

  if tanimoto>=aceptacion:
    return tanimoto,True

  else:
    return tanimoto,False

#########################################################################################
#########################################################################################
#########################################################################################
#########################################################################################
# Para administrar la nueva matriz energética del Ecuador, se dispone de un diccionario con la información 
# de las plantas de energía y las ciudades que atienden cada una.
# Cada ciudad tiene: una tupla con los consumos mensuales (12) del año en megavatios-hora (MWh) y 
# la tarifa de consumo en dólares por megavatio-hora (MWh) que le cobra la planta eléctrica.
# Una ciudad puede estar servida por más de una planta eléctrica. 
# No todas las ciudades son servidas por todas las plantas eléctricas.

consumos = {
            'Coca Codo Sinclair': { 'Quito': { 'consumos':(400, 432, 400, 432, 420, 432, 460, 432, 400, 432, 300 , 213),'tarifa': 65},
                                    'Guayaquil': { 'consumos': (120, 55, 32, 120, 75, 32, 150, 55, 32, 120, 97, 32),'tarifa': 84},
                                  },
            'Sopladora': {
                          'Guayaquil':{ 'consumos': (310, 220, 321, 310, 220, 321, 310, 220, 321, 310, 220, 321),'tarifa':55},
                          'Quito': { 'consumos': (400, 432, 587, 400, 432, 587, 400, 432, 587, 400, 432, 587),'tarifa': 79},
                          'Loja': { 'consumos': (50, 32, 32, 50, 32, 32, 50, 32, 32, 50, 32, 32),'tarifa': 32},
                        },
            }
# Además, dispone del siguiente diccionario con información de ciudad por región :

informacion={
							'costa': ('Guayaquil', 'Manta'),
							'sierra': ('Quito', 'Ambato','Loja'),
							'oriente': ('Tena', 'Nueva Loja')}
# Implemente lo siguiente:
# Una función total_anual(consumo_energia, planta, ciudad) que recibe el diccionario consumo_energia, 
# el nombre de una planta y el nombre de una ciudad. La función debe calcular y retornar el total anual de 
# megavatios-hora servido por planta a ciudad.

def total_anual(consumo_energia,planta,ciudad):
  total=0

  for central in consumo_energia:
    if central==planta and ciudad in consumo_energia[central]:
      total+=sum(consumo_energia[planta][ciudad]["consumos"])

  return total

# Una función total_plantas_ciudad(consumo_energia, ciudad) que recibe el diccionario consumo_energia 
# y el nombre de una ciudad. La función debe devolver un diccionario cuyas claves corresponden a 
# los nombres de las plantas generadoras que proveen energía a ciudad y los valores corresponden al 
# total anual de megavatios-hora servido por cada planta a ciudad.

def total_plantas_ciudad(consumo_energia,ciudad):
  diccionario={}
  for central in consumo_energia:
    if ciudad in consumo_energia[central]:
      diccionario[central]=total_anual(consumo_energia,central,ciudad)
  
  return diccionario



# Una función megavatios_hora(consumo_energia, informacion) que recibe el diccionario consumo_energia 
# y el diccionario informacion. La función retorna el total anual de megavatios-hora 
# consumido por todas las ciudades de la región COSTA.

def megavatios_hora(consumo_energia,informacion):
  total=0
  for ciudad in informacion["costa"]:
    plantas=total_plantas_ciudad(consumo_energia,ciudad).values()
    consumoXciudad=sum(plantas)
    total+=consumoXciudad


  return total

# Una función facturacion(consumo_energia) que recibe el diccionario consumo_energia y 
# genera un archivo con la facturación total en dólares de los seis primeros meses de cada planta 
# generadora. El archivo resultante se llamará ’facturacion.txt’ y tendrá la siguiente estructura: