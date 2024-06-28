"""Se realizó un concurso de tiro al blanco.
Existen 5 participantes y cada uno de ellos efectúa 3 disparos, registrándose las coordenadas X-Y de cada disparo.
Determinar:
a. Cuantos disparos se efectuaron en cada cuadrante por cada participante
b. Cuantos disparos se efectuaron en total en el centro.
NOTA: no considere disparos sobre los ejes"""



centro=0
for i in range (5):
    cuadrante_positivo=0
    cuadrante_x_negativo_e_y_positivo=0
    cuadrante_x_positivo_e_y_negativo=0
    cuadrante_negativo=0
    for disparo in range (3):
        x1=int(input("valor disparo en x"))
        y1=int(input("valor disparo en y"))
        if (x1==0 and y1 ==0):
            centro+=1
        elif (x1>0 and y1>0):
            cuadrante_positivo+=1
        elif (x1<0 and y1>0):
            cuadrante_x_negativo_e_y_positivo+=1
        elif (x1>0 and y1<0):
            cuadrante_x_positivo_e_y_negativo+=1
        elif (x1<0 and y1<0):
            cuadrante_negativo+=1
    print("En cuadrante positivo:",cuadrante_positivo)
    print("en cuadrante x negativo,y positivo: ",cuadrante_x_negativo_e_y_positivo)
    print("en cuadrante x e y negativo: ",cuadrante_x_positivo_e_y_negativo)
    print("en cuadrante negativo: ",cuadrante_negativo)
    print("en cuadrante x positivo e y negativo: ",cuadrante_x_positivo_e_y_negativo)
print("Cantidad de disparos en centro: ",centro)