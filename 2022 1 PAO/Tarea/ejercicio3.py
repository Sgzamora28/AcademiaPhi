def simplificacion(num,dem):
    mayor=max([num,dem])
    while mayor>1:
        if num%mayor==0 and dem%mayor==0:
            dem=int(dem/mayor)
            num=int(num/mayor)
        mayor-=1
    return num,dem

def suma(num1,num2,den1,den2):
    if den1==den2:
        den_sum=den1
        num_sum=num1+num2
    else:
        den_sum=den1*den2
        num_sum=int((den_sum/den1)*num1+(den_sum/den2)*num2)

    num_sum,den_sum=simplificacion(num_sum,den_sum)
    return num_sum,den_sum

def resta(num1,num2,den1,den2):
    if den1==den2:
        den_res=den1
        num_res=num1-num2
    else:
        den_res=den1*den2
        num_res=int((den_res/den1)*num1-(den_res/den2)*num2)

    num_res,den_res=simplificacion(num_res,den_res)
    return num_res,den_res

def multplicacion(num1,num2,den1,den2):
    num_mul=num1*num2
    den_mul=den1*den2
    num_mul,den_mul=simplificacion(num_mul,den_mul)
    return num_mul,den_mul

def divison(num1,num2,den1,den2):
    num_div=num1*den2
    den_div=den1*num2
    num_div,den_div=simplificacion(num_div,den_div)
    return num_div,den_div


#main
frac1=input('Ingrese una fraccion en la forma u/v: ')
frac2=input('Ingrese una fraccion en la forma u/v: ')
num1,den1=frac1.split('/')
num2,den2=frac2.split('/')
num1=int(num1); num2=int(num2)
den1=int(den1); den2=int(den2)
num_sum,den_sum=suma(num1,num2,den1,den2)
num_res,den_res=resta(num1,num2,den1,den2)
num_mul,den_mul=multplicacion(num1,num2,den1,den2)
num_div,den_div=divison(num1,num2,den1,den2)
print('\n')
#suma
if den_sum!=1:
    print(f'La suma de {frac1} y {frac2} es igual a {num_sum}/{den_sum}')
else:
    print(f'La suma de {frac1} y {frac2} es igual a {num_sum}')


#resta:
if den_res!=1:
    print(f'La resta de {frac1} y {frac2} es igual a {num_res}/{den_res}')
else:
    print(f'La resta de {frac1} y {frac2} es igual a {num_res}')


#multiplicacion
if den_mul!=1:
    print(f'La multiplicacion de {frac1} y {frac2} es igual a {num_mul}/{den_mul}')
else:
    print(f'La multiplicacion de {frac1} y {frac2} es igual a {num_mul}')


#division
if den_div!=1:
    print(f'La divison de {frac1} y {frac2} es igual a {num_div}/{den_div}')
else:
    print(f'La divison de {frac1} y {frac2} es igual a {num_div}')

#valores mayores a menores
terminos=[num1,num2,den1,den2]
terminos.sort(reverse=True)
final='Los terminos ordenados de mayor a menor son: '
for termino in terminos:
    final+=str(termino)+', '
print('\n'+final.strip(', '))


#promedio entre terminos
print('El promedio entre los termino es igual a ', sum(terminos)/4)

#resultados de v/u y/x
print('\n')
num_sum,den_sum=suma(den1,den2,num1,num2)
num_res,den_res=resta(den1,den2,num1,num2)
num_mul,den_mul=multplicacion(den1,den2,num1,num2)
num_div,den_div=divison(den1,den2,num1,num2)

if den_sum!=1:
    print(f'La suma de {den1}/{num1} y {den2}/{num2} es igual a {num_sum}/{den_sum}')
else:
    print(f'La suma de {den1}/{num1} y {den2}/{num2} es igual a {num_sum}')


#resta:
if den_res!=1:
    print(f'La resta de {den1}/{num1} y {den2}/{num2} es igual a {num_res}/{den_res}')
else:
    print(f'La resta de {den1}/{num1} y {den2}/{num2} es igual a {num_res}')


#multiplicacion
if den_mul!=1:
    print(f'La multiplicacion de {den1}/{num1} y {den2}/{num2} es igual a {num_mul}/{den_mul}')
else:
    print(f'La multiplicacion de {den1}/{num1} y {den2}/{num2} es igual a {num_mul}')


#division
if den_div!=1:
    print(f'La divison de {den1}/{num1} y {den2}/{num2} es igual a {num_div}/{den_div}')
else:
    print(f'La divison de {den1}/{num1} y {den2}/{num2} es igual a {num_div}')