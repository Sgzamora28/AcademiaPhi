import random as rd
tareas = ['pintar soldados', 'hornear galletas', 'armar muñecos', 'cortar papel de regalo']
inicio = [678, 200, 240, 423]
duracion = [300, 800, 456, 112]

fin=[]
for i in range(len(duracion)):
    resultado=inicio[i]+duracion[i]
    fin.append(resultado)


verificados=[]
verificador=0
l_tareas=[]
tiempo=[]
#
while len(verificados)!=len(tareas):
    i=rd.randrange(len(tareas))
    tarea=tareas[i]
    if tarea not in verificados:
        verificados.append(tarea)
        if tarea not in l_tareas and verificador+duracion[i]<=1440:
            verificador+=duracion[i]
            l_tareas.append(tarea)
            tiempo.append(duracion[i])

print(l_tareas)
t=tiempo.copy()
t.sort()
j=0
for x in t: #---->[0 3)
    i=tiempo.index(x)
    print("{}. {}".format(j+1,l_tareas[i]))
    j+=1