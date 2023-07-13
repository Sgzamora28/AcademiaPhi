def seleccionar_numeros(numeros, num):
  resultado=[]
  for numero in numeros:
    if numero%num!=0:
      resultado.append(numero)
  
  return resultado

i=0
for valor in seleccionar_numeros(range(0,10),4): #[0,1,2,3,4,5,6,7,8,9]
  print(i,valor)
  i+=1


#codigo realizado
lst_numeros=[5,8,4,9,7,0,1]
contador=0
for numero in lst_numeros:
  if numero==0:
    lst_numeros.clear()
    # break
  else:
    contador+=1

print(contador)


#solucion
lst_numeros=[5,8,4,9,7,0,1]
contador=0
numero=lst_numeros[contador]
while numero!=0:
  contador+=1
  numero=lst_numeros[contador]

print(contador)

i=0
final=''
while final!=0:
     final=lst_numeros[i]
     i+=1

print(i-1)  