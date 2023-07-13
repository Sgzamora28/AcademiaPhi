import numpy as np
#pag_###.txt---> pag_01.txt pag_02.txt
ruta="Examen p2 1PAO\\archivos\\"
t_paginas=("pagina_01.txt","pagina_02.txt","pagina_03.txt","pagina_04.txt")



###############################################
#Palabra; p. ###,###,###

#Abismo; p. 11, 15
#Camarada p. 2, 4
glosario={}


#"2,3,4,5"---->split(",")---> x=["2","3","4","5"]
#strings=[]
# for numero in x:
#   strings.append(str(numero))
#",".join(x)
#
# 
# 
# 
# 
# numeros=[2,3,4]
# vector=np.array(numeros,str) 

# i=1
for i in range(len(t_paginas)):
  pagina=t_paginas[i]
  with open(ruta+pagina) as pag:
    for line in pag:
      lista=line.strip().lower().split()
      # print(lista)

      for palabra in lista:
        
        if palabra not in glosario:
          glosario[palabra]=[]

        glosario[palabra].append(i+1)

# print(glosario)
claves=list(glosario.keys())
claves.sort()

with open(ruta+"glosario.txt","w") as arch:
  # print(claves)
  for p in claves:
    paginas=glosario[p]
    v_paginas=np.array(paginas,str)#----> ["2" "3" "4"]   ["2","3","4"]
    arch.write("{}; p. ".format(p.title()))
    arch.write("{}\n".format(", ".join(v_paginas)))#  lista=["Steven","Zamora","Cevallos"]---> " ".join(lista)---> Steven Zamora Cevallos
    # arch.writelines(v_paginas)
    # arch.write("\n")