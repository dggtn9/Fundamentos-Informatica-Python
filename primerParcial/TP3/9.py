"""Ejercicio 9: Diseñar un programa que calcule y muestre el sueldo neto de un empleado en
base a su sueldo básico y su antigüedad en años. Si es soltero se le incrementa
el sueldo en 5% del salario bruto por cada año de antigüedad, mientras que si es
casado se le incrementa el sueldo en 7% del bruto por cada año de antigüedad.
También se le realizan los siguientes descuentos: Jubilación: 11%, Obra Social:
3%, Sindicato: 3%
Como datos de entrada se ingresa por teclado el sueldo básico, antigüedad
y estado civil ('soltero' si es soltero o 'casado' si es casado). Se debe informar:
(reemplazar los 9 por los valores que correspondan)
Estado Civil: Soltero/Casado
Sueldo básico Antigüedad Descuentos Importe
$ 999.99 99 años + 999.99
Jubilación - 999,99
Obra Social - 999,99
Sindicato - 999,99
------------
Sueldo Neto 999,99 """

sueldo_basico=float(input("Ingrese sueldo basico"))
antiguedad_en_anios=int(input("Ingrese antiguedad en anios"))
estado_civil=input('Ingrese la palabra "soltero" si es soltero,de otra manera escriba "casado" ')

jubilacion= (0.11*sueldo_basico)
obra_social=(0.03*sueldo_basico)
sindicato= (0.03*sueldo_basico)
incremento_porcentual = 0.0

if estado_civil== "soltero" :
    incremento_porcentual = 0.05
    print("Estado Civil: Soltero")

else:
    incremento_porcentual = 0.07
    print("Estado civil casado")

sueldo_bruto = ((sueldo_basico*incremento_porcentual)*antiguedad_en_anios)+sueldo_basico
sueldo_neto = sueldo_bruto - jubilacion - obra_social - sindicato
print("Su sueldo es", sueldo_neto,"usd")
print("Sueldo básico es",sueldo_basico)
print("Antigüedad es",antiguedad_en_anios," anios")
print("Descuentos:")
print("Jubilación -",jubilacion)
print("Obra Social -", obra_social)
print("Sindicato - ",sindicato)
print("Su sueldo es",sueldo_neto,"usd")