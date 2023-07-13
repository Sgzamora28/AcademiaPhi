#Listas
#Es ordenada
#Es heterogea
#Son mutables
#Permite la repeticion de elementos


x="Kyra"
lista=["Steven",x,2021]
#         0     1   2
#       -3     -2   -1 
# 
# #Indexacion
# print(lista)
lista[-1]="Azucena"

# Agregar datos
lista.append("Isabel") #Agregar el dato al ultimo
lista.insert(1,'Oceanografia') #Agrega el dato en la posicion que queramos
# print(lista)


#Operaciones con listas

#Suma-Contatenacion
lista2=[284,29384,203,205,203]
lista_concatenada=lista+lista2
# print(lista_concatenada)

#Multiplicacion con int
# print(lista2*3) #lista2+lista2+lista2

#Slicing
print(lista)
listaChiquita=lista[:4]
# print(listaChiquita)
#Invertir una lista 
listaInvertida=lista[::-1]
print(listaInvertida)
