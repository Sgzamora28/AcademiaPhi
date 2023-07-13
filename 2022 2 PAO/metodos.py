import numpy as np

a=np.random.randint(1,10,(3,3))
b=np.random.randint(1,10,(3,1))

a=np.array(a,dtype=float)
b=np.array(b,dtype=float)

#Pivoteo por filas
ab=np.concatenate((a,b),axis=1)
referencia=np.copy(ab)
n,m=ab.shape

for i in range(n-1):
    columna=np.abs(ab[i:,i])
    i_max=np.argmax(columna)

    if i_max!=0:
        cambio=np.copy(ab[i,:])
        ab[i,:]=ab[i_max+i,:]
        ab[i_max+i,:]=cambio


#eliminacion hacia delante
for i in range(n-1):
    pivote=ab[i,i]
    k=i+1
    for j in range(k,n):
        factor=ab[j,i]/pivote
        ab[j,:]=ab[j,:]-ab[i,:]*factor



#sustitucion hacia atras
ufila=n-1
ucolumna=m-1
x=np.zeros(n,dtype=float)

for i in range(ufila,-1,-1):
    suma=0
    for j in range(i+1,ucolumna):
        suma+=ab[i,j]*x[j]
    b=ab[i,ucolumna]
    x[i]=(b-suma)/ab[i,i]

x=np.transpose([x])


for i in range(3,-1,-1):
    print(i)
