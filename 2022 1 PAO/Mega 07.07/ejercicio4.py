def costosrecoleccion(proveedoras,recoleccion):
  promedio=sum(recoleccion)/len(recoleccion)
  
  miniRec=min(recoleccion)
  indMini=recoleccion.index(miniRec)
  menor=proveedoras[indMini]

  maxRec=max(recoleccion)
  indMax=recoleccion.index(maxRec)
  mayor=proveedoras[indMax]

  return promedio,mayor,menor


def minManobra(proveedoras: list,costosManoObra: list,costoLimite: float):
  prov=[]
  for i in range(len(costosManoObra)):
    if costosManoObra[i]<costoLimite:
      prov.append(proveedoras[i])
  
  return prov


def insumosMayorMenor(proveedoras: list,insumos: list):
  mayorAmenor=[]
  ordenada=insumos.copy()
  ordenada.sort(reverse=True)
  for insumo in ordenada:
    i=insumos.index(insumo)
    mayorAmenor.append(proveedoras[i])
  
  return mayorAmenor



#main
nombreProveedoras = ["FEITA S.A.", "Chikitita S.A.", "Brafe", "SIC", "Dollman"]
costosRecoleccion = [6.58, 2.07, 8.11, 3.05, 3.51]
costosManoObra = [1.39, 3.98, 6.88, 8.49, 5.03]
costosTransporte = [0.87, 8.35, 5.52, 9.25, 4.27]
costosInsumos = [9.94, 7.22, 9.92, 9.44, 9.02]


x=costosrecoleccion(nombreProveedoras,costosRecoleccion)
print(x)

y=minManobra(nombreProveedoras,costosManoObra,8)
print(y)

z=insumosMayorMenor(nombreProveedoras,costosInsumos)
print(z)
