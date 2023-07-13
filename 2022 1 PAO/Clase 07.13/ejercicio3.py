def peligrosidad(personas:str,delitos:dict):
  arch=open(personas)
  arch.readline()
  diccionario={}
  for linea in arch:
    linea=linea.strip().split(',') #['1303408189','28','tercer nivel','robo','vandalismo']
    suma_delitos=0
    for i in range(3,len(linea)):
      delito=linea[i]
      x=delitos[delito]
      suma_delitos+=x

    puntos_edad=0
    if 20<int(linea[1])<45:
      puntos_edad=10

    puntos_inst=0
    if linea[2]=='secundaria' or linea[2]=='tercer nivel':
      puntos_inst=10
    
    ranking=suma_delitos+puntos_edad+puntos_inst
    diccionario[linea[0]]=ranking
  arch.close()
  return diccionario






#main
palabrasclaves=["TNT","bomba","polvora","mision","muerte"]
tiposdelitos={"robo":10,"asesinato":15,"vandalismo":5,"terrorismo":30}

x=peligrosidad('Clase 07.13\\personas.txt',tiposdelitos)
print(x)