ganador=74852
        #0 1 2 3 4
        #-5 -4 -3 -2 -1
# boleto=input('Ingrese su boleto')

for i in range(4): #0 1 2 3
  boleto=input('Ingrese su boleto: ')#123456
  #boleto.isdigit() and len(boleto)==5
  while not(boleto.isdigit() and len(boleto)==5):
    boleto=input('Ingrese correctamente su boleto: ')
  boleto=int(boleto)
  if boleto==ganador:
    print('Su boleto es el ganador. Gano la cantidad de 5000 duros')
  
  elif str(boleto)[-2:]==str(ganador)[-2:]:
    print('Los dos ultimos digitos son iguales a los del numero ganador. Ganaste 100 duros')

  elif str(boleto)[-1]==str(ganador)[-1]:
    print('El ultimo digito coincide con el del numero ganador. Ganaste 10 duros')
  
  else:
    print('El boleto no tiene premio ')
