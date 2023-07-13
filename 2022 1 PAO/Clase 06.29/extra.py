# 1.- Suponga que existe dos listas paralelas, la primera es una lista de fechas y la segunda es una lista de
# etiquetas que contienen conjuntos con los hashtag que han sido tendencia. Por ejemplo:
l_fechas = ['08-22-2016', '08-08-2016', '08-27-2016', '08-29-2016', '09-08-2016']
l_etiquetas = [{'#YoSoyEspol', '#Rio2016', '#BSC', '#ECU', '#GYE'}, {'#GYE', '#BRA', '#YoSoyEspol'}, {'#GYE', '#BSC'},
              {'#YoSoyEspol', '#UIO', '#EMELEC', '#GYE'}, {'#UIO', '#EMELEC','#EMELEC'}]

# Implemente las siguientes funciones:
# EncontrarTendenciasMes(Mes),esta función recibe como parámetro un mes de tipo numérico y debe retornar un conjunto con 
# todas las tendencias de dicho mes ejemplo.
# EncontrarTendenciasMes(9),retornaría {'#UIO', '#EMELEC'}
# EncontrarTendenciasMes(8)     retornaría {'#YoSoyEspol', '#Rio2016', '#BSC', '#ECU', '#GYE', '#BRA', '#UIO', '#EMELEC' }

def tendenciasXmes(mes):
  tendecias=set()
  for i in range(len(l_fechas)):
    mes1,dia,anio=l_fechas[i].split('-')
    if int(mes1)==mes: 
      tendecias

  return set(tendecias)

#sin usar colecciones
# l_etiquetas2 = [['#YoSoyEspol', '#Rio2016', '#BSC', '#ECU', '#GYE'], ['#GYE', '#BRA', '#YoSoyEspol'], ['#GYE', '#BSC'],
#               ['#YoSoyEspol', '#UIO', '#EMELEC', '#GYE'], ['#UIO', '#EMELEC','#EMELEC']]

# def tendXmes(mes):
#   tendencias=[]
#   for i in range(len(l_fechas)):
#     mes1,dia,anio=l_fechas[i].split('-')
#     if int(mes1)==mes:
#       for tendencia in l_etiquetas2[i]:
#         if tendencia not in tendencias:
#           tendencias.append(tendencia)
  
#   return tendencias



tendencias=tendenciasXmes(8)
print(tendencias)