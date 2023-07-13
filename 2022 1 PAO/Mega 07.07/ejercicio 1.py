lista = [89, 45, 23, 17, 55, 95, 13, 41, 28, 11]
lista.sort()
promedio = sum(lista) // len(lista)
# print(promedio)
menores = []
i = 0
while lista[i] < promedio:
  menores.append(lista[i])
  i += 1
# print(menores)



pal = 'Se van en sus naves'
b = pal[::-1].replace(' ','').lower()
# print(b)
pal_b = pal.lower().replace(' ','')
# print(pal_b)
if pal_b == b:
  print('Es palíndromo')
else:
  print('No es palíndromo')