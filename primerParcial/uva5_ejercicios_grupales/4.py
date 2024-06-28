"""Leer números que representan edades de un grupo de personas, finalizando la lectura cuando se ingrese el
número 999.
 Imprimir cuántos son menores de 18 años, cuántos tienen 18 años o más y la cantidad de edades ingresadas. 
 Descartar valores que no representan una edad válida (se considera válido una edad entre 0 y 100). 
 Utilizar el depurador de Thonny para visualizar las variables y detectar posibles errores en tiempo de ejecución.  """

cantidad_edades_ingresadas=0
cantidad_menores=0
cantidad_mayores=0
edad=int(input("Ingresa edad"))
while edad<0 or edad>100:
    edad=int(input("Ingresa edad"))
while edad !=999:
    cantidad_edades_ingresadas+=1
    if edad <18:
        cantidad_menores+=1
    else:
        cantidad_mayores+=1
    edad=int(input("Ingresa edad"))
    while edad < 0 or edad > 100 and edad!=999:
        edad = int(input("Ingresa edad"))

print("menores de 18 años: ",cantidad_menores)
print("mayores de 18 años: ",cantidad_mayores)
print("cantidad de edades ingresadas: ",cantidad_edades_ingresadas)