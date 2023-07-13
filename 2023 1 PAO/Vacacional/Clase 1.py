#DATOS ----> MATERIALES PARA PROGRAMAR

#DATOS PRIMITIVOS

#DE TIPO NUMERICO

#NUMEROS ENTEROS ----> datos de tipo "int" 
aleatorio=203829492
edad=14
#NUMEROS DECIMALES ----> datos de tipo "float"
nota1=16.45
nota_2=14

#OPERACIONES CON DATOS NUMERICOS
#SUMA---> +
suma=nota1+nota_2
# print(suma)
#RESTAR---> -
resta=nota1-nota_2
# print(resta)
#DIVIDIR---> /
division=nota1/nota_2
# print(division)
#MULTIPLICAR---> *
multipliacion=nota1*nota_2
# print("El resultado de la multipliacion es igual a",multipliacion)
#POTENCIA---> **
potencia=nota_2**2
# print(potencia)
#DIVSION ENTERA----> //
division_entera=nota1//nota_2
# print("La division entera es",division_entera) #----> 2
#MODULO---> %
modulo=5%2
# print(modulo)

#DIVISIBILIDAD
#Yo quiero saber si un numero es par (los numeros pares son los divisibles para 2)

comprobacion=4%2
# print(comprobacion)







#DE TIPO TEXTO -----> datos de tipo "str" (cadenas/strings)
saludo="hola que hace"
despedida="nos vemos pronto"


#CONCATENACION (suma)
#SOLO ENTRE STR
frase=saludo+","+despedida
# print(frase)
#REPETICION (multiplicacion)
frase2=saludo*3 #saludo+saludo+saludo
# print(frase2)

#DE TIPO LOGICO ----> datos de tipo "bool" (booleans)
valor=True
valor2=False



#IGUALDAD ---> ==
#Entre numeros
comprobacion1=nota1==nota_2
# print(comprobacion1)

#Entre str
f1="hola que hace"
f2="hola que hace"
comprobacion2=f1==f2
# print(comprobacion2)

#DESIGUALDAD ---> !=

comprabacion3=nota1!=nota_2
# print(comprabacion3)

comprabacion4=f1!=f2
# print(comprabacion4)

#MAYOR/MENOR (O IGUAL) QUE
#Solo para numeros

#Mayor/Menor que (</>)
c5=-5>-1
print(c5)

#Mayor/Menor o igual que
c6=5>=5
print(c6)

#Disyuncion V ---> or
operacion1=c5 or c6
# print(operacion1) 

#Conjuncion ^ ---> and
operacion2=c5 and c6
print(operacion2)

#Negacion ---> not()
negacion1=not(operacion1)
# print(negacion1)
negacion2=not(operacion2)
print(negacion2)




#VARIABLES ---> CAJAS DE MATERIALES
nota2=16
promedio=(nota1+nota2)/2


#FUNCIONES -----> HERRAMIENTAS PARA CONSTRUIR
#print ---> mostrar por pantalla un valor 
