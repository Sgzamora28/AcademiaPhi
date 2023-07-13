import random as rd
print('Suerte en el juego')
print('o _ _ _ _ _')
intentos=5
avance=0

#condiciones del game over---> avance==5 or intentos==0

while not(avance==5 or intentos==0):
    jugador=input('Ingrese un caracter para dar el avance: ')
    aleatorio=rd.randint(1,3)
    avance+=aleatorio
    if avance>5:
        retroceso=avance-5
        print('El sistema genero {} paso(s) y regreso {} posicion(es)'.format(aleatorio,retroceso))
        avance=5-retroceso
    else:
        print('El sistema genero {} paso(s)'.format(aleatorio))
    
    camino=[' _ ']*6 #['-','-','-','-','-','-']
    camino[avance]=jugador
    print('Camino'+''.join(camino))
    intentos-=1

    if avance==5:
        print('Lograste cruzar el camino')

    elif intentos==0:
        print('No lograste cruzar el camino')

    #l=[1,2,3,4]
    #cadena='-'.join(l) #'1-2-3-4'

