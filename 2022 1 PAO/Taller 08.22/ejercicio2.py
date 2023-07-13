import numpy as np

ventas=np.random.randint(50000,500000,(5,6))
print(ventas)

tipoGasolina=np.array(['Regular','Extra','Super','Diesel','Premium'])

gasolineras=np.array(['Primax Alborada','PS Los Rios','Mobil Cumbaya','Primax Reina','Lutexsa CIA Ltda','PS Remigio Crespo'])
distrito=np.array(['distrito1','distrito2','distrito1','distrito3','distrito2','distrito4'])
ciudades=np.array(['Guayaquil','Babahoyo','Quito','Portoviejo','Guayaquil','Cuenca'])

# gasolina=input("Ingrese un tipo de gasolina: ")
# i1=np.where(tipoGasolina==gasolina)
# # print(i1)
# m_indexada=ventas[i1].ravel()
# # print(m_indexada)
# prom=m_indexada.mean()
# i2=np.where(m_indexada>prom)

# m_final=gasolineras[i2]
# print(m_final)



#2
ciudad=input("Ingrese una ciudad: ")
i3=np.where(ciudades==ciudad)#---> Arreglo de indices
# print(i3)
m_ciudades=ventas[:,i3]
print(m_ciudades)
print()
m_sumaXgasolinera=np.sum(m_ciudades,axis=0).ravel()
print(m_sumaXgasolinera)
print()
i4=np.where(m_sumaXgasolinera>1500000)
m_final=gasolineras[i3][i4]
print(m_final)
# print(m_ciudades)



