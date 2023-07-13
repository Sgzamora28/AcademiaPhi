#diccionarios

#todos los elementos del diccionario tienen dos partes clave:valor
 #clave---> un tipo de elemento inmutable (String,int,tupla)
 #valor---> cualquier tipo de elemento (inmutable o mutable)


#los elemetos del diccionario no estan en un orden en especifico

#Definiendo diccionrios vacios
diccionario={}
diccionario=dict()

#obtener valores de diccionario
dic1={'Nombres':'Steven Gonzalo','Apellidos':'Zamora Cevallos','Edad':20,'Matricula':202101713}
print(dic1['Nombres'])
# correo=dic1['Correo']
correo=dic1.get('Correo')
print(correo)
# print(dic1['Correo'])

#acceder y crear valores en un diccionario
#-->acceso
dic1['Nombres']='Spidy Gonzalez'
#-->creacion
dic1['Correo']='sgzamora@espol.ed.ec'


#eliminar claves en un diccionario
# del(dic1['Nombres'])
print(dic1)

#eliminar todos los datos
# dic1.clear()

#dccionario de numeros
numeros={'x':5,'y':10,'z':11,'w':-1}
longitud=len(numeros)
maximo=max(numeros)
print("longitud:",longitud,'\nmaximo:',maximo)


#guardar las claves de un diccionario en una coleccion
claves=list(dic1.keys())
# print(claves)

#guardar los valores de un diccionario en una coleccion
valores=list(dic1.values())
# print(valores)

#guardar claves y valores de un diccionario en una coleccion
elementos=list(dic1.items())
# print(elementos)

#recorrer diccionario
print()
#for por claves
for claves in dic1:
  elemento=dic1[claves]
  print(claves,elemento)

print()
#for por valores
for valor in dic1.values():
  print(valor)

print()
listaNotas=[("Algebra",70),('Programacion',100),('CV',60)]
d_notas=dict(listaNotas)
print(d_notas)