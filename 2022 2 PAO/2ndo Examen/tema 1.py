# [10 puntos] Implemente la función llenar_matriz(nom_archivo) que recibe el nombre del archivo con los datos 
# en el formato anterior. La función retorna una tupla con tres valores. 
# El primer valor de la tupla es un vector con los nombres de las farmacias en el archivo. 
# El segundo valor de la tupla es un vector con los nombres de los meses en el archivo. 
# El tercer valor es una matriz de Numpy donde las filas representan las farmacias del archivo, 
# las columnas representan los meses del archivo y las celdas representan el total (acumulado) comprado 
# en dólares en ese mes en esa farmacia.
import numpy as np
def llenar_matriz(nom_archivo):
  with open(nom_archivo) as arch:
    linea1=arch.readline().strip().split(":")[1]
    meses=linea1.split(",")
    vector_meses=np.array(meses)
    linea2=arch.readline().strip().split(":")[1]
    farmarcias=linea2.split(",")
    vector_farmacias=np.array(farmarcias)
    matriz=np.zeros((vector_farmacias.size,vector_meses.size),float)
    arch.readline()
    for line in arch:
      datos=line.strip().split(",") #----> ["2022-OCT-10","Ecu-Vida","14.26"] ---> OCT
      mes=datos[0].split("-")[1] #["2022","OCT","10"]
      farmacia=datos[1]
      i_farmacia=np.where(vector_farmacias==farmacia)
      i_mes=np.where(vector_meses==mes)
      matriz[i_farmacia,i_mes]+=float(datos[2])
    
    # print(matriz)
    return vector_farmacias,vector_meses,matriz


# 2.[10 puntos] Escriba la función total_farmacias(M, etiquetas_farmacias, v_farmacias) 
# que recibe la matriz M generada en el numeral 1, el vector generado en el numeral 1 con los nombres 
# de las farmacias (corresponden a las etiquetas de las filas de la matriz) y otro vector con nombres de 
# ciertas farmacias. La función retornará el valor total por las compras solo en estas farmacias.

def total(matriz,farmacias,vector):
  indices=[]
  for farmacia in vector:
    i=np.where(farmacias==farmacia)[0]
    indices.append(i)
  v_indices=np.array(indices)
  copia_matriz=matriz[v_indices,:]
  # print(copia_matriz)

  return sum(copia_matriz)

# 3.[15 puntos] Escriba la función top_n(M, etiquetas_meses, n) que recibe la matriz M del numeral 1, 
# el vector generado en el numeral 1 con los nombres de los meses 
# (corresponden a las etiquetas de las columnas de la matriz) y un número entero n. 
# La función retorna un vector con los nombres de los n meses en los que más se ha comprado 
# (medido en dólares). Los nombres deben aparecer ordenados descendentemente por el total de compras hechas.

def top_n(matriz,meses,n):
  sumas=np.sum(matriz,axis=0)#suma por columna
  i_ordenados=np.argsort(sumas)[::-1][:n]
  return meses[i_ordenados]

# Ahora en su programa principal:
# 4.[5 puntos] Utilice la función del numeral 1 para generar los vectores y la matriz a 
# partir delos datos contenidos en el archivo dataset.csv.
farmacias,meses,matriz=llenar_matriz("2ndo Examen\\dataset.csv")

# 5.[10 puntos] Muestre por pantalla el nombre de la farmacia con más meses con compras cero.
conteo=np.zeros(farmacias.size,int)
n,m=matriz.shape
for i in range(n):#filas
  for j in range(m):#columnas
    if matriz[i,j]==0:
      conteo[i]+=1
i_mayor=np.argmax(conteo)
print(farmacias[i_mayor])

# 6.[5 puntos] Muestre por pantalla los nombres de las farmacias en las que hubo compras todos los meses de la matriz.
validacion=np.ones(farmacias.size,bool)
n,m=matriz.shape
matriz[0,3]=0
matriz[4,1]=0
for i in range(n):#filas
  for j in range(m):#columnas
    if matriz[i,j]!=0:
      validacion[i]= validacion[i] and True
    else:
      validacion[i]= validacion[i] and False
indexada=farmacias[validacion]
print(indexada)