import random as rd
#fundamentos
# 1        10
#fsndamentou
def desordenar(palabra):
    x=palabra
    for i in range(6):
        a1=rd.randrange(len(x)) #------> randrange(7)----> [0,7)
        x1=x[a1]
        a2=rd.randrange(len(x))
        while a2==a1:
            a2=rd.randrange(len(x))
        x2=x[a2]
        deletreada=list(x)
        deletreada[a1]=x2
        deletreada[a2]=x1
        desordenada=''.join(deletreada)
        x=desordenada
    
    return desordenada



#main
#base de datos
l_palabras=['hola','futbol','Ecuador','Peru','tenis','basquet']
l_categorias=['saludo','deportes','paises','paises','deportes','deportes']
l_puntos=[5,10,90,90,15,30]

#prep
categoria=input('Ingrese una categoria: ').lower()#---->deportes
while categoria not in l_categorias:
    categoria=input('Ingrese correctamente la categoria: ').lower()

palabras=[]
puntos=[]
correctas=[]
for i in range(len(l_palabras)):
    if l_categorias[i]==categoria:
        palabras.append(l_palabras[i])
        puntos.append(l_puntos[i])


#juego
equivocaciones=0
puntuacion=0
#condiciones del game_over---> equivocaciones==5 or len(palabras)==0
while not(equivocaciones==5 or len(palabras)==0):
    aletoria=rd.choice(palabras)
    x=palabras.index(aletoria)
    palabras.remove(aletoria)
    adivinanza=desordenar(aletoria)
    print(adivinanza)
    intento=input('Trate de adivinar la palabara desordenada: ')
    if intento==aletoria:
        print('Adivino correctamente la palabra')
        puntuacion+=len(aletoria)+puntos[x]
        correctas.append(aletoria)
    else:
        print('No adivino correctamente la palabra')
        equivocaciones+=1
    puntos.pop(x)
print('Game over')
print('Su puntaje es',puntuacion)
print('Palabras adivinidas correctamente\n',correctas)