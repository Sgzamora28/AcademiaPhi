lista=[1,2,4,'Pablito',True,12.4]#son mutables
lista.remove('Pablito')
lista[2]=15
print(lista)

# for elemento in lista:
    # print(elemento)
#que puedo hacer con tuplas
tupla=(1,2.5,True,'Pedro')#son inmutables
print(tupla)
tupla_nueva=tupla[:2]#permiten slicing
primer_valor=tupla[0]#permiten index
# print(tupla_nueva)
print(primer_valor)#permiten recorrido
for i in tupla:
    print(i)

#convertir tupla a lista y visceversa

tupla1=tuple(lista)
print(tupla1)

lista1=list(tupla)
lista1[1]=12.5
print(lista1)

#operaciones con tuplas
#----concatenar tuplas-----
t1=(1,3,6,3)
t2=('Steven','Pol','Tamara','Daniela')
t3=t1+t2
print(t3)

t4=t1*2
print(t4)

#---comprobacion---
comprobacion='Steven' in t2
print(comprobacion)


