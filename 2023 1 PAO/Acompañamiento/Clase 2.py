nombre="Steven"
apellido="Zamora"

# print(nombre,apellido)

precio=20.5
libro="Calculo de Una Variable"
# print("El precio del libro",libro,"es de $",precio)


###############################
#FORMATEO DE SALIDA
###############################

#Old style

# %s ---> Celda contendra un str
# %d ---> Celda contendra un int
# %f ---> Celda contendra un float

#round----> funcion que me permite redondear 
#round(numero,cantidad de decimales)

# print("El precio del libro %s es de $%.1f"%(libro,precio))

#%[cantidad de espacio].[cantidad de decimales][tipo de dato]




#New Style

# print(f"El precio del libro {libro} es de ${precio}")

#Formato .format

# print("El precio del libro {} es de ${:-^30.2f}".format(libro,precio))
#                                                        0     1

#{[orden de los datos]:[relleno][alineacion][espacio].[cantidad de decimales][tipo dato]}
# ALINEACION: < (derecha)
#             > (izquierda)
#             ^ (centro)





###############################
#Cadenas de Texto#
###############################
#Son inmutables ---> NO SE PUEDEN MODIFICAR
#Son indexables (permiten indexacion y slicing)

saludo="Hola mundo" 
#INDEXACION
x=saludo[5]
# print("El quinto caracter es la letra \"{}\"".format(x))

#SLICING
y=saludo[::-1]
# print(y)

#OPERACIONES

#Pertenencia/No pertenencia (Busqueda)

fullname="Steven Gonzalo Zamora Cevallos"
nombre1="Juan"

#Pertenecia 
busqueda=nombre1 in fullname
print(busqueda)

#No pertencia
busqueda2=nombre1 not in fullname
print(busqueda2)


#Concatenacion


#Repeticion


#longitud de cadena ----> len()
#minimo caracter de una cadena -----> min() [el caracter de menor codigo ASCII]
#maximo caracter de una cadena -----> max() [el caracter de mayor codigo ASCII]