saludo="Hola Mundo"
id='Soy steven'

# print(len(saludo))


#  "Hola Mundo"
#   0123456789


#Indexamientos y Slicing
cuartoCaracter=saludo[3]
x=saludo[:4]
# print(x)

################
#Ejercicio 1
################
# secuencia="ATCCGTAGCGTAATCCATGCATTATC"
# busqueda="TTGACTATAGCCAAGCGTAGCGAAAAAATTC"
# inicio=input("Extraer desde la posicion: ")
# fin=input("Extraer hasta la posicion: ")

# extraida=secuencia[int(inicio):int(fin)+1]
# print(extraida)

# buscar=extraida in busqueda
# print("Se encontro la secuencia:",buscar)


######################
#Ejercicio 2
######################

info='El DIA 2021-05-17 en la CIUDAD Guayaquil se registró una TEMP_MIN 18.3 grados centígrados y una TEMP_MAX 27.7 grados centígrados.'
l_info=info.split(' ')
print(l_info)
#['El', 'DIA', '2021-05-17', 'en', 'la', 'CIUDAD', 'Guayaquil', 'se', 'registró', 'una', 
# 'TEMP_MIN', '18.3', 'grados', 'centígrados', 'y', 'una', 'TEMP_MAX', '27.7', 'grados', 'centígrados.']
fecha=""
ciudad=""
minima=""
maxima=""

for i in range(len(l_info)):
  palabra_actual=l_info[i]
  if palabra_actual.isupper():#etiqueta
    if palabra_actual=="DIA":
      fecha=l_info[i+1]
  
    elif palabra_actual=="CIUDAD":
      ciudad=l_info[i+1]

    elif palabra_actual=="TEMP_MIN":
      minima=l_info[i+1]

    else:
      maxima=l_info[i+1]


print(fecha,ciudad,minima,maxima)
