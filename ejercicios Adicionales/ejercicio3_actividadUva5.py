"""3.Una mueblería necesita un sistema para ingresar 10 productos. Se pide ingresar categoría (A, B o C) y precio.
Validar que el ingreso de la categoría sea de alguna de esas tres letras y que el precio sea positivo. Al finalizar,
 mostrar la cantidad de productos ingresados de cada categoría y el total de importes.  """


categoria_a = "A"
categoria_b="B"
categoria_c="C"
a=0
b=0
c=0
importe_total=0
importe_a=0
importe_b=0
importe_c=0
cantidadTotal=0

for i in range (3):
    categoria = input("Ingresa categoria puede ser A,B o C: ")

    while categoria !="A" and categoria!="B" and categoria!="C":
        categoria = input("Ingresa categoria puede ser A,B o C: ")

    precio = int(input("Ingresa precio: "))
    while precio <0:
        precio = int(input("Ingresa precio: "))

    cantidadTotal+=1
    importe_total+=precio
    if categoria =="A":
        a+=1
    if categoria =="B":
        b+=1
    if categoria =="C":
        c+=1


print("Importe total:",importe_total)
print("cantidad a: ",a)
print("cantidad b: ",b)
print("cantidad c: ",c)





