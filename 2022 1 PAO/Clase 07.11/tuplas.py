#Listas
lista=[1,2,3,4,'Steven',1.3,True]
#mutables
lista[0]='Domenica'
print(lista)
#lista es ordenada
ultimo_elemento=lista[-1]
# print(ultimo_elemento)

#Tuplas--> Listas pero congeladas

tupla=(1,4,5,'Zamora')
primer_elemento=tupla[0]
# tupla[0]=15
for elemento in tupla:
  print(elemento)

#editando elementos de una tupla
conversion1=list(tupla)
conversion1[0]=15
tupla_final=tuple(conversion1)
print(tupla)
print(conversion1)
print(tupla_final)

#slicing de tupla
tupla_vacia=()
primer_elemento=tupla[0]
tupla_chiquita=tupla[:2]
print(tupla_chiquita)

#operaciones de tuplas
tupla_chiquita1=tupla[::2]
tupla_chiquita2=tupla[-2:]
print(tupla_chiquita1+tupla_chiquita2)
print(tupla_chiquita2*2)

#comprobaciones de pertenencia
validacion=5 in tupla_chiquita2
print(validacion)
# x=del(tupla)