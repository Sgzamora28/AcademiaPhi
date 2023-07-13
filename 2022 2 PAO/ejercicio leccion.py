import string  
abc=string.ascii_lowercase

import random as rd
aleatorio=rd.randrange(4,10)

palabras=[]
for i in range(aleatorio):
  palabra=""
  x=rd.randint(5,15)
  for j in range(x):
    letra=rd.choice(abc)
    while letra in palabra:
      letra=rd.choice(abc)
    palabra+=letra

  mayus1=rd.randrange(len(palabra))
  mayus2=rd.randrange(len(palabra))
  while mayus2<=mayus1:
    mayus1=rd.randrange(len(palabra))
    mayus2=rd.randrange(len(palabra))

  palabra=palabra[:mayus1]+palabra[mayus1].upper()+palabra[mayus1+1:mayus2]+palabra[mayus2].upper()+palabra[mayus2+1:]
  
  palabras.append(palabra)


palabras.sort()
# for p in palabras:
  # print(p)


#Ejercicio 2
lista=['www.espol.edu.ec',"a","a","A",'www.espol.edu.ec']
listanueva=[]
for direc in lista:
  listanueva.append(direc.lower())


i=0
ganador=""
for url in listanueva:
  contador=listanueva.count(url)
  if contador>=i:
    i=contador
    ganador=url

print("El URL mas visitado es",ganador,"con",i,"visitas")