"""
Desarrollar un programa para cargar 5 notas. Validar que se encuentren entre 1 y 10. Al finalizar, mostrar el promedio de las notas. """
notas=0
total_notas=0
for i in range (5):
    nota = int(input("Ingresa nota"))
    if nota >=1 and nota <=10:
        notas += nota
        total_notas+=1
    else:
        nota = int(input("Ingresa nota"))

promedio = notas/total_notas

print("promedio de las notas es ",promedio)
print(total_notas)
