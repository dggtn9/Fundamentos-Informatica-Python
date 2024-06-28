"""
#Ejercicio 3: Determinar si la lista es capicúa (palíndromo). Una lista capicúa se lee de igual
#modo de izquierda a derecha y de derecha a izquierda. Por ejemplo, [2, 7, 7, 2]
#es capicúa, mientras que [2, 7, 5, 2] no lo es."""

def determinarCapicua(lista):
    listaInversa=[]
    for i in range(len(lista),0,-1):
        listaInversa.append(lista[i-1])

    for i in range(len(lista)):
        if lista[i]!=listaInversa[i]:
            return False
    return True



