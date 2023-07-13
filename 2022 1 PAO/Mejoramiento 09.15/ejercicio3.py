# Asuma que tiene la matriz M cuyas filas representan ciudades del mundo, las columnas representan indicadores de
# innovación y cada celda contiene el valor que tiene la ciudad para un indicador . Además, cuenta con el diccionario
# indicadores con el siguiente formato:

# indicadores = {'Num empresas':{'columna':17, 'puntaje':{(0,9):1, (10,19):2,...}}
# 'Num coworkings':{'columna':5, 'puntaje':{(0,15):10, (16,30):15,...}},
# ... }

import numpy as np

# [14 puntos] obtenerPuntajes(M, indicadores, indicador) que recibe la matriz M, el diccionario de indicadores,
# y el nombre de un indicador; y devuelve un vector con el puntaje obtenido por cada ciudad en ese indicador.
# Por ejemplo: Si una ciudad, tiene un valor de 15 para el indicador 'Num empresas', obtendrá 2 como puntaje.
#     i1 i2 i3
# c1 [[x x x]
# c2  [x x x]
# c3  [x x x]]

#[[x]
# [x]
# [x]] --> [x x x]

def puntajes(matriz:np.ndarray,indicadores:dict,indicador:str):
  i_columna=indicadores[indicador]['columna']
  puntajes=indicadores[indicador]['puntaje']#{(0,15):10, (16,30):15,...}
  vector=matriz[:,i_columna].ravel()
  for i in range(vector.size):
    valor=vector[i]
    for p in puntajes:#p---> (0,15)
      if valor is range(p[0],p[1]+1):#range(0,16)---> [0,16)
        vector[i]=puntajes[p]
  return vector




# indicadores = {'Num empresas':{'columna':17, 'puntaje':{(0,9):1, (10,19):2,...}}
# 'Num coworkings':{'columna':5, 'puntaje':{(0,15):10, (16,30):15,...}},
# ... }

# 2. [12 puntos] crearMatrizPuntajes(M, indicadores) que recibe la matriz M y el diccionario de indicadores; y
# retorna una matriz de puntajes (P) cuyas filas representan ciudades, las columnas representan indicadores y el
# valor de cada celda representa el puntaje obtenido por esa ciudad en ese indicador.

def crearMatriz(matriz:np.ndarray,indicadores:dict):
  puntos=np.zeros(matriz.shape,int)
  # matriz.shape---> (f,c)
  f,c=matriz.shape

  for i in range(f):
    for j in range(c):

      for clave,valor in indicadores.items():
        if j==valor['columna']:
          puntos[i,j]=puntajes(matriz,indicadores,clave)[i]
  
  return puntos