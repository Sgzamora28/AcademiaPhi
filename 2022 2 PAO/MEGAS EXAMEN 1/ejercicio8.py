def seleccionar_numeros(numeros,Num):
  resultado=[]
  for numero in numeros:
    if numero%Num!=0:
      resultado.append(numero)

  return resultado


i=0
for valor in seleccionar_numeros((range(0,10)),4):
  print(i,valor)
  i+=1