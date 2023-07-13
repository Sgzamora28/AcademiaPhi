l = [ 'ATTTGCTTGCTATTTAAACCGGTTATGCATAGCGC', 'ATTAGCCGCTATCGA' ]
r='CG'
v1=0
v2=0
indices=[]
for s in l:
  # print(s)
  inv=s[::-1]
  for i in range(len(inv)):
    if i!=len(s)-1:
      validacion1=inv[i:i+len(r)]
      if validacion1==r:
        v2+=1
        indices.append(i)
  mitad=len(inv)//2
  inv2=inv[mitad+1:]
  for i in range(len(inv2)):
    if i!=len(inv2)-1:
      validacion2=inv2[i:i+len(r)]
      if validacion2==r:
        v1+=1


  if v1==2 and v2>=3:
    print('Secuencia: {}'.format(s))
    print(indices)