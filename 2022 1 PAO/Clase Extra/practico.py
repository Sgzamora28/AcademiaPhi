def long_max(palabras):
  lista=[ ]
  for palabra in palabras:
    long1=len(palabra)
    lista.append(long1)
  return max(lista)

def palabras_max(palabras):
  lista=[ ]
  x=long_max(palabras)
  for palabra in palabras:
    if len (palabra)==x:
      lista.append(palabra)
    
  return lista

# Programa Principal
print('Inicio del programa')
nombres=input('Ingrese ')


#pedirle al usuario que ingrese dos listas de nombres y por cada una de ellas se debe retornar los nombres que coincidan con la 
# longitud del nombre mas largo


for i in range(2):
    nombres=input('Ingrese una lista de nombres: ') #'Steven Fernando Kyra Daniel'
    nombres=nombres.split(' ') #['Steven','Fernando','Kyra','Daniel']
    maximo=long_max(nombres)
    print('La longitud de la palabra mas larga es:',maximo)
    lista_maximo=palabras_max(nombres)
    print(lista_maximo)