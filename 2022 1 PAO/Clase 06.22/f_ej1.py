def menor(productos,costos,ref):
    nombres=[]
    for i in range(len(productos)):
        if costos[i]<ref:
            nombres.append(productos[i])
    return nombres


def encarecimiento(listaE,tipo):
    '''Esta funcion devuelve la cantidad de elementos con encarecimiento positivo o negativo y su promedio

    '''
    cantidad=0
    sumatoria=0
    # for i in range(len(listaE)):
    if tipo=='positivo':
        for veri in listaE:
            if veri>0:
                cantidad+=1
                sumatoria+=veri

    else:
        for veri in listaE:
            if veri<0:
                cantidad+=1
                sumatoria+=veri

    promedio=sumatoria/cantidad
    
    return cantidad,promedio