def buscar_por_edades(inferior, superior, nombres, edades):
    resultado=[]
    for i in range(len(edades)):
        if inferior<edades[i]<superior:
            resultado.append(nombres[i])
    return resultado