import random as rd
palabras=['espol','programacion','fundamentos','calculo','donalt']
vocales='aeiou'
elegida=rd.choice(palabras)
secreto=elegida
vocal=[]
for letra in secreto:
    if letra in vocales and letra not in vocal:
        vocal.append(letra)
vocal_escogida=rd.choice(vocal)

palabra=''
for letra in secreto:
    if letra==vocal_escogida:
        palabra+=letra
    else:
        palabra+='-'

y=[]
for x in palabra:
    y.append(x)

print(palabra)

turnos=2*len(secreto)
jugados=0

while turnos!=0:
    turno=input('Ingrese una letra: ').lower()
    while not(len(turno)==1 and turno.isalpha()):
        turno=input('Ingreso incorrecto. Ingrese solo una letra: ').lower()
    if turno in secreto:
        verificador=secreto.count(turno)
        while verificador!=0:
            correcta=secreto.index(turno)
            secreto=secreto[:correcta+1].replace(turno,'@')+secreto[correcta+1:]
            y[correcta]=turno
            verificador-=1
        print(''.join(y))
        jugados+=1

    elif turno in elegida and turno not in secreto:
        print('Esta letra ya fue adivinada, intente con otra')

    else:
        turnos-=1
        print('Letra incorrecta, te quedan {} turno(s)'.format(turnos))
        jugados+=1
        if turno==0:
            print('Game Over')
    
    if '-' not in y:
        turnos=0
        print("Ha adivinado la palabra correctamente")
        print("Jugo un total de {} turnos".format(jugados))