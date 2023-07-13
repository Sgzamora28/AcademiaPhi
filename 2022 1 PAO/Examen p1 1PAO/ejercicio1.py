def racha(lista):
  final=0
  x=0
  for i in range(len(lista)):
    if i!=len(lista)-1:
      if lista[i]==1:
        x+=1

      
      else:
        if x>final:
          final=x
        x=0

    else:
      if lista[i]==1 and x!=0:
        x+=1
        if x>final:
          final=x

  return final



# main
lista1=[0,1,1,0,1,1,1,0,0,1]
lista2=[1,0,0,1,0,1,1,1,1,1,0,0,1,1]
x=racha(lista1)
print(x)
x=racha(lista2)
print(x)