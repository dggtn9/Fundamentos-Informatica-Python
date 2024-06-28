


lista1=[1000000,83,45,1,212000,123,4,56,89]


def burbujeo(lista):
    intercambios=True
    numPasada=len(lista)-1
    while numPasada>0 and intercambios:
        intercambios=False
        for i in range (numPasada):
            if lista[i]>lista[i+1]:
                intercambios=Tru
                temp=lista[i]
                lista[i]=lista[i+1]
                lista[i+1]=temp
        numPasada=numPasada-1


burbujeo(lista1)
print(lista1)

