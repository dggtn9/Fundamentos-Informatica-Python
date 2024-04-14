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
legajo=int(input("Ingrese su numero de legajo"))
categoria=int(input("Ingrese si es categoria 1,2 o 3"))
salario=int(input("Ingrese su salario"))
empleado=0
importe=0
while legajo and categoria and salario >=1:
      importe+=salario
      if salario>200000 :
          empleados_ganan_mas_de_doscientosmil+=1
      elif salario<50000 and categoria ==3:
           menos_cincuentamil_categoria_tres+=1

      legajo_empleado_mas_gana
      sueldo_mas_bajo
      sueldo_por_categoria1
      sueldo_por_categoria2
      sueldo_por_categoria3
      salario_promedio =salario/importe

print("Importe total de salarios pagados por la empresa:",importe)
print("Cantidad de empleados que ganan más de $200000.", empleados_ganan_mas_de_doscientosmil)
print(" Cantidad de empleados que ganan menos de $50000, cuya categoría sea 3.", menos_cincuentamil_categoria_tres)
print("Legajo del empleado que más gana",legajo_empleado_mas_gana)
print("Sueldo más bajo",sueldo_mas_bajo)
print("Importe total de sueldos por cada categoría 1",sueldo_por_categoria1)
print("Importe total de sueldos por cada categoría 2",sueldo_por_categoria2)
print("Importe total de sueldos por cada categoría 3",sueldo_por_categoria3)
print("Salario promedio",salario_promedio)


