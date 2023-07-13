import numpy as np
# import numpy

#Los 5 arreglos son paralelos
P = np.array(["ct-32", "mto-990", "ct-32"])
PF = np.array([789, 1500, 900]) 
PD = np.array([26, 35, 70])
D = np.array([300, 12, 100])
CF = np.array([1000, 2000, 1100])
# [6 puntos] Escriba una función llamada produccionAnual(codigo, P, PF) que retorne la cantidad
# total de piezas código fabricadas en el año.

#NP.WHERE
# frutas=np.array(["Manzana","Pera","Noni","Mandarina","Mango","Sandia","Kiwi","Mandarina","Coco"])
# i=np.where(frutas=="Mandarina")#----->(array([3,7]),)
# # print(i)
# indexada=frutas[i]
# print(indexada)


#INDEXAMIENTO BOOLEANO
# frutas=np.array(["Manzana","Pera","Noni","Mandarina","Mango","Sandia","Kiwi","Mandarina","Coco"])
# condicion = frutas=="Mandarina" #[False False False  True False False False  True False]
# print(condicion)
# indexada=frutas[condicion]
# print(indexada)



#INDEXAMIENTO ELEGANTE
# frutas=np.array(["Manzana","Pera","Noni","Mandarina","Mango","Sandia","Kiwi","Coco"])
# i=np.array([0,3,5])
# indexadas=frutas[i]
# print(indexadas)




def produccionAnual(codigo,piezas,fabricadas):
  i_pieza=np.where(piezas==codigo)
  x=fabricadas[i_pieza]#---> cantidad de piezas fabricadas de la pieza "codigo"
  total=np.sum(x)
  return total




# [12 puntos] El rendimiento de fabricación de un producto se mide de la siguiente forma:
# rendimiento = (total_piezas_fabricadas - total_piezas_defectuosas) / total_capacidad
#
#  Escriba la función rendimientoPromedio(codigo, P, PF, PD, CF, D) que retorna el rendimiento
# promedio diario para un codigo. El rendimiento promedio diario es igual a rendimiento /
# total_dias_fabricacion.

def rendimientoPromedio(codigo, piezas, fabricadas, defectuosas, c_maxima, dia_anio):
  total_piezas_fabricadas=produccionAnual(codigo,piezas,fabricadas)
  i_pieza=np.where(piezas==codigo)#---> Retorna todos los indices donde el arreglo es igual a la condicion
  total_piezas_defectuosas=np.sum(defectuosas[i_pieza])#----> cantidad de piezas defectuosas
  total_capacidad=np.suma(c_maxima[i_pieza])
  rendimiento = (total_piezas_fabricadas - total_piezas_defectuosas) / total_capacidad
  total_dias_fabricacion=i_pieza.size
  promedio=rendimiento/total_dias_fabricacion
  
  return promedio

# [12 puntos] Escriba la función porcentajeAnualDefecto(codigo, P, PD, PF), que retorna el
# porcentaje de defectos que tiene un codigo. El porcentaje de defectos se calcula como sigue:
# porcentaje_defectos = ( total_piezas_defectuosas / total_piezas_fabricadas ) * 100

def porcentajeAnualDefecto(codigo,piezas,defectuosas,fabricadas):
  total_piezas_fabricadas=produccionAnual(codigo,piezas,fabricadas)
  i_pieza=np.where(piezas==codigo)
  total_piezas_defectuosas=np.sum(defectuosas[i_pieza])
  porcentaje_defectos = ( total_piezas_defectuosas / total_piezas_fabricadas ) * 100

  return porcentaje_defectos



# [10 puntos] Escriba la función productosDefectuosos(codigos, P, PF, PD, porcentaje), que
# retorna un arreglo con los códigos de los productos que están en la lista codigos y que tengan un
# porcentaje de defectos mayor a porcentaje.


def productosDefectuosos(codigos,piezas,fabricadas,defectuosas,porcentaje):
  defectuosas=np.array([])

  for codigo in codigos:
    defecto=porcentajeAnualDefecto(codigo,piezas,defectuosas,fabricadas)
    if defecto>porcentaje:
      np.append(defectuosas,codigo)#Esta es la manera de agregar elementos a un array


  return defectuosas




# [10 puntos] Escriba la función minimoPorcentajeDefecto(P, PF, PD), que retorna el código del
# producto con el menor porcentaje anual de defectos.

def minimoPorcentajeDefecto(piezas,fabricadas,defectuosas):
  x=np.array([])#otro arreglo paralelo
  for i in range(piezas.size):
    pad=porcentajeAnualDefecto(piezas[i],fabricadas[i],defectuosas[i])
    np.append(x,pad)

  menor=np.argmin(x)
  pieza_menor=piezas[menor]

  return pieza_menor
