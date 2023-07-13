x1=float(input('Ingrese un numero: '))
x2=float(input('Ingrese otro numero: '))
suma=x1+x2
# print("La suma de",x1,"+",x2," es igual a:",suma)

#El operador %
#operadores para definir tipos de datos
#%s--->str
#%f--->float
#%b--->booleanos
#%d--->int    
# print("La suma de %.2f+%.2f es igual a %.0f"%(x1,x2,suma))


#Formateo con .format
print("La suma entre {:-^10.1f} + {:-^10.1f} es igual a {:.2f}".format(x1,x2,suma))