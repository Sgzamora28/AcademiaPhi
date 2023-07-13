import numpy as np

paises={"II":"II","Ec":"Ec","Fa":"Fa"}

def crearMatriz(nombre,anio,trimestre):
  # datos=np.zeros((9,len(paises)*3),int)
  datos=np.zeros((10*3,9),int)
  # paises=np.array(list(paises.keys))
  rango=np.arange(1,4)#1,2,3
  if trimestre==2:
  #2 trimestre---> 4,5,6
    rango+=3

  elif trimestre==3:
  #3 trimestre---> 7,8,9
    rango+=6


  elif trimestre==4:
  #4 trimestre---> 10,11,12
    rango+=9
  with open(nombre) as arch:
    arch.readline()
    i=0
    j=0
    for line in arch:
      l_datos=line.strip().split(",")
      if anio==int(l_datos[0]):
        if int(l_datos[1]) in rango:
          valores=l_datos[-3:]
          for x in range(len(valores)):
            datos[i,j]=valores[x]
            j+=1
            if j>8:
              j=0
              i+=1





  return datos



matriz=crearMatriz("estadisticas.csv",2021,1)
print(matriz)


#1 punto
matriz_indexada=matriz[::3,::3]
print()
# print(matriz_indexada)
# print()
#paises
suma=np.sum(matriz_indexada,axis=1)
# print(suma)

indice_top10=np.argsort(suma)[::-1]
# top10=paises[indice_top10]
# print(indice_top10)


#2 punto
matriz_indexada2=matriz[2::3,2::3]
# print(matriz_indexada2)
# print()
m_i1=matriz_indexada2[:,0].ravel()
m_i2=matriz_indexada2[:,1].ravel()
m_i3=matriz_indexada2[:,2].ravel()
matriz_resta=m_i1-m_i2-m_i3
# print(matriz_resta)
# print()
indice_top5=np.argsort(matriz_resta)[::-1][:5]
# print(indice_top5)
# top5=paises[indice_top5]

matriz_indexada3=matriz[::3,::3]+matriz[1::3,::3]+matriz[2::3,::3]
suma2=np.sum(matriz_indexada3,axis=1)
indice_top3=np.argsort(suma2)[::-1][:3]
# top3=paises[indice_top3]

matriz_indexada4=matriz[1::3,1::3]
promedio=np.mean(matriz_indexada4,axis=1)
print(promedio)
inidce_menor=np.argmin(promedio)
#menor=paises[indice_menor]