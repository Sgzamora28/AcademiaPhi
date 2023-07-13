import datetime

def calcularFecha(fecha, n):
    f = datetime.datetime.strptime(fecha, '%d-%m-%Y').date()
    resta = f - datetime.timedelta(days=n)
    return resta.strftime('%d-%m-%Y')


def cargar(archivo):
  ids=set()
  rutas={}
  with open(archivo) as arch:
    arch.readline()
    for line in arch:
      ruta,chofer,fecha=line.strip().split(",")#----> [id_ruta,id_chofer,fecha]
      ids.add(chofer)

      if rutas.get(ruta,0)==0:
        rutas[ruta]={}

      if rutas[ruta].get(fecha,0)==0:
        # rutas[ruta][fecha]=set([chofer])
        rutas[ruta][fecha]={chofer}
      
      else:
        rutas[ruta][fecha].add(chofer)
      

  return ids,rutas

def buscar(dicc,fecha,choferes,ruta,n):
  conducido=set()#guardar quienes si han conducido
  recorrido=dicc[ruta]
  for i in range(1,n+1):#1,2,3,4
    f_anterior=calcularFecha(fecha,i)
    conducido=conducido|recorrido.get(f_anterior,set())

  no_conducido=choferes-conducido
  return no_conducido
  

def grabar(fecha,dicc,choferes,n):
  for recorrido,datos in dicc.items():
    with open(f"{recorrido}_{fecha}.txt","w") as arch:
      arch.write("Para la ruta {}, los choferes disponibles para la fecha {} que no hayan manejado {} dias anteriores son:\n".format(recorrido,fecha,n))
      no_manejado=buscar(dicc,fecha,choferes,recorrido,n)
      for chofer in no_manejado:
        arch.write(f"{chofer}\n")




choferes,rutas=cargar("rutasManejadas2018.txt")
# print(choferes)
# print(rutas)
sin_conducir=buscar(rutas,"21-05-2018",choferes,"Guayaquil-Cuenca",2)
# print(sin_conducir)
grabar("19-05-2018",rutas,choferes,2)



