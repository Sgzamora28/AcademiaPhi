#################################################################################
#################################################################################
import datetime

def calcularFecha(fecha, n):
    f = datetime.datetime.strptime(fecha, '%d-%m-%Y').date()
    resta = f - datetime.timedelta(days=n)
    return resta.strftime('%d-%m-%Y')

#################################################################################
#################################################################################


#DICIONARIO
#{}---> diccionario vacio
# x={clave:valor}
# x[clave]---> valor
# x[clave_nueva]=valor_nuevo
# list(x.keys())---> [clave1,clave2,clave3]
# list(x.values())----> [valor,valor2,valor3]
# list(x.items())----> [(clave1,valor1),(clave2,valor2)]


#SETS/CONJUNTOS
#set()---> conjunto vacio
#y={1,3,5,,6,8}
#y.add(7)
#y.add([1,2,4,5])


#DESEMPAQUETAMIENTO
#Funciona para todas las colecciones que se manejan con indices---> listas,tuplas,arreglos
#z=["Steven","Zamora",20]
#nombre=z[0]
#edad=z[2]
#nombre,apellido,edad=z

#(12 puntos) ​La función cargarDatos(nomA) que recibe el nombre del archivo con los datos anteriores. Esta
# función retorna una tupla de dos elementos. El primer elemento es un -----conjunto----- con los ids de TODOS los
# choferes mencionados en el archivo. El segundo elemento es un diccionario con la siguiente estructura: {fecha​:
# {id_ruta​:{ch1,ch2,..., chk}}}. Ejemplo del diccionario:

# {"17-05-2018":{"Guayaquil-Cuenca":{"SMSNADOPN","AGBCCAPMP",...},
#  "Guayaquil-Daule" :{"...","...",...},
#  ...},
#  "18-05-2018": {"Guayaquil-Cuenca":{"EVNTAASFL","AAQSPTTGL",...},
#  "Guayaquil-Daule":{"...","...",...},
#  ...},
#  ...
# }
# 
# #list(fechas.values())---> [{"Ruta 1"=set(),"Ruta 2"=set()},{"Ruta 3"=set(),"Ruta 1"={}}] 


#Manera tradicionl de abrir archivo
# arch=open("Mejoramiento 09.12\\rutasManejadas2018.txt")
# # arch.readline()----> si el archivo tiene una cabecera
# for line in arch:
#   print(line.strip())


# arch.close()
##########################################################
#Metodo pro
# with open("Mejoramiento 09.12\\rutasManejadas2018.txt") as arch:
#   arch.readline()
#   for line in arch:
#     print(line.strip())


#iteral 1
def cargarDatos(archivo):
  ids_choferes=set()
  fechas={}
  with open("Mejoramiento 09.12\\"+archivo) as arch:
    arch.readline()
    for line in arch:
      id_ruta,id_chofer,fecha=line.strip().split(",")
      # print(fecha)
      ids_choferes.add(id_chofer)

      if fecha not in fechas:
        fechas[fecha]={id_ruta:set()}
      

      if id_ruta not in fechas[fecha]:
        fechas[fecha][id_ruta]=set()

      fechas[fecha][id_ruta].add(id_chofer)

    # print(fechas)

  return ids_choferes,fechas

choferes,fechas=cargarDatos("rutasManejadas2018.txt")


#Literal 2
# (16 puntos) ​La función encontrarChoferes(dicc, fecha, losChoferes, id_ruta, n) que recibe el diccionario del
# numeral anterior, una fecha (con formato dd-mm-yyyy), ​el ----conjunto---- con los ids de TODOS los choferes, el
# nombre de una ruta y un entero n. Esta función retorna un conjunto con los ids de todos los choferes que NO
# hayan manejado la ruta id_ruta en los n días anteriores a fecha (sin incluir fecha). Por ejemplo, si n es 3 y la
# fecha es "02-05-2018", la función devuelve un conjunto con los ids de choferes que NO hayan manejado id_ruta
# el 29, 30 de abril y el 1 de mayo de 2018.

def encontrarChoferes(dicc,fecha,choferes,ruta,n):
  ids=set()#---> conjunto de los choferes que si condujeron
  for i in range(1,n):#---(1,.....,n)
    fecha_anterior=calcularFecha(fecha,i)
    # print(fecha_anterior)
    x=dicc[fecha_anterior][ruta]#---> El conjunto de choferes que ha conducido en esa ruta para la fecha anterior
    ids=ids.union(x)#---> Aqui voy agregando a los choferes que si han conducido en esa fecha

  return choferes-ids





sinConducir=encontrarChoferes(fechas,"19-05-2018",choferes,"Guayaquil-Daule",3)
print(sinConducir)



#Literal 3
# (12 puntos) ​La función grabarArchivo(fecha, diccionario, losChoferes, n) que recibe una fecha, el diccionario
# del numeral 1, un conjunto con los IDs de todos los choferes y un número entero n​. Esta función crea un
# archivo, cuyo nombre tiene el formato idRuta_fecha.txt, para cada id_ruta de fecha con los choferes que NO
# han manejado la ruta id_ruta en los n días anteriores a la fecha (sin incluir fecha). El formato para estos
# archivos es el siguiente:
# Para la ruta Guayaquil-Cuenca, los choferes disponibles para la fecha 19-05-2018 que no
# hayan manejado 2 dias anteriores son:
# VSSUIMCMS
# SJMPYSANL



def grabarArchivo(fecha,dicc,choferes,n):
  for f in dicc:
    for ruta in dicc[f]:
      with open("Mejoramiento 09.12\\{}_{}.txt".format(ruta,fecha),"w") as arch:
        noIds=encontrarChoferes(dicc,fecha,choferes,ruta,n)
        arch.write("Para la ruta {}, los choferes disponibles para la fecha {} que no hayan manejado en los {} dia(s) anterior(es) son:\n".format(ruta,fecha,n))
        for id in noIds:
          arch.write("{}\n".format(id))

print(fechas)
grabarArchivo("19-05-2018",fechas,choferes,3)
