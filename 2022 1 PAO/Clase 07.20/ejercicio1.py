archivo=open('datos.txt','w')
archivo.write("Dias de la semana\n")
archivo.close()
lista=['lunes','\n','martes','\n','miercoles','jueves','viernes']
archivo=open('datos.txt','a')
archivo.writelines(lista)
archivo.close()