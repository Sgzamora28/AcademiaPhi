#funciones
def extraer_datos(l_tweets,ciudad):
  fechas=[]
  minimas=[]
  maximas=[]

  for tweet in l_tweets:
    c2=''
    tweet=tweet.split(' ')
    for i in range(len(tweet)):

      if tweet[i]=='DIA':
        fecha=tweet[i+1]

      if tweet[i]=='CIUDAD':
        c2=tweet[i+1]

      if c2==ciudad:
        if fecha not in fechas:
          fechas.append(fecha)
        if tweet[i]=='TEMP_MIN':
          t_min=float(tweet[i+1])
          minimas.append(t_min)
        
        if tweet[i]=='TEMP_MAX':
          t_max=float(tweet[i+1])
          maximas.append(t_max)

  return fechas,minimas,maximas
#main

tweets = ['El DIA 2021-05-17 en la CIUDAD Latacunga se registró una TEMP_MIN 18.3 grados centígrados y una TEMP_MAX 27.7 grados centígrados.',
          'El DIA 2018-01-11 en la CIUDAD Latacunga se registró una TEMP_MIN 21.2 grados centígrados y una TEMP_MAX 32.3 grados centígrados.',
          'El DIA 2018-01-11 en la CIUDAD Salinas se registró una TEMP_MIN 20.3 grados centígrados y una TEMP_MAX 26.5 grados centígrados.',
          'El DIA 2020-05-09 en la CIUDAD Latacunga se registró una TEMP_MIN 17.5 grados centígrados y una TEMP_MAX 24.2 grados centígrados.']

fechas,minimas,maximas=extraer_datos(tweets,'Latacunga')
promedios=[]
for i in range(len(fechas)):
  promedio=(minimas[i]+maximas[i])/2
  promedios.append(promedio)


mes1=input('Ingrese un numero de mes: ')#'12'
#condiciones correectas---> mes.isdigt() and 1<=mes<=12
while not(mes1.isdigit() and 1<=int(mes1)<=12):
  mes1=input('Ingrese un numero de mes valido: ')

mes1=int(mes1)
print(promedios)
promedio_menor=max(promedios)
for i in range(len(fechas)):
  mes2=fechas[i].split('-')[1]
  if mes1==int(mes2):
    if promedios[i]<promedio_menor:
      promedio_menor=promedios[i]

print('Para el mes de {}. El promedio de temperatura menor fue {}'.format(mes1,promedio_menor))