import procesosInteragua as fun
clientes = ["Rogelio Vanegas / Enero", "Rogelio Vanegas / Febrero", "Rogelio Vanegas / Marzo", "Carol Arteaga / Enero","Carol Arteaga / Febrero","Carol Arteaga / Marzo",
"David Orozco / Enero","David Orozco / Febrero","Margarita Defaz / Marzo","Margarita Defaz / Enero"]

consumo = [50,150,120,200,55,87,102,365,210,110]

while True:
  op= fun.menu()
  if op==1:
    clientes,consumo = fun.ver_listado(clientes,consumo)
  if op==2:
    cli,rec = fun.calculos(clientes,consumo)
    print(cli,rec)
  if op==3:
    fun.ingresar(rec)
  if op==4:
    fun.salir()