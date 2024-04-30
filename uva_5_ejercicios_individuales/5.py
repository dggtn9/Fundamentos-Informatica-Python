"""El factorial de un número entero N mayor que cero se define como el producto de todos los enteros X
tales que 0 < X <= N. Desarrollar un programa para calcular el factorial de un número dado hasta ingresar -1.
 Deberán rechazarse las entradas inválidas (menores que 0). Al finalizar informar cuantas veces se calculó el factorial.
"""


cant=0
numero_dado=int(input("Ingrese numero"))
while numero_dado < 0 :
    numero_dado=int(input("Ingrese numero"))
while numero_dado!=-1:
    cant+=1
    factorial = 1
    for i in range(1,numero_dado):
           factorial=factorial*(i+1)
    print(factorial)
    numero_dado = int(input("Ingrese numero"))
print("Cantidad de veces que se calculó factorial ", cant)
