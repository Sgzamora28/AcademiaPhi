# from f_ej1 import
import f_ej1 as ej1


l_productos=['CEREALES','CARNE','PESCADOS','ACEITE']
l_costos=[47.08,37.95,12.07,40.5]
eL=[-0.42,0.34,-4.25,2.54]


cant,prom=ej1.encarecimiento(eL,'positivo')
print('La cantidad de productos con encarecimiento positivo es {}. Valor promedio: {:.2f}'.format(cant,prom))
referencia=input('Ingrese un valor entero: ')
#condicion correcta---> referencia.isdigit()
while not referencia.isdigit():
    referencia=input('Recuerede que el valor debe ser entero: ')
referencia=int(referencia)

lista_menor=ej1.menor(l_productos,l_costos,referencia)
# print(lista_menor)
print('Productos')
for i in range(len(lista_menor)):
    print('{}. {}'.format(i+1,lista_menor[i].title()))
