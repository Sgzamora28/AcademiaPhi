def racha(lista):
  mayor=0
  actual=0
  for i in range(len(lista)):
    if i!=len(lista)-1:
      if lista[i]==1:
        actual+=1


      else:
        if actual>mayor:
          mayor=actual

        actual=0

    else:
      if lista[i]==1 and actual!=0:
        actual+=1
        if actual>mayor:
          mayor=actual

  return mayor


racha_prueba=racha([1,1,1,0,0,0,0,1,1,0,1,1,1,1])
print(racha_prueba)