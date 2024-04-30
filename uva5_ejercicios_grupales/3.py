"""Una mueblería necesita un sistema para ingresar 10 productos.
Se pide ingresar categoría (A, B o C) y precio.
Validar que el ingreso de la categoría sea de alguna de esas tres letras y que el precio sea positivo. 
Al finalizar, mostrar la cantidad de productos ingresados de cada categoría y el total de importes.  """

sumatoria_precio_c=0
sumatoria_precio_b=0
sumatoria_precio_a=0
cantidad_c=0
cantidad_b=0
cantidad_a=0
for i in range (10):
    categoria = input("categoria A,B,o C: ")
    while categoria != 'A' and categoria != 'B' and categoria != 'C':
        categoria=input("categoria A,B,o C: ")
    precio = int(input("Ingrese precio"))
    while precio <0:
        precio=int(input("Ingrese precio"))
    if categoria == 'C' :
        cantidad_c+=1
        sumatoria_precio_c += precio
    if categoria == 'B':
        cantidad_b += 1
        sumatoria_precio_b += precio
    if categoria == 'A':
        cantidad_a += 1
        sumatoria_precio_a += precio
importe_total = (sumatoria_precio_a + sumatoria_precio_b + sumatoria_precio_c )
print("cantidad de productos ingresados de A: ", cantidad_a)
print("cantidad de productos ingresados de B: ", cantidad_b)
print("cantidad de productos ingresados de C: ", cantidad_c)
print("total de importes: ", importe_total )