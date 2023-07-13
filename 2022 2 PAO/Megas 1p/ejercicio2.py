import random as rd
# Implemente un programa que determine el porcentaje de efectividad de la función random.shuffle. Para esto siga el siguiente algoritmo:
# Genere una lista de 50 números aleatorios únicos (sin repetición) entre 1 y 800, sin usar shuffle.


# Repita los siguientes pasos 100 veces:
# • Desordene la lista del paso 1 usando la función random.shuffle
# • Contar cuántos elementos han cambiado de posición entre la lista del paso 1 y la lista
# retornada por shuffle. Llamemos a este valor X.
# • Calcular el porcentaje de efectividad de cada iteración PEfec con la siguiente fórmula e
# ingrese éste en una nueva lista.
# PEfec = X * 100 / len(lista)
# • Calcule y muestre por pantalla el porcentaje de efectividad total que es promedio de los
# porcentajes de efectividad obtenidos en las 100 repeticiones. En otras palabras, debe
# dividir la suma de todos los porcentajes de efectividad de las repeticiones para 100.


aleatoria=[]

while len(aleatoria)!=50:
  a=rd.randint(1,800)
  if a not in aleatoria:
    aleatoria.append(a)


# for i in range(50):
#   a=rd.randint(1,800)
#   while a in aleatoria:
#     a=rd.randint(1,800)

  # aleatoria.append(a)

# print(aleatoria)
sum_efectividad=0
for i in range(100):
  a2=aleatoria.copy()
  rd.shuffle(a2)
  x=0
  for i in range(len(a2)):
    if a2[i]!=aleatoria[i]:
      x+=1

  efectividad=x*100/len(a2)
  sum_efectividad+=efectividad


promedio=sum_efectividad/100

print("El promedio de efectividad es igual a:",promedio)



