import numpy as np

t_ciudades = ('Barcelona', 'Barranquilla', 'Bogota', 'Bucaramanga',
              'Buenos Aires', 'Guayaquil', 'Lima', 'Machala', 'Portoviejo',
              'Puerto Montt', 'Quito', 'Riohacha', 'San Jose', 'Washington DC')

d_ciudades = {
              "Capital": ['Barcelona', 'Bogota', 'Buenos Aires', 'Lima', 'Quito','Washington DC', "Machala"],
              "Costa": ['Barranquilla','Guayaquil','Machala','Portoviejo','Puerto Montt','Riohacha',"Barcelona","Lima",],
              "Sierra": ['Bogota', 'Bucaramanga', 'Cuenca', 'Ibarra', 'Quito', 'San Jose',"Washington DC", "Buenos Aires"]
             }

t_fechas = ("12-ENE-2017", "29-MAY-2003", "25-JUN-1995", "12-OCT-1970","09-NOV-2020", "29-ABR-2016", "21-DEC-2012", "15-AGO-1999")

###########################################################################
#COMSTRUCCION DE LA MATRIZ PARA FINES REPRESENTATIVOS
matriz = np.random.randint(-90, 57, (len(t_fechas), len(t_ciudades)), int)
print(matriz)
print()
###########################################################################

#La ciudad con la mayor diferencia entre su maxima y minima temperatura registrada
maximos=np.max(matriz,axis=0).ravel()
minimos=np.min(matriz,axis=0).ravel()
diferencia=maximos-minimos
i_mayor=np.argmax(diferencia)
mayor=t_ciudades[i_mayor]
# print(maximos)
# print(minimos)
# print(diferencia)
print(mayor)
print()


#Funcion top n
#La funcion recibe una matriz de temperaturas, el diccionario de ciudades, las etiquetas de columnas, un entero n y 
# dos strings que representan los tipos de ciudades. Considerando solo los datos de las ciudades que cumplen ambos tipos, 
# la funcion retorna una tupla con los siguientes dos elementos:
#-Un vector con las n ciudades que han registrado las mayores temperaturas historicas y
#-Un vector paralelo con sus correspondientes temperaturas
def top_n(matriz,d_ciudades,columnas,n,tipo1,tipo2):
    indices=[]
    for i in range(len(columnas)):
        ciudad=columnas[i]
        if ciudad in d_ciudades[tipo1] and ciudad in d_ciudades[tipo2]:
            # print(ciudad)
            indices.append(i)
    
    # print(indices)
    matriz_index=matriz[:,indices]
    # print(matriz_index)
    # print(matriz_index)
    maximo_columna=np.max(matriz_index,axis=0)
    i_maximas=np.argsort(maximo_columna)[::-1][:n]#--->[3 0 1 2]
    ciudades_max=np.array(list(columnas))[i_maximas]
    max_ordenada=np.sort(maximo_columna)[::-1][:n]

    return ciudades_max,max_ordenada



x=top_n(matriz, d_ciudades, t_ciudades, 2, "Capital", "Sierra")
print(x)