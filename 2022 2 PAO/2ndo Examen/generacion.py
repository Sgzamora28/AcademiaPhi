import random as rd

def generacionTema1():
  with open("2ndo Examen\\dataset.csv","w",encoding="utf-8") as escritor:
    with open("2ndo Examen\\datos.csv",encoding="utf-8") as lector:
      x=lector.readline()
      meses=x.strip().split(":")[1].split(",")
      y=lector.readline()
      farmacias=y.strip().split(":")[1].split(",")
      escritor.writelines([x,y,lector.readline()])
      for i in range(1500):
        fecha="2022-"
        fecha+=rd.choice(meses)+"-"+str(rd.randint(1,30))
        farmacia=rd.choice(farmacias)
        valor=rd.randrange(3000)/100

        escritor.write(f"{fecha},{farmacia},{valor}\n")

def generacionTema2():
  diccionario={}
  with open("2ndo Examen\\tema2.csv") as arch:
    farmacias=arch.readline().strip().split(",")
    medicamentos=arch.readline().strip().split(",")
    for medicamento in medicamentos:
      lista=[]
      cantidad=rd.randint(4,13)
      while len(lista)!=cantidad:
        eleccion=rd.choice(farmacias)
        while eleccion in lista:
          eleccion=rd.choice(farmacias)
        lista.append(eleccion)
      diccionario[medicamento]=lista
  return diccionario

print(generacionTema2())
# generacionTema1()

