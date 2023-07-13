import random as rd
ejercicios = ['sentadillas', 'flexiones', 'trotar', 'abdominales']
minutos = [10, 12, 22, 15]
tiempo=int(input('Ingrese su tiempo disponible para la rutina: '))
# indices=list(range(len(minutos)))#[0, 1, 2, 3]

rutina=[]
verificados=[]
tiempo_total=0

while not(len(verificados)==len(ejercicios)):#con esta nueva condicion me aseguro que se evaluen todos los ejercicios de la lista ejercicios
  # indice_aletorio=rd.choice(indices)
  indice_aletorio=rd.randrange(len(ejercicios))
  ejercicio=ejercicios[indice_aletorio]
  if ejercicio not in verificados:#si el ejercicio ya fue evaluado, se salta esta parte del codigo
    verificados.append(ejercicio)
    if tiempo_total+minutos[indice_aletorio]<=tiempo:#aqui hago la verificacion de que el tiempo que aniade el nuevo ejercicio no sobrepase al tiempo establecido
      rutina.append(ejercicio)
      tiempo_total+=minutos[indice_aletorio]


print('Rutina sugerida: ',rutina)
print('Total de tiempo: ',tiempo_total)

  