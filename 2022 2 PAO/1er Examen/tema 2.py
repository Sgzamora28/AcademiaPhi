o1 = "La revolucion francesa"
o2 = "i un corso clave la frena"

o1 = o1.lower().replace(' ', '')
o2 = o2.replace(' ','').lower()

l1 = list(o1)
l2 = []

for letra in o2:
  l2.append(letra)

l1.sort()
l2.sort()

if l1==l2:
  print("Son anagramas")
else:
  print("No son anagramas")