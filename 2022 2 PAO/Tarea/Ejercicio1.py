# La lista mostrrada en el ejemplo contiene los URLs de diferentes sitios Web que han sido visitados.
lista = ["www.espol.edu.ec", 
  "www.google.com", 
  "www.sri.gob.ec", 
  "www.fiec.espol.edu.ec", 
  "www.uess.edu.ec", 
  "www.FIEC.espol.edu.ec", 
  "www.fict.espol.edu.ec", 
  "www.fcnm.Espol.edu.ec", 
  "www.ucsg.edu.ec", 
  "www.Stanford.edu", 
  "www.harvard.edu", 
  "www.stanford.edu", 
  "www.UCSG.edu.ec", 
  "www.google.com.ec", 
  "www.facebook.com", 
  "www.opensource.org", 
  "www.educacionbc.edu.mx"]
# Los URLs normalmente se repiten y corresponden algunas veces a universidades de Ecuador y otros países.
# Note que los URLs no diferencian entre mayúsculas y minúsculas.
# Por ejemplo: www.espol.edu.ec y www.ESPOL.edu.ec corresponden al mismo sitio.
# Escriba un programa en Python que dada una lista realice lo siguiente:
# a. Muestre los nombres o siglas de las universidades que aparecen en la lista (sin repetir).
educativos=[]
for url in lista:
  if '.edu' in url:
    www=url.split('.')
    sitio=www[www.index('edu')-1]
    if sitio not in educativos:
      educativos.append(sitio)
print(f'En la lista actual aparecen {len(educativos)} universidades:')
for i in range(len(educativos)):
  universidades=educativos[i]
  print(f'{i+1}. {universidades.upper()}')
print()
# b. Muestre la cantidad y los nombres/siglas de universidades de Ecuador que aparecen en la lista.
nacionales=[]
for url in lista:
  if '.edu' in url and '.ec' in url:
    www=url.split('.')
    nacional=www[www.index('edu')-1].upper()
    if nacional not in nacionales:
      nacionales.append(nacional)
print(f'En la lista actual aparecen {len(nacionales)} universidades de Ecuador:')
for i in range(len(nacionales)):
  universidades=nacionales[i]
  print(f'{i+1}. {universidades}')
print()
# c. Dado un usuario y el nombre o sigla de la universidad, imprima el correo electrónico asignado.
usuario=input('Ingrese el usuario: ').lower()
universidad=input('Ingrese el nombre o las siglas de la universidad: ').lower()
correo=usuario
for url in lista:
  dominio=url.lower().split('.')
  if 'edu' in dominio:
    if universidad==dominio[dominio.index('edu')-1] and '@' not in correo:
      correo+='@'+('.'.join(dominio[dominio.index('edu')-1:])).lower()
if '@' not in correo:
  print('La universidad seleccionada no se encuentra en la lista actual')
else:
  print(f'El correo institucional del usuario es: {correo}')
print()