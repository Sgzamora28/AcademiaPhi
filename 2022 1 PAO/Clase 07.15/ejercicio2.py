#funciones
def emparejamiento(cod1:str,cod2:str,d_personas:dict,aceptacion:float):
  interseccion=d_personas[cod1]&d_personas[cod2]
  union=d_personas[cod2].union(d_personas[cod1])
  tanimto=len(interseccion)/len(union)
  
  empareja=False
  if tanimto>aceptacion:
    empareja=True

  # if tanimto>aceptacion:
  #   empareja=True
  # else:
  #   empareja=False

  return tanimto,empareja

def imprimir(cod:str,d_persona:dict,minimo:float,maximo:float):
  for key in d_persona:
    if cod!=key:
      tanimoto=emparejamiento(cod,key,d_persona,0)[0]
      
      compatibilidad='No compatible'
      if minimo<tanimoto<maximo:
        compatibilidad='Es compatible'
      # print("%s@%.2f@%s"%(key,tanimoto,compatibilidad))
      print("{}@{:.2f}@{}".format(key,tanimoto,compatibilidad))
      # print(key,'@',tanimoto,'@',compatibilidad)


#main
personas = { 'P1021' : {'alegre', 'farrero', 'hacker', 'deportista','fabuloso'},
             'P1001' : {'farrero', 'deportista', 'programador', 'fabuloso','alegre'},
             'P10031': {'alegre','extrovertida','musico','aventurero','farrero'}
             }



imprimir('P1021',personas,0.3,0.99)