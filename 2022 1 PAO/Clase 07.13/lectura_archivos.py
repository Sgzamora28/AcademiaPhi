#datos que existen solamente en el programa
x='Es una variable'
y=5
z=10
multplicacion=y*z

print(multplicacion)
print('fin programa')
#una vez que termina el programa, estos datos ya no existen

#Escritura
# nomFile=open('ArchivoPrueba.txt','a')#cuando yo quiero escribir datos---> 'w' #cuando yo quiero aniadir datos---> 'a'
# # for i in range(5):
# nombre=input('Ingrese su nombre: ')
# matricula=input('Ingrese su matricula: ')
# facultad=input('Ingrese su facultad: ')
# nomFile.write('{},{},{}\n'.format(nombre,matricula,facultad))
# nomFile.close()#siempre tengo que cerrar ese archivo


#Lectura
lectura=open('ArchivoPrueba.txt','r')
#modo de lectura 1
# for lineas in lectura:
#   nombre,matricula,facultad=lineas.strip().split(',')
#   print('{}'.format(matricula))
  

#modo de lectura 2
linea=lectura.readline()
while linea!='':
  linea=linea.strip('\n')
  print(linea)
  linea=lectura.readline()