
def burbujeo(lista):
    intercambios=True
    numPasadas=len(lista)-1
    while intercambios and numPasadas>0:
        intercambios=False
        for i in range (numPasadas):
            if lista[i]>lista[i+1]:
                intercambios=True
                temp=lista[i]
                lista[i]=lista[i+1]
                lista[i+1]=temp
        numPasadas=numPasadas-1

lista1=[8555,8,97,23]
burbujeo(lista1)
print(lista1)

def busquedaSecuencial(lista,valor):
    pos=-1
    i=0
    while pos==-1 and i <len(lista):
        if lista[i]==valor:
            pos=i
        i+=1
    return pos

print(busquedaSecuencial(lista1,8))

def maximo(lista):
    i=0
    valMax=i
    for i in range (len(lista)):
        if lista[i]>valMax:
            valMax=lista[i]
        i+=1
    return valMax

print(maximo(lista1))