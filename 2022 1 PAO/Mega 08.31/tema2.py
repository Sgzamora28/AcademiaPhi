# Las distancias en km, expresadas en valores enteros positivos, entre ciudades del Ecuador conectadas directamente 
# por una carretera están dadas en el archivo Ecuador_Distancias.txt con el siguiente formato:
# Ciudad de Partida|Ciudad,Distancia|Ciudad,Distancia|...|Ciudad,Distancia
#[ciudad de partida,ciudad,ciduad,ciudad...]

# Implemente las siguientes funciones:

# a. cargarDatos(nombreArchivo) que recibe el nombre del archivo como string y retorna el diccionario distancias con el siguiente formato:
# {"Ambato":{"Azogues":280, "Babahoyo":212, ... ,"Pedernales":318}, ... "Babahoyo":{‘Ambato’:250,...}}

def cargador(archivo):
  dic={}
  with open(archivo) as arch:
    arch.readline()
    for line in arch:
      lista=line.strip().split("|")
      x=dic.get(lista[0],-1)

      if x==-1:
        dic[lista[0]]={}

      for valores in lista[1:]:
        ciudad,distancia=valores.split(",")
        dic[lista[0]][ciudad]=int(distancia)

  return dic


diccionario=cargador("Mega 08.31\\Ecuador_Distancias.txt")
# print(diccionario)

#b.  ciudadesCercanas(distancias, km) donde km es un valor entero positivo y distancias es el diccionario generado en el literal a. 
# La función retorna una lista de tuplas con todos los pares de ciudades conectadas directamente por una carretera que estén a una 
# separación menor o igual que km. La tupla incluye ciudad1, ciudad2, y distancia que las separa. 
# Por ejemplo:
# ciudadesCercanas(distancias, 300) retorna [(‘Ambato’,’Azogues’,280), (‘Ambato’,’Babahoyo’,212), (‘Azogues’,’Babahoyo’,125), (‘Babahoyo’,’Ambato’,250)]



# {'Pedernales': {'Ambato': 318, 'Azogues': 555, 'Portoviejo': 180}, 'Ambato': {'Azogues': 280, 'Babahoyo': 212, 'Pedernales': 318}, 
# 'Azogues': {' Pedernales': 555, 'Babahoyo': 125}, 'Babahoyo': {'Ambato': 250}, 'Guayaquil': {'Machala': 182, 'Portoviejo': 195, 'Cuenca': 196}}

def cercanas(distancias,km):
  lista=[]
  for partida,destinos in diccionario.items():
    for ciudad in destinos:
      x=distancias[partida][ciudad]
      if x<=km:
        lista.append((partida,ciudad,x))

  return lista


# x=cercanas(diccionario,200)
# print(x)

# c. guardarCiudadesCercanas(distancias, listaKms) que recibe el diccionario de distancias generado en el literal a y una lista de valores enteros positivos. 
# La función deberá generar por cada valor de la lista un archivo con las ciudades separadas a máximo dicho valor. Por ejemplo:
# guardarCiudadesCercanas(distancias, [300, 100, 250]) genera los siguientes tres archivos: ciudades300.txt, ciudades100.txt, ciudades250.txt.

# El archivo ciudades300.txt tendría el siguiente contenido:

# Ambato,Azogues,280
# Ambato,Babahoyo,212
# Azogues,Babahoyo,125
# Babahoyo,Ambato,250

def guardar(distancias,kms):
  for km in kms:
    ciudades=cercanas(distancias,km)
    with open("Mega 08.31\\ciudades"+str(km)+".txt","w") as arch:
      for datos in ciudades:
        arch.write("{} {} {}\n".format(datos[0],datos[1],datos[2]))

guardar(diccionario,[300, 100, 250])

# Escriba un programa que lea el archivo Ecuador_Distancias.txt y genere un diccionario de distancias, de acuerdo al formato del literal a. 
# Luego, usando este diccionario, su programa deberá crear los archivos de las ciudades separadas hasta 150, 225, 320 y 555 km.