#Sets o conjuntos

#sin son mutables
#desordenados
#conjuntos no tienen elementos repetidos


lista=['Zamora','Zamora','Franco','Zambrano','Silva','Gomez','Gomez']
lista_sin_repetir=[]
#metodo zzzzzz
for apellido in lista:
  if apellido not in lista_sin_repetir:
    lista_sin_repetir.append(apellido)

#metodo pepa
set_sinRepetir=list(set(lista))
# print(set_sinRepetir)

#no permiten ni index ni slicing
set_prueba={'Steven','Steven','Zamora','Cevallos',2002,29}
# print(set_prueba)
# print(set_prueba[:2])

#verificar pertenencia
verificacion='Steven' in set_prueba
# print(verificacion)

#iteracion
# for elemento in set_prueba:
#   # print(elemento)
#   print()


#eliminar elemento especifico
# set_prueba.remove(2002)
# print("Set sin 2002:",set_prueba)

#obtener y eliminar del conjunto un elemento aleatorio
# x=set_prueba.pop()
# print("Obtener un elemento aleatorio: ",x)
# print("Set sin el elemento obtenido:",set_prueba)

#eliminar set
# set_prueba.clear()
# print(set_prueba)

#añadir elementos

set_prueba.add(5)
print(set_prueba)
x=len(set_prueba)
print(x)

set2={'29', 'Phi', 'Fundamentos', 'Kyra', '5',2002}
lista=['Steven',"Steven",'Franco','29',29,431,True,False,True]
set2.update(lista)
print(set2)


#Operaciones de conjuntos

#union de conjuntos
union=set_prueba|set2
print(union)
union=set2.union(set_prueba)
# print(union)

#nterseccion de conjuntos
intereccion=set_prueba&set2
# print(intereccion)
intereccion=set2.intersection(set_prueba)
print(intereccion)

#diferencia de conjuntos
diferencia=set_prueba-set2
print(diferencia)
diferencia=set_prueba.difference(set2)
print(diferencia)

#diferencia simetrica
diferencia_simetrica=set2^set_prueba
print(diferencia_simetrica)
diferencia_simetrica=set_prueba.symmetric_difference(set2)
print(diferencia_simetrica)