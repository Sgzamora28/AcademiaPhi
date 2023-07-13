import random as rd
#Tenemos una lista de promedios y una lista de Alumnos
lst_nombres=["Steven","Kyra","Gabriel","Fernando","Melissa","Eduardo","Nathaly","Stephany"]
lst_promedios=[]

for i in range(len(lst_nombres)):
  x=rd.randint(6,10)
  lst_promedios.append(x)

print(lst_promedios)



#Crear una funcion que retorne el top n de alumnos, sus parametros son la lista de alumnos, la lista de promedios y
#un valor n para el top. La funcion imprime la cantidad n de estudiantes con el mayor promedio

def topn(alumnos:list[str],promedios:list[int],n:int):
  #[9, 8, 8, 8, 6, 9, 6, 8]
  prom=promedios.copy() #pero esta lista no la voy a ordenar
  top_nombres=[]#guardar los nombres en base al top
  copia_promedios=promedios.copy()
  copia_promedios.sort(reverse=True) #ordena de menor a mayor. Si yo le agg el reverse=True ordena de mayor a menor
  #[9,9,8,8,8,8,6,6]


  for promedio in copia_promedios:
    indice=prom.index(promedio)
    estudiante=alumnos[indice]
    top_nombres.append(estudiante)
    prom[indice]=0

  top=top_nombres[:n]
  
  for e in top:
    print(e)


#main 

topn(lst_nombres,lst_promedios,4)
