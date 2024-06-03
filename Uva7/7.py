"""
Determinar si una lista es capicúa.

"""
import random
def crearlista():
    lista=[]
    for i in range(5):
        valor = random.randint(0, 9)
        lista.append(valor)
    return lista

lista1 = crearlista()
print(lista1)
largo=len(lista1)
iteracion=largo//2

posible_capicua=True
for i in range (0,iteracion):
    der=i
    izq= largo - (i + 1)
    posible_capicua= posible_capicua and lista1[der]==lista1[izq]
if posible_capicua==True:
    print("Es capicua")
else:
    print("No es capicua")



