# Asuma que tiene un archivo con la información de los productos agrícolas cosechados por una hacienda durante
# todos los días del año 2018. La información se encuentra en el siguiente formato:
# codigo1,codigo2,codigo3,...,codigoN
# codigo_producto,fecha(dd-MMM-aaaa),cantidad_cosechada
# Ejemplo:
# 100034,100312,100021,...,201245,432198
# codigo_producto,fecha(dd-MMM-aaaa),cantidad_cosechada
# 100034,02-ENE-2018,5 
# 100021,02-ENE-2018,15
# 100021,07-ENE-2018,11
# 432198,20-ENE-2018,12
# ...
# Nota: La primera línea del archivo contiene los códigos de todos los productos agrícolas presentes en el resto del
# archivo, mientras que la segunda línea es la cabecera del archivo.
# Implemente las siguientes funciones:
import numpy as np

# [8 puntos] crearMatriz(nomArchivo) que recibe el nombre del archivo con la información de las cosechas de un
# año; y devuelve un vector con todos los códigos de productos y una matriz con los totales (valores enteros) de
# cosechas para cada producto (filas) durante cada mes del año (columnas).


def crearMatriz(archivo):
  meses=["ENE","FEB","MAR","ABR","MAY","JUN","JUL","AGO","SEP","OCT","NOV","DIC"]
  with open(archivo) as arch:
    codigos=np.array(arch.readline().strip().split(","))#---->[100034 100312 100021 201245 432198]
    matriz=np.zeros((codigos.size,12),int) 
    arch.readline()
    for line in arch:
      codigo,fecha,cosecha=line.strip().split(",")#"100034","02-ENE-2018","43"
      fila=np.where(codigos==codigo)
      mes=fecha.split("-")[1]#["02","ENE","2018"]--->"ENE"
      columna=meses.index(mes)
      matriz[fila,columna]+=int(cosecha)

  return codigos,matriz


# [5 puntos] mesMasRentable(M) que recibe la matriz de cosechas M. Esta función retorna el nombre del mes
# en que más se cosechó y el total de cosecha de ese mes.
def mesMasRentable(cosechas):
  meses=["ENE","FEB","MAR","ABR","MAY","JUN","JUL","AGO","SEP","OCT","NOV","DIC"]
  suma_mes=np.sum(cosechas,axis=0).ravel() 
  i_mayor=np.argmax(suma_mes)
  cosecha=np.max(suma_mes)
  mes=meses[i_mayor]

  return mes,cosecha


# [8 puntos] altoBajos(M, k) que recibe la matriz de cosechas M y un entero k. La función retorna el nombre de
# todos los meses que tienen una cosecha total con al menos k unidades por debajo de la cosecha del mejor mes
# del año.

def altoBajos(cosechas,k):
  meses=["ENE","FEB","MAR","ABR","MAY","JUN","JUL","AGO","SEP","OCT","NOV","DIC"]
  suma_mes=np.sum(cosechas,axis=0).ravel()#suma por columna
  # k<=cosecha<cosecha_mayor ---->  k<=cosecha & cosecha<cosecha_mayor
  cosecha_mayor=mesMasRentable(cosechas)[1]
  # i_condicion=np.where(suma_mes,((k<=cosechas) & (cosechas<cosecha_mayor)))
  condicion= k<=cosechas & cosechas<cosecha_mayor
  return np.array(meses)[condicion]


# [9 puntos] mejorTrimestre(M, Cod, codigo) que recibe la matriz de cosechas M, el vector de códigos Cod y el
# codigo de un producto. La función debe retornar el nombre del trimestre ("T1", "T2", "T3" o "T4") en el que más
# se cosechó el producto con codigo.

def mejorTrimestre(cosechas,codigos,codigo):
  trimestres=["T1","T2","T3","T4"]
  i_codigo=np.where(codigos==codigo)
  cosechas_indexada=cosechas[i_codigo,:].ravel()#[valor1 valor2 valor3 valor4 valor5 valor6 valor7 valo8 valor9 valor10 valor11 valor12]
                                                #    0     1      2       3      4      5     6      7     8      9        10      11
  ganador=0
  i_ganador=0
  x=0

  # lista_sumas=[]
  for i in range(4):
    indexada=cosechas_indexada[x:x+3]
    suma=np.sum(indexada)
    
    if suma>ganador:
      ganador=suma
      i_ganador=i
    
    x+=3
  
  return trimestres[i_ganador]
  # if i_ganador==0:
  #   return "T1"

  # elif i_ganador==1:
  #   return "T2"

  # elif i_ganador==2:
  #   return "T3"

  # else:
  #   return "T4"