jugadores=['CR7','Neymar Jr.', 'Messi','Maradona','Di Maria']
#cantidad de goles anotados por jugador
goles_anotados=[32,24,45,40,30]
#% de posesión del balón
posesion_balon=[90,84,91,89,70]

#% pases acertados
pases=[54,60,78,60,92]
#tiros directos al arco
tiros=[187,239,112,200,190]
#pais de pertenencia
pais=['Portugal','Brasil','Argentina','Argentina','Argentina']

#literal 1
paises_unicos=[]
for p in pais:
  if p not in paises_unicos:
    paises_unicos.append(p)
print(paises_unicos) #['Portugal', 'Brasil', 'Argentina']

#literal 2
goles_promedio=[]
#metrica goles promedio=goles anotados del país / número de jugadores del pais
for p in paises_unicos:
  total_goles=0
  total_jugadores=0
  for i in range(len(pais)):
    if pais[i]==p:
      total_jugadores+=1
      total_goles+=goles_anotados[i]

  promedio_goles=total_goles/total_jugadores
  goles_promedio.append(promedio_goles)

print(goles_promedio)


efectivdad_promedio=[]
for p in paises_unicos:
  anotaciones=0
  tiros_totales=0
  for i in range(len(pais)):
    if pais[i]==p:
      anotaciones+=goles_anotados[i]
      tiros_totales+=tiros[i]
  
  promedio_efectividad=anotaciones/tiros_totales
  efectivdad_promedio.append(promedio_efectividad)

# print('Efectividad promedio',efectivdad_promedio)
indice_arg=paises_unicos.index('Argentina')
prom_argetina=efectivdad_promedio[indice_arg]
contador=0
for i in range(len(jugadores)):
  if pais[i]=='Argentina':
    efectivdad=goles_anotados[i]/tiros[i]
    # print(efectivdad,jugadores[i])
    if efectivdad>prom_argetina:
      contador+=1

print(contador)

mayor_pases=[]
for i in range(len(pais)):
  if pases[i]>91:
    mayor_pases.append(jugadores[i])
    # print(jugadores[i])

print(mayor_pases)


copia_posesion=posesion_balon.copy()
copia_posesion.sort(reverse=True)
indice_mayor=posesion_balon.index(copia_posesion[0])
print(jugadores[indice_mayor],pais[indice_mayor])



#promedios_mundiales
prom_gol=sum(goles_anotados)/len(goles_anotados)
prom_posesion=sum(posesion_balon)/len(posesion_balon)
prom_pases=sum(pases)/len(pases)
prom_tiros=sum(tiros)/len(tiros)


if goles_anotados[0]>prom_gol and posesion_balon[0]>prom_posesion and pases[0]>prom_pases and tiros[0]>prom_tiros:
  print('CR7 esta por encima del promedio mundial')

else:
  print('CR7 no esta por encima del promedio mundial')
