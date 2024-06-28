"""
Ejercicio 7: Calcular y devolver el Máximo Común Divisor de dos enteros no negativos, basándose
en las siguientes fórmulas matemáticas:
· MCD(X,X) = X
· MCD(X,Y) = MCD(Y, X)
· Si X > Y => MCD(X, Y) = MCD(X-Y, Y).
Ejemplo: MCD(40, 15) devuelve 5.

"""
numero_menor=0

def calcular(a,b):

    if a>b:
        numero_menor=b
    elif a<b:
        numero_menor=a
    else:
        numero_menor=b
    maximo=0
    for i in range (1,numero_menor+1):
        if a%i==0 and b%i==0 and i > maximo:
            maximo=i
    return maximo


r=calcular(40,20)
d= calcular(40-20,20)

print(r)
print(d)


