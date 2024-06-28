"""
Calcular la suma de los números de una lista.


"""
import random


def crear_lista(a,b):
    lista = []
    for i in range (5):
        valor = random.randint(a, b)
        lista.append(valor)
    return lista

def main():
    lista1=crear_lista(5,100)
    suma=0
    for i in range (len(lista1)):
        suma+=lista1[i]

    print(lista1)
    print(suma)

if __name__ == "__main__":
    main()