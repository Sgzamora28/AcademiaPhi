# Implemente la función racha(lista) que reciba una lista de cualquier longitud compuesta únicamente de ceros (0) y unos (1) en un orden aleatorio. 
# Recorriendo la lista una sola vez, la función debe retornar el tamaño de la mayor racha (cantidad de unos consecutivos) detectados en la lista.
# Ejemplo:
# Si lista=[0,1,1,0,1,1,1,0,0,1] entonces el tamaño de la mayor racha es 3.


# Si lista=[1,0,0,1,0,1,1,1,1,1,0,0,1,1] entonces el tamaño de la mayor racha es 5.
# Ayuda: Para resolver este problema utilice un contador y recuerde que SOLO DEBE recorrer la lista UNA vez. No hay while ni for anidados.



#["Steven","Zamora","Cevallos"]
#    0         1        2
def racha(lista):
  mayor=0
  x=0 #contador que va a almacenar las rachas
  for i in range(len(lista)):
    if i!=len(lista)-1:

      if lista[i]==1:
        x+=1


      
      else:
        if x>mayor:
          mayor=x
        x=0

    else:
      if lista[i]==1 and x!=0:
        x+=1
        if x>mayor:
          mayor=x

  return mayor


#main
contador=racha([0,1,1,0,0,0,0,1,1,1])
print(contador)