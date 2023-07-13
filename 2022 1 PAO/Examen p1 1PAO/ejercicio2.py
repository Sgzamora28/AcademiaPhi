import random as rd


aleatoria=[]
while len(aleatoria)!=50:
  x=rd.randint(1,800)
  if x not in aleatoria:
    aleatoria.append(x)


# print(aleatoria)
suma_efec=0
for i in range(100):
  a2=aleatoria.copy()
  rd.shuffle(a2)
  x=0#cantidad de elementos cambiados
  for i in range(len(a2)):
    if aleatoria[i]!=a2[i]:
      x+=1

  efectivdad=x*100/len(a2)
  suma_efec+=efectivdad		

promedio=suma_efec/100

print("El promedio de efectividad es:",promedio)
