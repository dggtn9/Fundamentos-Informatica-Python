"""Ejercicio 3: Desarrollar un programa que solicite un número de mes (por ejemplo 4) y
escriba el nombre del mes en letras ("abril"). Verificar que el mes sea válido y
mostrar un mensaje de error en caso de que no lo sea."""
print("Ejercicio 3:")
mes=int(input("Ingresa un mes"))
if mes <=12:
    if mes == 1:
        print("Enero")
    if mes == 2:
        print("Febrero")
    if mes == 3:
        print("Marzo")
    if mes == 4:
        print("Abril")
    if mes == 5:
        print("Mayo")
    if mes == 6:
        print("Junio")
    if mes == 7:
        print("Julio")
    if mes == 8:
        print("Agosto")
    if mes == 9:
        print("Septiembre")
    if mes == 10:
        print("Octubre")
    if mes == 11:
        print("Noviembre")
    if mes == 12:
        print("Diciembre")
else:
    print("ese numero no corresponde a un mes del anio")