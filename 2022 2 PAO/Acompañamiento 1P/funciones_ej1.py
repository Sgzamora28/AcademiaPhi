def buscar(superior:int,inferior:int,nombres:list[str],edades:list[int]):
  '''La función retorna una lista con todos los nombres de los animales que estén dentro del rango de las edades.'''
  resultado=[]
  for i in range(len(edades)):
    if inferior<=edades[i]<superior:    #[2,4)
      resultado.append(nombres[i])

  return resultado
