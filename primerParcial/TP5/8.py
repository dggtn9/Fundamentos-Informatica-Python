"""Ejercicio 8:
Una empresa cuenta con N empleados, divididos en tres categorías (1, 2 y 3).
Por cada empleado se lee su legajo, categoría y salario. Se solicita elaborar un
informe que contenga:

· Importe total de salarios pagados por la empresa.
· Cantidad de empleados que ganan más de $200000.
· Cantidad de empleados que ganan menos de $50000, cuya categoría sea
3.
· Legajo del empleado que más gana.
· Sueldo más bajo.
· Importe total de sueldos por cada categoría.
· Salario promedio"""
cantidadEmpleados = int(input("Ingrese la cantidad de empleados: "))
gananMasDe200000 = 0
gananMenosDe50000cc = 0
sueldoMasBajo = 0
promedioSueldos = 0
sueldoTotalCategoriaa = 0
sueldoTotalCategoriab = 0
sueldoTotalCategoriac = 0
sueldoTotal = 0
legajoMasGana = 0

for i in range(cantidadEmpleados):
      legajo = int(input("Ingrese el legajo del empleado: "))
      categoria = input("Ingrese la categoria del empleado: ")
      salario = int(input("Ingrese el salario del empleado: "))
      sueldoTotal += salario

      if salario > 200000:
            gananMasDe200000 += 1
      if salario < 50000 and categoria == "C":
            gananMenosDe50000cc += 1
      if i == 0:
            sueldoMasBajo = salario
            legajoMasGana = legajo
      else:
            if salario < sueldoMasBajo:
                  sueldoMasBajo = salario
            if salario > sueldoMasBajo:
                  legajoMasGana = legajo
      if categoria == "A":
            sueldoTotalCategoriaa += salario
      if categoria == "B":
            sueldoTotalCategoriab += salario
      if categoria == "C":
            sueldoTotalCategoriac += salario

promedioSueldos = sueldoTotal / cantidadEmpleados

print("El importe total de salarios pagados por la empresa es: ", sueldoTotal)
print("La cantidad de empleados que ganan mas de $200000 es: ", gananMasDe200000)
print("La cantidad de empleados que ganan menos de $50000 y cuya categoria es 3 es: ", gananMenosDe50000cc)
print("El legajo del empleado que mas gana es: ", legajoMasGana)
print("El sueldo mas bajo es: ", sueldoMasBajo)
print("El importe total de sueldos por cada categoria es: ")
print("Categoria 1: ", sueldoTotalCategoriaa)
print("Categoria 2: ", sueldoTotalCategoriab)
print("Categoria 3: ", sueldoTotalCategoriac)
print("El salario promedio es: ", promedioSueldos)


