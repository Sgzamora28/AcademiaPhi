# En su programa usted ya tiene definida una lista con las transacciones de las tiendas de Marathon
# Sports en Guayaquil. Cada elemento de la lista es un string con los siguientes campos:
# sector|tienda|categoria|producto|totalVentas|dia-mes-año que contiene el total de ventas en un día
# para un producto​ de una cierta categoría​ en una tienda​ ubicada en un determinado sector​.
transacciones = [ 'centro|Bahia|futbol|zapatos-Adidas|290.78|25-03-2013',
                  'centro|Malecon2000|natacion|chaleco-Fins|110.92|01-02-2014',
                  'sur|MallDelSur|natacion|gafasPiscina-Swingo|90.07|13-05-2014',
                  'centro|Bahia|natacion|zapatos-Nike|315.72|13-12-2015',
                  'norte|CityMall|natacion|gafasPiscina-Adidas|310.19|31-05-2016']
# Escriba sentencias un programa en Python que, usando la información dada, genere la siguiente
# información:
# 1. Tres listas (sur,centro,norte) cuyos elementos son los nombres únicos de las tiendas: una lista
# por cada sector.
# 2. El total de ventas de los productos Adidas en el mes de mayo del año ingresado por teclado.

sur=[]
centro=[]
norte=[]
anio=int(input('Ingrese un anio: '))
#datos=['Steven','Zamora','202101713']
#nombre,apellido,matricula=datos
totalVentas=0
for trans in transacciones:
  sector,tienda,cat,prod,ventas,fecha=trans.split('|')
  dia,mes,anio2=fecha.split('-')
  # print(fecha)
  if sector=='sur' and tienda not in sur:
    sur.append(tienda)
  
  elif sector=='centro' and tienda not in centro:
    centro.append(tienda)

  elif sector=='norte' and tienda not in norte:
    norte.append(tienda)


  if anio2==str(anio) and mes=='05' and 'Adidas' in prod:
    totalVentas+=float(ventas)

print(totalVentas)