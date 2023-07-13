def mezcla(archivo):
  canciones=[]
  indice_bailable=[]
  with open(archivo,encoding='utf-8') as arch:
    arch.readline()
    for linea in arch:
      datos=linea.strip().split(",")
      canciones.append([datos[1],datos[2],float(datos[-2])])
      indice_bailable.append(float(datos[3]))

  playlist=[]
  copia=indice_bailable.copy()
  copia.sort(reverse=True)
  validacion=0
  for i in range(len(copia)):
    original=indice_bailable.index(copia[i])
    x=canciones[original][-1]
    if validacion+x<3600000:
      if not(4000<canciones[original][-1]<5000):
        playlist.append(f"{canciones[original][0]};{canciones[original][1]}\n")
        validacion+=canciones[original][-1]
      else:
        print(f"{canciones[original][0]} no es una cancion elegible")
      
      indice_bailable[original]=0
  escritura=open("mezcla.csv","w",encoding="utf-8")
  escritura.write("Cancion,Artista\n")
  escritura.writelines(playlist)


mezcla("featuresdf.csv")
