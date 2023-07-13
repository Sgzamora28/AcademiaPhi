import numpy as np
lst_datos = ['112|CampoBolivar|0-2|97', '116|CampoZamora|3-0|86', 
'117|CampoTungurahua|4-3|101', '119|CampoPastaza|2-1|78','113|CampoGuayas|1-3|65']


def ubicarCampos(lista:list):
    matriz_campos=np.zeros((5,5),int)
    matriz_barriles=np.zeros((5,5),int)
    for dato in lista:
      campos,nombre,coordenada,barriles=dato.split("|")
      coor=coordenada.split("-")
      x=int(coor[0])
      y=int(coor[1])
      matriz_campos[x,y]=campos
      matriz_barriles[x,y]=barriles

    return matriz_campos,matriz_barriles


# print(ubicarCampos(lst_datos))



print(ubicarCampos(lst_datos)[0])