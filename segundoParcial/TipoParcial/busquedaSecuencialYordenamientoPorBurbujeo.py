
def metodoPorBurbujeo(lista):
    intercambios=True
    numPasada=len(lista)-1
    while numPasada>0 and intercambios:
        for i in range(numPasada):
            if lista[i]>lista[i+1]:
                intercambios=True
                temp=lista[i]
                lista[i]=lista[i+1]
                lista[i+1]=temp
        numPasada=numPasada-1

lista1=[125,856,4,10,23,9,784]
metodoPorBurbujeo(lista1)
print(lista1)

def buscarValorSecuencial(lista,nro):
        pos = -1
        i = 0
        while pos == -1 and i < len(lista):
            if lista[i] == nro:
                pos = i
            i += 1
        return pos

lista2=[125,856,4,10,23,9,784]
print(buscarValorSecuencial(lista2,856))



def maximo(lista):
    for i in range(len(lista)):
        if i == 0 or lista[i] > valMax:
            valMax = lista[i]
            posMax = i
    return posMax

lista3=[125,856,4,10,23,9,784]
print("posicion del valor maximo",maximo(lista3))

def minimo(lista):
    for i in range(len(lista)):
        if i == 0 or lista[i] < valMin:
            valMin = lista[i]
            posMin = i
    return posMin

lista3=[125,856,4,10,23,9,784]
print("posicion del valor minimo",minimo(lista3))