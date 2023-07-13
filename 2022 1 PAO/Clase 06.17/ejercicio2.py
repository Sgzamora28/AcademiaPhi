# Se tiene una lista de datos con la información de la cantidad de personas que ha inmigrado de cada país y su capital. Un ejemplo de lista es:
lst_datos = ["España|132|Madrid", "EEUU|242|Washington", "Italia|354|Roma"]

# Implementar un programa en Python que, utilizando la lista de datos, 
# muestre por pantalla otra lista con el total de inmigrantes de 3 países solicitados al usuario por teclado.

# Por ejemplo, si el usuario quiere saber el total de inmigrantes de Ecuador, Italia, y Brasil, la respuesta podría ser:

# [324,354,123]
# #cada valor representa a Ecuador, Italia y Brasil respectivamente


lst_paises=[]
for i in range(3):
    pais=input('Ingrese el pais a verificar: ')
    lst_paises.append(pais)

inmigrates=[]
for dato in lst_datos:
    pais,cantidad,capital=dato.split('|')#['Espania','132','Madrid']
    if pais in lst_paises:
        inmigrates.append(int(cantidad))

print(inmigrates)