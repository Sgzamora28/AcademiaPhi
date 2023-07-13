from random import *
print('Suerte en el juego')
print('o _ _ _ _ _')


avance=0
intentos=4

#condiciones game over---> avance==5 or intentos==0
turnos=['primer','segundo','tercer','cuarto y ultimo']
i=0
while not(avance==5 or intentos==0):
  jugador=input('Ingrese un caracter para dar el {} avance: '.format(turnos[i]))
  aleatorio=randint(1,3)

  avance+=aleatorio
  if avance>5:
      retroceso=avance-5
      print('El sistema genero {} paso(s) y regreso {} posicion'.format(aleatorio,retroceso))
      avance=5-retroceso
  else:
      print('El sistema genero {} paso(s)'.format(aleatorio))
  camino=[' _ ']*6
  camino[avance]=jugador
  print('Camino: '+''.join(camino))
  intentos-=1
  i+=1
  if avance==5:
      print('Logro cruzar el camino')
  elif intentos==0:
    print('No logro cruzar el camino')
    