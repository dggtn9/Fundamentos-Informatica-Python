"""Ingresar por teclado la cantidad de términos a generar de la siguiente serie:

 1 7 19 43 91 187 379 763 1531 3067 6139
El primer término es el 1 y cada término se genera como el doble del término anterior más 5.
Mostrar la serie por pantalla e informar la suma de los términos generados.
"""



terminos=int(input("Ingresa terminos"))
valor=1
sumatoria=0
for i in range (terminos):
    if i >0:
        valor = (valor * 2) + 5
    sumatoria += valor
    print(valor)
print("Sumatoria total es: ",sumatoria)

