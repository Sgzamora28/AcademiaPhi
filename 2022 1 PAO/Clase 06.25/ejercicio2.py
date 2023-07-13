universidadesCosta=["ESPOL", "UTMACH", "UG", "UEES", "UTM", "UTB"] 
ciudadesUC=["Guayaquil", "Machala", "Guayaquil", "Guayaquil", "Portoviejo", "Babahoyo"] 

universidadesSierra=["ESPE", "UTPL", "UPN", "UDLA", "UAZUAY", "UTN"] 
ciudadesUS=["Quito", "Loja", "Quito", "Quito", "Cuenca", "Ibarra"]
             # x                x       x 

# for i in range(len(universidadesCosta)):
#     if ciudadesUC[i]=='Guayaquil':
#         uniGQ.append(universidadesCosta[i])

# for i in range(len(universidadesSierra)):
#     if ciudadesUS[i]=='Quito':
#         uniGQ.append(universidadesSierra[i])

# print(uniGQ)


# print('Punto 1')
# uniGQ=[]#---->len(uniGQ)==uniG+uniQ
# uniG=ciudadesUC.count('Guayaquil')
# uniQ=ciudadesUS.count('Quito')
# # print(uniG,uniQ)
# i=0
# j=0
# while len(uniGQ)!=uniG+uniQ:
#     if i!=len(ciudadesUC):
#         if ciudadesUC[i]=='Guayaquil':
#             uniGQ.append(universidadesCosta[i])
#         i+=1
#     elif j!=len(ciudadesUS):
#         if ciudadesUS[j]=='Quito':
#             uniGQ.append(universidadesSierra[j])
#         j+=1
# uniGQ.sort(reverse=True)
# print(uniGQ)

print('Punto 2')

sinRepetir=list(set(ciudadesUC+ciudadesUS))
copiaUC=ciudadesUC.copy()
copiaUS=ciudadesUS.copy()

print(sinRepetir)
for i in range(len(sinRepetir)):
    lista=[]
    while sinRepetir[i] in copiaUC or sinRepetir[i] in copiaUS:
        if sinRepetir[i] in copiaUC:
            x=copiaUC.index(sinRepetir[i])
            lista.append(universidadesCosta[x])
            copiaUC[x]='x'
        else:
            x=copiaUS.index(sinRepetir[i])
            lista.append(universidadesSierra[x])
            copiaUS[x]='x'
    print(sinRepetir[i])
    print(lista)