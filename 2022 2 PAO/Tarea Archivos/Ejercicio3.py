def obtenerResumen(nombre):
  diccionario = {}
  with open(nombre,encoding='utf-8') as arch:
    for line in arch:
      linea = line.lower().strip().replace(".", "").split(" ")
      for palabra in linea:
        diccionario[palabra] = diccionario.get(palabra, 0) + 1

  print(diccionario)
  palabras = list(diccionario.items())
  contador = open("contador.txt", "w",encoding='utf-8')
  for pal, valor in palabras:
    contador.write("{} {}\n".format(pal, valor))


obtenerResumen("navidad.txt")
