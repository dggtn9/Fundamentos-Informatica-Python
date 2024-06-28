"""
#Ejercicio 2: Calcular la suma de los números de la lista."""

def calcularSuma(lista):
    total=0
    for i in range(len(lista)):
        total+=lista[i]
    return total
