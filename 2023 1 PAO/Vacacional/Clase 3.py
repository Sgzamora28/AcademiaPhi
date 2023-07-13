#########################################
#FORMATEO DE SALIDA#
#########################################


# nombre=input("Ingrese un nombre: ")
# promedio=float(input("Promedio general: "))
# edad=int(input("Ingese tu edad: ")) #---> str ["20"]
# print('El nombre del usuario es',nombre)


# anio_nacimiento=2023-edad #2023-"20"s
# print("El anio de nacimiento del usaurio es",anio_nacimiento)

#Formateo de Salida

# nombre_pagina=input("Ingresa un nombre para tu pagina: ")

# print("www.",nombre_pagina,".com")


##### #Old style #####
#%s ---> string
#%d ---> int
#%f ---> float

# print("www.%s.com"%(nombre_pagina))
#Yo, ___________________________ autorizo

# print("Yo %25s autorizo a la entidad blablabla utilizar mis datos..... Promedio general %.2f"%(nombre,promedio))



#Funcion format
# {[orden de las variables]:[relleno][alineacion (< > ^)][espacio de la celda].[decimales][tipo de dato]}
# print("Yo {:-^25s} autorizo a la entidad blablabla utilizar mis datos..... Promedio general {:.2f} blablabla".format(nombre,promedio))


#########################################
#CADENAS-STRINGS-STR-DATOS DE TIPO TEXTO#
#########################################

#Son celosos con las mayusculas y minusculas
#Los str son inmutables
#Permiten indexacion y slicing


saludo1='Hola que hace'
saludo2="Hola que hace"


#"H O L A"  
# 0 1 2 3

#Indexacion
#LOS INDICES SIEMPRE EMPIEZAN EN 0 DESDE IZQUIERDA A DEECHA

#De un string tomar un solo caracter en base a su indice
# print(saludo1[-1])

#Slicing
#ES TOMAR UNA PORCION DE LA CADENA ORIGINAL
#str[start:stop:step]
#str[inicio:final:salto]

p1=saludo1[:4]
p2=saludo1[9:]
p3=saludo1[::-1]
# print(p1,p2)
# print(p3)

texto="python"
print(texto[:2]+texto[::-1]+texto[2:])