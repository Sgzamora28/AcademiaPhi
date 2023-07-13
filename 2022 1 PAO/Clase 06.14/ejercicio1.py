#1315987204
def cedulaValida(cedula):
    validacion1=len(cedula)==10 #True/false
    validacion2=1<int(cedula[:2])<24 #True/false
    validacion3=int(cedula[2])<6
    a=[2,1,2,1,2,1,2,1,2,0]
    ced=[]#[1,3,1,5,9,8,7,2,0,4]
    for digito in cedula:
        ced.append(int(digito))
    
    sum=0
    for i in range(len(a)):
        x=a[i]*ced[i]
        if x>=10:
            x=(x//10)+(x%10)
        sum+=x
        
    
    residuo=sum%10
    if residuo==0:
        result=0
    else:
        result=10-residuo
    
    validacion4=int(cedula[-1])==result

    final=validacion1 and validacion2 and validacion3 and validacion4

    return final


cedula=input('cedula: ')
x=cedulaValida(cedula)
print(x)