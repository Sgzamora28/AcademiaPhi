x="Hola Mundo"
ubi=x.index("a")
x1=x[:ubi+1].replace("o","a")
x2=x[ubi+1:]
nueva_x=x1+x2
print(nueva_x)


y='Adios a todos'

#Indexacion
# primerCaracter=x[10]
# print(primerCaracter)


#Slicings
corta=x[::2]
# print(corta)

# #Operaciones de strings

# #longitud
# longitud=len(x)
# # print(longitud)
# # print(x)

# #pertenencia
# # print(verificacion)


# subStr=input("Ingrese la cadena a buscar: ").capitalize()
# verificacion=subStr in x
# print(verificacion)


#buscar una letra
ubicacion=x.lower().index('m')
# print(ubicacion)

ubicacion=x.find("Mundos")
# print(ubicacion)