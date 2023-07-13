def solicitar():
    '''Crea una lista con las caficaciones ingresadas'''
    datos=input('Ingrese 6 calificaciones obtenidas en una asignatura: ')#los input guardan strings
    #condicion correcta--->datos.count(',')==5
    while datos.count(',')!=5:
        datos=('Ingrese solamente 6 calificaciones, recuerde separarlas por comas: ')
    #lista=['6','10','8','9',10,7]
    #porcion=lista[:3]
    calificaciones=datos.split(',')
    for i in range(len(calificaciones)):
        calificaciones[i]=int(calificaciones[i])

    return calificaciones

def promedio(lista):
    lista.sort(reverse=True)
    promedio=sum(lista[:4])/4
    return promedio

def categoria(promedio):
    '''Funcion que retorna la cualificacion del promedio'''
    if promedio>9:
        return 'A'
        # categoria='A'
    elif 8<promedio<=9:
        return 'B'
        # categoria='B'
    elif 7<promedio<=8:
        return 'C'
        # categoria='C'
    elif 6<promedio<=7:
        return 'D'
        # categoria='D'
    else: 
        return 'E'
        # categoria='E'
    
    # return categoria

