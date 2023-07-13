def obtenerEstadisticas(nombre):
  i=0
  suma=0
  with open(nombre) as arch:
    arch.readline()
    for linea in arch:
      suma+=float(linea.strip().split("|")[2])
      i+=1
  prom=suma/i
  return i,prom