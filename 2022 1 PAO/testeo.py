#Pregunta 3
def extraer_datos(tweets, ciudad):
  fechas=[]
  minimas=[]
  maximas=[]
  for tweet in tweets:
    palabras=tweet.split(" ")
    for i in range(len(palabras)):
      if palabras[i]=="DIA":
        fecha=palabras[i+1]
      if palabras[i]=='CIUDAD':
        c2=palabras[i+1]
      if palabras[i]=="TEMP_MIN":
        t_min=palabras[i+1]
      if palabras[i]=='TEMP_MAX':
        t_max=palabras[i+1]

    if c2==ciudad:
      fechas.append(fecha)
      maximas.append(t_max)
      minimas.append(t_min)

  return fechas,minimas,maximas

#main tema 3
tweets = ['El DIA 2021-05-17 en la CIUDAD Guayaquil se registró una TEMP_MIN 18.3 grados centígrados y una TEMP_MAX 27.7 grados centígrados.',
          'El DIA 2018-01-11 en la CIUDAD Guayaquil se registró una TEMP_MIN 21.2 grados centígrados y una TEMP_MAX 32.3 grados centígrados.',
          'El DIA 2018-01-11 en la CIUDAD Latacunga se registró una TEMP_MIN 20.3 grados centígrados y una TEMP_MAX 26.5 grados centígrados.', 
          'El DIA 2020-04-09 en la CIUDAD Guayaquil se registró una TEMP_MIN 17.5 grados centígrados y una TEMP_MAX 24.2 grados centígrados.', 
          'El DIA 2020-04-09 en la CIUDAD Latacunga se registró una TEMP_MIN 7.5 grados centígrados y una TEMP_MAX 12.2 grados centígrados.']
fechas,t_minimas,t_maximas=extraer_datos(tweets,"Latacunga")
t_promedios=[]
for i in range(len(fechas)):
  promedio=(float(t_minimas[i])+float(t_maximas[i]))/2
  t_promedios.append(promedio)

mes=input('Ingrese un numero de mes: ')
while not(mes.isdigit() and 1<=int(mes)<=12):
  mes=input('Ingrese un numero de mes valido: ')
mes=int(mes)

resultado=max(t_promedios)
verificador=0
for i in range(len(fechas)):
  anio,mes2,dia=fechas[i].split('-')
  if mes==int(mes2):
    if t_promedios[i]<=resultado:
      verificador=1
      resultado=t_promedios[i]

if verificador==1:
    print("La menor tempratura para el mes {} es {:.2f}".format(mes,resultado))
else:
    print("No hay registros para esa fecha ingresada")