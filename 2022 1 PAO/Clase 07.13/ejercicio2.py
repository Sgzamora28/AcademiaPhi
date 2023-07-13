# Para match.com es importante emparejar personas para este día del Amor y de la Amistad. Para esto cuenta con un diccionario personas con la siguiente estructura:
# Para conocer la compatibilidad entre dos personas se utilizan sus características y se calcula el índice de Tanimoto de la siguiente manera:


#funciones
# La función hayEmparejamiento(codigoP1, codigoP2, dicPersonas, aceptacion) que recibe el código de dos personas, el diccionario de personas y el nivel de aceptación (entre 0 y 1). 
# Esta función devolverá una tupla con el valor del índice de Tanimoto y un valor de verdad True en el caso de que haya emparejamiento y False en caso contrario. 
# Hay emparejamiento cuando el valor del índice de Tanimoto es superior o igual al nivel de aceptación

def emparejamiento(codigoP1,codigoP2,diccionario,aceptacion):
  union=diccionario[codigoP1].union(diccionario[codigoP2])
  interseccion=diccionario[codigoP1]&diccionario[codigoP2]
  tanimoto=len(interseccion)/len(union)
  emparejamiento=False
  if tanimoto>=aceptacion:
    emparejamiento=True

  return tanimoto,emparejamiento

# 2. [8 puntos] La función imprimirResultados(codPersona, dicPersonas, aceptacionMinimo, aceptacionMaximo) recibe el código de una persona, el diccionario de personas y 
# los niveles de aceptación mínimo y máximo. Esta función recorre todo el diccionario verificando la compatibilidad de esta persona con las demás y genera un reporte en un archivo. 
# El nombre del archivo es el codPersona con extensión “.txt”. El formato de cada línea del archivo es el siguiente:
# Código@indiceTanimoto@textoCompatibilidad
# Donde textoCompatibilidad debe ser “compatible” si el índice de Tanimoto está entre los niveles de aceptación mínimo y máximo, caso contrario debe ser “no compatible”.
def imprimirResultados(codigo:str,diccionario:dict,minimo:float,maximo:float):
  with open('Clase 07.13\\'+codigo+'.txt','w') as f:
    sujeto=diccionario[codigo]
    for clave in diccionario:
      if clave!=codigo:
        tanimoto=emparejamiento(codigo,clave,diccionario,0)[0]

        if minimo<tanimoto<maximo:
          textoCom='compatible'

        else:
          textoCom='no compatible'
        
        f.write('{}@{:.2f}@{}\n'.format(clave,tanimoto,textoCom))


#main
personas = { 'P1021' : {'alegre', 'farrero', 'hacker', 'deportista','fabuloso'},
             'P1001' : {'farrero', 'deportista', 'programador', 'fabuloso','alegre'},
             'P10031': {'alegre','extrovertida','musico','aventurero','farrero'}
             }

x=emparejamiento('P10031','P1001',personas,0.5)
imprimirResultados('P10031',personas,0.3,0.8)




