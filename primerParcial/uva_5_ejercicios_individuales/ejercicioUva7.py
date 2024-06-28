"""
Desarrollar un algoritmo que permita crear al azar 5 números pertenecientes a la lista A y otros 5 números pertenecientes a la lista B.
 Crear una lista C, donde cada posición es el resultado de la suma del número en la misma posición en la lista A con el número en la misma
 posición en la lista B. Ejemplo: Se crea A = [1, 2, 3, 4, 5] y B = [4, 7, 1, 3, 6] → C = [5, 9, 4, 7, 11]

"""

import random
def main():
    c = []
    def generar_lista(len):
        lista = []
        for i in range(len):
            lista.append(random.randint(0,100))
        return lista


    a = generar_lista(5)
    b = generar_lista(5)

    for i in range(5):
        c.append(a[i]+b[i])
    print("A = ",a,"")
    print("A = ",b,"")
    print("A = ",c,"")

if __name__=="__main__":
    main()


