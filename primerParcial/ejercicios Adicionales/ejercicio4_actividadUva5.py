"""Leer números que representan edades de un grupo de personas, finalizando la lectura cuando se ingrese el número 999.
Imprimir cuántos son menores de 18 años, cuántos tienen 18 años o más y el promedio de edad de ambos grupos.
Descartar valores que no representan una edad válida. (Se considera válido una edad entre 0 y 100)."""


cantidad_total=0
cantidad_menores=0
cantidad_mayores=0
suma_edad_menores=0
suma_edad_mayores=0

n =int(input("Ingresa edad"))
while n!=999:
    if n>=0 and n<=100:
       cantidad_total+=1
       if n<18:
            cantidad_menores+=1
            suma_edad_menores=suma_edad_menores+n
       else:
            cantidad_mayores+=1
            suma_edad_mayores=suma_edad_mayores+n
    else:
        print("Edad erronea")
    n = int(input("Ingresa edad"))
suma_total=suma_edad_menores+suma_edad_mayores
promedio_menores=suma_edad_menores/suma_total
promedio_mayores=suma_edad_mayores/suma_total

print("Cantidad mayores: ",cantidad_mayores)
print("Cantidad menores: ",cantidad_menores)
print("Promedio mayores: ",promedio_mayores)
print("Promedio menores: ",promedio_menores)