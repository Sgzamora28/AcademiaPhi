import random as rd
lst_numeros=[5,5,2,4,7,2,1,0,3,4]

rd.shuffle(lst_numeros)
print(lst_numeros)
copia=lst_numeros.copy()
##################################################
#Codigo con mala practica
contador=0
for numero in lst_numeros:
  if numero==0:
    lst_numeros.clear()

  else:
    contador+=1

print(contador)
##################################################
lst_numeros=copia
#Codigo correcto
contador=0
final=""

while final!=0:
  final=lst_numeros[contador]
  contador+=1

print(contador-1)