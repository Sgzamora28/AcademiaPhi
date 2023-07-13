import datetime


taxis=[[1372637482620000005,"C","","",20000005,1372637482,"A","-8.599239:41.149188,-8.584767:41.168529,-8.584317:41.169258,-8.584326:41.169258"],
       [1372639181620000089,"C","","",20000089,1372639181,"A","-8.646534:41.175558,-8.648829:41.177367"],
       [1372639960620000309,"B","",38,20000089,1372639960,"A","-8.60418:41.160969,-8.603874:41.1615,-8.579781:41.167881,-8.579763:41.167899"]]


#TRIP_ID,CALL_TYPE,ORIGIN_CALL,ORIGIN_STAND,TAXI_ID,TIMESTAMP,DAY_TYPE,POLYLINE
def cargarDatos(datos:list):
  diccionario={}
  for dato in datos:
    taxi_id,timestap,coordenadas=dato[4],dato[-3],dato[-1]
    if taxi_id not in diccionario:
      diccionario[taxi_id]={timestap:coordenadas}
    
    else:
      diccionario[taxi_id][timestap]=coordenadas

  return diccionario



# {20000005: {1372637482: '-8.599239:41.149188,-8.584767:41.168529,-8.584317:41.169258,-8.584326:41.169258'}, 
# 20000089: {1372639181: '-8.646534:41.175558,-8.648829:41.177367', 1372639960: '-8.60418:41.160969,-8.603874:41.1615,-8.579781:41.167881,-8.579763:41.167899'}}
def obtenerRutas(datos:dict,id_taxi:int,mes:int,anio:int):
  coordenadas=[]
  for key,value in datos.items():
    if key==id_taxi:
      for fecha,coordenada in value.items():
        fechaF = str (datetime.datetime.fromtimestamp(int(fecha)))
        anio2,mes2=fechaF[:4],fechaF[5:7]
        print(anio2,mes2)
        if int(anio2)==anio and int(mes2)==mes:
          coordenadas.append(coordenada)
  
  return coordenadas


x=cargarDatos(taxis)
# print(x)

y=obtenerRutas(x,20000089,6,2013)
print(y)