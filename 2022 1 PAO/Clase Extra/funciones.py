#escriba una funcion que reciba una lista de valores de km de un radar y un valor maximo, la funcion debe RETORNAR una lista con los valores que
#superan al valor maximo ingresado 
#[100, 89, 60, 110]--->4
#   0   1    2   3
#maximo=90
def multas(lista,maximo):
    multados=[]
    #for por indices---> listas paralelas
    # for i in range(len(lista)): # range(4)---> [0,4)
    #     if lista[i]>maximo:
    #         multados.append(lista[i])

    #for por contenido
    for km in lista:
        if km>maximo:
            multados.append(km)
    # i=0
    # while i<len(lista):
    #     if lista[i]>maximo:
    #         multados.append(lista[i])
    #     i+=1
    return multados


# x=multas(lista,km_maximo)
