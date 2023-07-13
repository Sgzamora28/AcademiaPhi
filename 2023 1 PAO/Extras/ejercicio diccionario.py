import random as rd
def crear_diccionario():
  dic_datos={}
  nombres=["Kyra","Steven","Fernando","Daniel","Melissa","Maria","Gary","Elias","Roberto","Ericka"]
  for i in range(10):
      matricula=str(rd.randint(2019,2023))
      for j in range(5):
          matricula+=str(rd.randrange(10))
      nombre=nombres[i]
      x=rd.randint(3,5)
      dic_datos[matricula]={"notas":{},"nombre":nombre}
      for k in range(x):
          dic_datos[matricula]["notas"]["calif"+str(k+1)]=round(rd.uniform(40,100),2)
  return dic_datos

def obtener_datos(diccionario):
  '''Funcion que retorna dos listas paralelas, la primera es el nombre de los estudiantes del diccionario que recibe
  y la segunda es la lista de los promedios de aquellos estudiantes'''
  nombres=[]
  promedios=[]
  for dicc in diccionario.values():
    nombres.append(dicc["nombre"])
    notas=dicc["notas"]
    promedio=sum(notas.values())/len(notas)
    promedios.append(round(promedio,2))
  return nombres,promedios

def nota_top(nombres:list[str],promedios:list[float]):
  '''Funcion que retorna el nombre de la persona que tiene el mas alto promedio y ese promedio'''
  nota_alta=max(promedios)
  indice=promedios.index(nota_alta)
  nombre=nombres[indice]
  return nombre,nota_alta

#main
dic_datos=crear_diccionario()
n,p=obtener_datos(dic_datos)
print(n)
print(p)
print(nota_top(n,p))