claves={}
with open("featuresdf.csv",encoding="utf-8") as arch:
  arch.readline()
  for linea in arch:
    datos=linea.strip().split(",")
    artista=datos[2]
    key=datos[5]
    claves[key]=claves.get(key,[])
    claves[key].append(artista)
