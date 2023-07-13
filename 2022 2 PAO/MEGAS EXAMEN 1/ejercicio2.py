# RIKAFE es una productora de café local que desea comenzar a internacionalizarse.
# Para asegurar la comercialización de su producto, ha solicitado a varias proveedoras las 
# cotizaciones por los servicios de la recolección, mano de obra, transporte e insumos.
# Los valores de las cotizaciones, en millones de dólares, se encuentran en las siguientes listas, 
# en el orden correspondiente.
nombreProveedoras = ["FEITA S.A.", "Chikitita S.A.", "Brafe", "SIC", "Dollman"]
costosRecoleccion = [6.58, 2.07, 8.11, 3.05, 3.51]
costosManoObra = [1.39, 3.98, 6.88, 8.49, 5.03]
costosTransporte = [0.87, 8.35, 5.52, 9.25, 4.27]
costosInsumos = [9.94, 7.22, 9.92, 9.44, 9.02]
# Implemente las siguientes funciones:
# 1. Función que retorne 3 cosas:
# • El promedio de todos los costos de Recolección
# • La proveedora con el costo de Recolección más alto
# • La proveedora con el costo de Recolección más bajo.
# Para ello la función deberá tener como parámetros el listado de proveedoras y
# el listado de los costos de recolección.


def cRecoleccion(proveedoras,recoleccion):
  promedio=sum(recoleccion)/len(recoleccion)

  maximo=max(recoleccion)
  i_alto=recoleccion.index(maximo)
  mas_alto=proveedoras[i_alto]

  minimo=min(recoleccion)
  i_bajo=recoleccion.index(minimo)
  mas_bajo=proveedoras[i_bajo]


  return promedio,mas_alto,mas_bajo


# Función que obtenga el listado de proveedoras cuyos costos de Mano de Obra sean menores al indicado. 
# La función deberá tener como parámetros el listado de proveedoras, listado de costos de Mano de Obra y el costo de 
# mano de obra límite. Se retornará un listado con las proveedoras que tengan el costo de Mano de Obra menor al límite.

def cmObra(proovedoras,costosMO,limite):
  p=[] #Las proovedoras que tengan costo menor al limite

  for i in range(len(proovedoras)):
    if costosMO[i]<limite:
      p.append(proovedoras[i])

  return p


# Función que muestre los nombres de las Proveedoras de acuerdo a su costo de Insumos de mayor a menor. 
# La función recibirá el listado de proveedoras y el listado de costos de Insumos.

def orden(proovedoras:list[str],costosI:list[int]): #[9,8,,98,1]
  ordenada=[]

  copiaCI=costosI.copy()#[98,9,8,1]
  copiaCI.sort(reverse=True)#El reverse=True es para ordenarlo de manera descendente

  for i in range(len(copiaCI)):
    indice=costosI.index(copiaCI[i])
    ordenada.append(proovedoras[indice])

  # print(ordenada)
  for elemento in ordenada:
    print(elemento)



orden(nombreProveedoras,costosInsumos)