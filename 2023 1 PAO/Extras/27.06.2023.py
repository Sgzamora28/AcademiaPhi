def ordenador_telefonico(l_telef):
    nombres=[]#["Steven","Azucena","Majo","Maso"]
    #             0          1       2      3
    numeros=[]#["09787","096140","0986362","098926372"]
    for dato in l_telef:#"Maria/2038482"
        datos=dato.split("/")#["Maria","203882"]
        nombre,numero=datos
        nombres.append(nombre)
        numeros.append(numero)

    nombres_ordenados=nombres.copy()#["Steven","Azucena","Majo","Maso"]
    nombres_ordenados.sort()#["Azucena","Majo","Maso","Steven"]
    #                             0       1      2       3
    numeros_ordenados=[]
    for nombre in nombres_ordenados:
        indice=nombres.index(nombre)#"Azucena"
        n=numeros[indice]#096140
        numeros_ordenados.append(n)

    return nombres_ordenados,numeros_ordenados



