# Tema 1.
# Una empresa de telecomunicaciones determina el costo para enviar un mensaje 
# como el acumulado de los valores de cada palabra diferenciadas por tamaño y tipo:

# una palabra corta tiene máximo M caracteres,
# una palabra larga tiene mas de M caracteres,
# una palabra especial es un verbo en infinitivo, es decir, palabras terminadas en ‘ar‘, ‘er, ‘ir‘ , sin importar su tamaño.
# Implemente las siguientes funciones:

# a) cargarDatos(nombreArchivo) que recibe el nombre del archivo que en lineas separadas especifica: el tamaño M, el costo de las palabras cortas,  
# largas e infinitivos. La función abrirá el archivo y retorna un diccionario de la forma:

# nombreArchivo='costos.txt'
# 10
# 0.02
# 0.05
# 0.03

# >>> cargarDatos('costos.txt')
# retorna:
# {'M':10, 'corta':0.2, 'larga':0.5, 'infinitivo':0.3}

def cargador(archivo):
  dic={"M":0,"corta":0,"larga":0,"infinitivo":0}
  with open("Mega 08.31\\"+archivo) as arch:
    i=0
    for line in arch:
      line=float(line.strip())
      if i==0:
        dic["M"]=line
      
      elif i==1:
        dic["corta"]=line

      elif i==2:
        dic["larga"]=line

      else:
        dic["infinitivo"]=line

      i+=1
  return dic

datos=cargador("costos.txt")


# b) calcularCostos(datos, nombreArchivo) es una función que determina el costo total de un mensaje guardado en un archivo.
# La variable datos corresponde al diccionario de datos generado en el literal a) y un nombre de archivo con el texto de varias lineas correspondiente al mensaje guardado. 
# Las palabras de cada línea se encuentran separadas por espacios y un punto "." al final del mensaje como único signo de puntuación presente. 
# El punto ‘.’ no deberá ser considerado para determinar el costo de esa última palabra.

def costos(datos,archivo):
  costo=0
  with open(archivo) as arch:
    for line in arch:
      lista=line.strip().replace(".","").split(" ")
      for palabra in lista:
        if len(palabra)>datos["M"]:
          tarifa=datos["larga"]
        else:
          tarifa=datos["corta"]

        if palabra.endswith("ar") or palabra.endswith("er") or palabra.endswith("ir"):
          costo+=len(palabra)*datos["infinitivo"]
        
        else:
          costo+=len(palabra)*tarifa
  
  return costo


x=costos(datos,"Mega 08.31\\mensaje.txt")
# print(x)



# c) cambiarMensaje(datos, nombreArchivo1, nombreArchivo2) es una función que baja el costo del mensaje al modificarlo mediante:

# el recorte de las palabras largas a M-1 caracteres y  colocando ‘#‘ al final.
# el reemplazo el punto final "." con la palabra especial "END".
# La función recibe el diccionario de datos generado en el literal a) y dos nombres de archivos: nombreArchivo1 que contiene el 
# mensaje y nombreArchivo2 que es el el archivo que se crea (guarda) con el mensaje modificado.


def cambiar(datos,archivo1,archivo2):
  oraciones=[]
  with open(archivo1) as arch:
    for line in arch:
      oracion=""
      for palabra in line.strip().split(" "):
        x=int(datos["M"])
        if len(palabra)>x:
          #x=Steven
          #6
          #x[:len(x)-1]
          palabra=palabra[:x-1]+"#"
        oracion+=palabra+" "
      oracion+"END"
      oraciones.append(oracion)

  with open(archivo2,"w") as arch:
    arch.writelines(oraciones)



cambiar(datos,"Mega 08.31\\mensaje.txt","Mega 08.31\\mensaje2.txt")

  
