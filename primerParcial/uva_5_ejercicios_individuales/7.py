"""Una empresa cuenta con N empleados, divididos en tres categorías A, B y C.
Por cada empleado se lee su legajo, categoría y salario. Se solicita elaborar un informe que contenga:


Importe total de salarios pagados por la empresa.
Cantidad de empleados que ganan más de $20000.
Cantidad de empleados que ganan menos de $5000, cuya categoría sea “C”.
Legajo del empleado que más gana.
Sueldo más bajo.
Importe total de sueldos por cada categoría.
Salario promedio. """

salarios_totales=0
cant=0
cant_menor5=0
cant_total=0
salarios_a=0
salarios_b=0
salarios_c=0
legajo_mas_gana=0
sueldo_mas_bajo=0
salario_mas_alto=0
numero_empleados=int(input("Numero de empleados"))
for i in range (numero_empleados):
    legajo = int(input("Ingrese legajo"))
    categoria = input("Ingrese categoria: A,B,C")
    salario = int(input("ingrese sueldo"))
    cant_total+=1
    if i ==0:
       legajo_mas_gana =legajo
       salario_mas_alto =salario
       sueldo_mas_bajo = salario
    else:
        if salario>salario_mas_alto:
            salario_mas_alto = salario
            legajo_mas_gana = legajo
        if sueldo_mas_bajo>salario:
            sueldo_mas_bajo=salario

    if salario>20000:
        cant+=1
    if salario<5000 and categoria=='C':
        cant_menor5+=1
    if categoria =='C':
        salarios_c+=salario
    if categoria == 'B':
        salarios_b+=salario
    if categoria == 'A':
        salarios_a+=salario

promedio=(salarios_a+salarios_b+salarios_c)/cant_total
print("Importe total de salarios pagados por la empresa.",salarios_totales)
print("Cantidad de empleados que ganan más de $20000: ",cant)
print("Cantidad de empleados que ganan menos de $5000, cuya categoría sea 'C':",cant_menor5)
print("Legajo mas gana",legajo_mas_gana)
print("sueldo mas bajo",sueldo_mas_bajo)
print("Importe total de sueldos por cada categoría:A:",salarios_a,"B",salarios_b,"C",salarios_c)
print("Salario promedio: ",promedio)