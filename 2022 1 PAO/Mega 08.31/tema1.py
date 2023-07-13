# TEMA 1 (30 PUNTOS)
# Suponga que existe un diccionario tendencias con un string que representa una fecha (mm-dd-aaaa) como clave y 
# como valor un conjunto de las etiquetas (hashtags) que fueron tendencias en Twitter para esa fecha. Por ejemplo:
tendencias = {"08-22-2016":{"#Rio2016","#GYE", "#BSC", "#ECU"}, "08-25-2016":{"#GYE", "#BRA"}, "08-27-2016":{"#YoSoyEspol", "#GYE", "#BSC"}}
# x=tendencias.get("08-25-2016",-1)
# print(x)

# Implemente las siguientes funciones:
# a. cuentaEtiquetas (tendencias, listaFechas) que recibe el diccionario de tendencias y una lista con strings que representan fechas (mm-dd-aaaa). 
# La función debe retornar un nuevo diccionario con la etiqueta como clave y como valor, el número de días que esta etiqueta fue tendencia durante 
# las fechas especificadas en listaFechas. 
# Por ejemplo:
# cuentaEtiquetas(tendencias, ["08-22-2016", "08-25-2016", "08-27-2016"]) retorna
# {‘#Rio2106’:1, ‘#GYE’:3, ‘#YoSoyEspol’:1, ‘#BSC’:2, ‘#ECU’:1, ‘#BRA’:1}

def contador(tendencias,fechas):
  diccionario={}
  for twits in tendencias.values():
    for twit in twits:
      x=diccionario.get(twit,-1)

      if x==-1:
        diccionario[twit]=0

      diccionario[twit]+=1

  return diccionario


contador(tendencias,["08-22-2016", "08-25-2016", "08-27-2016"])

# b. reportaTendencias(tendencias, listaFechas) que recibe el diccionario de tendencias y una lista con strings que representan fechas (mm-dd-aaaa). 
# La función debe mostrar por pantalla:
listaFechas=["08-22-2016", "08-25-2016", "08-27-2016"]
# 1) Las etiquetas que fueron tendencia todas las fechas en listaFechas
# 2) Las etiquetas que fueron tendencia al menos en una de las fechas en listaFechas

def reportar(tendencias,fechas):
  todas=[]
  no_todas=[]

  for fecha in fechas:
    x=tendencias.get(fecha,-1)
    if x!=-1:
      no_todas=no_todas+list(x)

  for tendencia in no_todas:
    y=no_todas.count(tendencia)
    if y==len(fechas) and tendencia not in todas:
      todas.append(tendencia)


  print("Todas las  fechas:",todas)
  print("Al menos una fecha:",set(no_todas))


reportar(tendencias,listaFechas)
  


# c. tendenciasExcluyentes(tendencias, fecha1, fecha2) que recibe el diccionario de tendencias y dos strings que representan fechas (mm-dd-aaaa).
# La función debe mostrar por pantalla las etiquetas que fueron tendencias o en fecha1 o en fecha2, pero no en las dos. 
# Nota: suponga que fecha1 y fecha2 existen en el diccionario como claves.

def excluyentes(tendencias:dict,fecha1:str,fecha2:str):
  conjunto1=tendencias[fecha1]
  conjunto2=tendencias[fecha2]
  excluyente=conjunto1^conjunto2
  print(excluyente)

print()
excluyentes(tendencias,"08-22-2016","08-27-2016")