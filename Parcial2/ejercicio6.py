"""
#Desarrollar una función que reciba la lista como parámetro y devuelva una nueva
#lista con los mismos elementos de la primera, pero en orden inverso. Por
#ejemplo, si la función recibe [5, 7, 1] debe devolver [1, 7, 5]"""

def invertirLista(lista):
    listaInversa=[]
    for i in range(len(lista),0,-1):
        listaInversa.append(lista[i-1])
    return listaInversa

#Programa Principal

listaPepe=[7,7,8,9,4,5,6,7]

print("Apariciones",contarApariciones(listaPepe,7))

listita=[1,4,4,2]

print("Es capicua?",determinarCapicua(listita))

min= int(input("Ingrese el valor desde que desea ingresar numeros\n"))
max= int(input("Ingrese el valor hasta que desea ingresar numeros\n"))

lista=cargarNumerosEntreExtremos(min,max)
print(lista)
print("La suma de los valores de la lista es: ",calcularSuma(lista))
