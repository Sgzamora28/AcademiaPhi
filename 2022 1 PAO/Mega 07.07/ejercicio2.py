import random as rd
juego=['X']*8+['Rueda']*4
rd.shuffle(juego)
print(juego)

intentos=6
aciertos=0

#game over---> intentos==0 or aciertos==4
acumulado=0
while not(intentos==0 or aciertos==4):
  intento=input('Ingrese un valor entre 0 y 11: ')#el valor lo guarda como str
  #condiciones correctas--> intento intento.isdigit() and int(intento) in range(12)
  while not(intento.isdigit() and int(intento) in range(12)):
    intento=input('Ingrese correctamente el valor a jugar: ')

  intento=int(intento)
 

  if juego[intento]=='Rueda':
    acumulado+=1000
    print('Has acertado, vas ganando {}'.format(acumulado))
    aciertos+=1
  
  else:
    print('No has acertado')

  intentos-=1
  print('Vas encontrando',aciertos,'rueda(s)')
  print('Te quedan {} intento(s)'.format(intentos))


if aciertos==4:
  print('Has ganado un auto 0 km!!')


elif aciertos==0:
  print('No te has llevado ningun premio. F :c')



else:
  print('Felicidades, has ganado ${} :3'.format(acumulado))