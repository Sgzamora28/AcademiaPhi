l_edades=[18,20,23,21,20,19,30,25,23]
l_norepetidos=[]
for edad in l_edades:
  if edad not in l_norepetidos:
    l_norepetidos.append(edad)

set_edades=set(l_edades)
l=list(set_edades)
# print(set_edades)

# valor1=set_edades[:2]
# set_edades[0]=3
lista=[]
tupla=()
set1=set()
#no es correcto set1={} 
longitud=len(set_edades)
# maximo=max(set_edades)
# minimo=min(set_edades)
# print(longitud)
# verificacion=18 in set_edades
# print(verificacion)
set_edades.add(16)
# print(set_edades)

set_edades.update([13,25,43,20])
# print(set_edades)
# set_edades.clear()
# print(set_edades)

set_edades.remove(13)
# print(set_edades)


set1={1,4,5,'pera','Steven','manzana'}
set2={4,2,'Steven'}
#union de conjuntos
set3=set1.union(set2) #set1|set2
# print(set3)

#interseccion
set4=set1.intersection(set2) #set1&set2 
# print(set4)

#diferencia
set5=set2.difference(set1)#set2-set1
# print(set5)

#diferencia simetrica
set6=set1.symmetric_difference(set2)#set1^set2
# print(set6)
