personas = { 'P1021' : {'alegre', 'fumador', 'hacker', 'deportista'},
             'P1002' : {'hacker','alegre','perezosa','matematico'},
             'P1001' : {'farrero', 'deportista', 'programador', 'fabuloso'},
             'P0911' : {'alegre','deportista','matematico','programador','fumador'} }
#Tanimoto
#cantidad de caracteristicas en comun/cantidad de caracteristicas totales entre las dos personas

# 1. [7 puntos] La función hayEmparejamiento(codigoP1, codigoP2, dicPersonas, aceptacion) que recibe el código de dos personas, el diccionario de personas y 
# el nivel de aceptación (entre 0 y 1). Esta función devolverá una tupla con el valor del índice de Tanimoto y un valor de verdad True en el caso de que haya emparejamiento y 
# False en caso contrario. Hay emparejamiento cuando el valor del índice de Tanimoto es superior o igual al nivel de aceptación

def emparejamiento(p1:str,p2:str,diccionario:dict,indice:float):
  totales=diccionario[p1].union(diccionario[p2])
  comun=diccionario[p1].intersection(diccionario[p2])

  tanimoto=len(comun)/len(totales)

  if tanimoto>=indice:
    return tanimoto,True

  else:
    return tanimoto,False


x=emparejamiento('P1002','P0911',personas,0.5)
print(x)