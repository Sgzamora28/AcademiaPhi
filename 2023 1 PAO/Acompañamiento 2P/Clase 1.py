#Tuplas
#Basicamente son listas congeladas
#No poseen mutabilidad
# tupla=("Steven","Mecatronica","202101713",21)
# tupla=list(tupla)
# print(tupla)
# t2=["Kyra","Oceanografia","20218382",20]
# print(tuple(t2))

#Conjuntos (Set)
#No poseen orden
#No poseen elementos repetidos
#Permiten modificaciones

# c1={"steven","melany","fernando","kyra","steven"}
# print(c1)

lista=["Calculo","Fisica","Programacion","Ingles","Ingles","Calculo"]
#################################################
# lista_sin_repetir=[]
# for elemento in lista:
#     if elemento not in lista_sin_repetir:
#         lista_sin_repetir.append(elemento)
#################################################
#Utilizando set
# lista_sin_repetir=list(set(lista))
# print(lista_sin_repetir)
#################################################

materias=set(lista)
# print(materias)
#Para agregar un solo elemento
# materias.add("Calculo")

#Para agregar mas de un elemento
materias.update(["Calculo","ARP","Quimica","Tenis"])
# print(materias)

#Como elimino elementos
#Elemento aletorios
# materias.pop()
# #Elemento especifico
# materias.remove("Tenis")
# print(materias)

#Operaciones de conjuntos
materias2={"Fisica","Calculo Vectorial","Algebra","Programacion"}
# print(materias2)
# UNION
# union=materias.union(materias2)
union=materias|materias2
# print(union)

#Interseccion
# interseccion=materias.intersection(materias2)
interseccion=materias&materias2
# print(interseccion)

#Diferencia
# diferecia=materias.difference(materias2)
diferecia=materias-materias2
# print(diferecia)

#Diferencia simetrica
# d_simetrica=materias.symmetric_difference(materias2)
d_simetrica=materias^materias2
# print(d_simetrica)


#Diccionarios
#Son modificables
#No utilizan indices
#utilizan la relacion clave:valor
#Las claves solo pueden elementos inmutable

diccionario={"nombre":"Steven","edad":21,"matricula":202101713,
             "materias":["Calculo","Programacion","Algebra","ARP"],
             "ise":3,("Provincia","Ciudad"):["Manabi","Portoviejo"]}



#EJERCICIO
# Para match.com es importante emparejar personas para este día del Amor y de la Amistad. 
# Para esto cuenta con un diccionario personas con la siguiente estructura:
# personas = { 'P1021' : {'alegre', 'fumador', 'hacker', 'deportista',… },
# 'P1001' : {'farrero', 'deportista', 'programador', 'fabuloso',… }
# ,… }
personas = { 'P1021' : {'alegre', 'fumador','estudioso', 'hacker', 'deportista' },
             'P1001' : {'farrero', 'deportista', 'programador', 'fabuloso' },
             'P1031' : {'fumador','estudioso','deportista','triste','enojon'},
             'P1041' : {'farrero','hacker','alegre','estudioso','deportista'}
            }

#           cantidad de caracteristicas que tengan en comun
# Tanimoto= ------------------------------------------------
#          cantidad de caracteristicas en total entre los dos

# [7 puntos] La función hayEmparejamiento(codigoP1, codigoP2, dicPersonas, aceptacion) 
# que recibe el código de dos personas, el diccionario de personas y el nivel de aceptación 
# (entre 0 y 1). Esta función devolverá una tupla con el valor del índice de Tanimoto y 
# un valor de verdad True en el caso de que haya emparejamiento y False en caso contrario. 
# Hay emparejamiento cuando el valor del índice de Tanimoto es superior o igual al nivel de 
# aceptación

def emparejamiento(c1,c2,dicPersonas,tolerancia):
    comun=len(dicPersonas[c1]&dicPersonas[c2])
    totales=len(dicPersonas[c1]|dicPersonas[c2])
    taminoto=round(comun/totales,2)
    aceptacion=False
    if taminoto>=tolerancia:
        aceptacion=True

    return taminoto,aceptacion


x=emparejamiento("P1021","P1041",personas,0.6)
print(x)