import numpy as np
sectores=np.array([['N','N','N','N','O'],
                   ['O','C','C','C','E'],
                   ['O','C','C','C','E'],
                   ['O','C','C','C','E'],
                   ['S','S','S','S','S']])


multas=[(0,0,120),(1,2,330),(3,4,123),(4,2,62),(0,0,50),(4,4,89),(0,3,25),(2,0,43),(3,2,21),(0,0,120)]

def generador(listaMultas):
  matriz=np.zeros((5,5),float)
  # print(matriz)
  for multa in listaMultas:
    i1,i2,valor=multa
    matriz[i1,i2]+=float(valor)

  return matriz



x=generador(multas)

def sectorTop(matriz):
  multaTop=np.max(matriz)
  top=np.where(matriz==multaTop)
  # print(top)
  ganador=sectores[top]
  tupla=(ganador[0],multaTop)
  return tupla

print(x)
print(sectorTop(x))
  