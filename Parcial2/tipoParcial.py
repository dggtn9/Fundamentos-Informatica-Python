import random

def main():
    def existe_en_lista(lista, valor_buscado):
        encontrado = False
        indice = 0

        while encontrado == False and indice < len(lista):
            aux = lista[indice]
            if aux == valor_buscado:
                encontrado = True
            indice+=1

        return encontrado

    def alta_de_productos(codigo_por_producto, stock_por_producto):
        for i in range(5):
            # Obtener codigo de producto
            codigo = random.randint(100, 999)
            while existe_en_lista(codigo_por_producto, codigo) == True:
                codigo = random.randint(100, 999)

            #Obtener stock
            stock = random.randint(0, 100)

            codigo_por_producto.append(codigo)
            stock_por_producto.append(stock)

    def obtener_posicion(lista, valor):
        posicion = -1
        indice = 0
        while posicion == -1 and indice < len(lista):
            if lista[indice] == valor:
                posicion = indice
            indice+=1

        return posicion

    def mostrar_listado_de_productos_vendidos(productos, ventas):
        print("PRODUCTO", " ", "CANTIDAD VENDIDA")
        for i in range(len(productos)):
            print(productos[i], " ", ventas[i])

    def mostrar_stock_actual(productos, stock_por_producto):
        print("PRODUCTO", " ", "STOCK")
        for i in range(len(productos)):
            print(productos[i], " ", stock_por_producto[i])

    def mostrar_productos_no_vendidos(productos, cantidad_vendida):
        print("Productos no vendidos:")
        for i in range(len(productos)):
            if cantidad_vendida[i] == 0:
                print(productos[i])

    def mostrar_almacenes_con_venta_minima(ventas_por_almacen):
        minimo = ventas_por_almacen[0]
        for i in range(1, len(ventas_por_almacen)):
            if minimo > ventas_por_almacen[i]:
                minimo = ventas_por_almacen[i]

        print("Almacenes con venta minima")
        for i in range(len(ventas_por_almacen)):
            if ventas_por_almacen[i] == minimo:
                print ("Almacen: ", i + 1)

    def validar_por_rangos(valor_minimo, valor_maximo, texto = ""):
        valor = int(input(texto))
        while valor < valor_minimo or valor > valor_maximo:
            valor = int(input(texto))
        return valor

    def validar_que_supere_valor(valor_minimo, texto):
        valor = int(input(texto))
        while valor < valor_minimo:
            valor = int(input(texto))
        return valor

    codigo_por_producto = []
    stock_por_producto = []
    cantidad_vendida_por_producto = [0] * 5 # Recuerda que es mas el formato
    ventas_por_almacen = [0] * 4

    # Primero doy de alta los productos
    alta_de_productos(codigo_por_producto, stock_por_producto)
    for i in range(5):
        print(codigo_por_producto[i], stock_por_producto[i])

    nro_almacen = validar_por_rangos(0, 4, "Ingresar numero de almacen (entre 1 y 4) o 0 para terminar")

    # PRINCIPAL
    while nro_almacen != 0:

        codigo_de_producto = validar_por_rangos(100, 999, "Ingrese el codigo de producto (3 cifras)")
        while existe_en_lista(codigo_por_producto, codigo_de_producto) == False:
            print("Producto inexistente, ingrese nuevamente:")
            codigo_de_producto = validar_por_rangos(100, 999, "Ingrese el codigo de producto (3 cifras)")

        cantidad_vendida = validar_que_supere_valor(0, "Ingresar cantidad vendida (valor mayor a 0)")

        # Comparar si la cantidad ingresa se puede vender (si hay stock disponible)
        indice_producto = obtener_posicion(codigo_por_producto, codigo_de_producto)
        stock_actual = stock_por_producto[indice_producto]

        if stock_actual >= cantidad_vendida:
            stock_por_producto[indice_producto] = stock_actual - cantidad_vendida
            cantidad_vendida_por_producto[indice_producto] += cantidad_vendida
            ventas_por_almacen[nro_almacen - 1] += cantidad_vendida
        else:
            print("ERROR: No hay suficiente stock del producto: ", codigo_de_producto)

        nro_almacen = validar_por_rangos(0, 4, "Ingresar numero de almacen (entre 1 y 4) o 0 para terminar")

    # REPORTES
    mostrar_listado_de_productos_vendidos(codigo_por_producto, cantidad_vendida_por_producto)
    mostrar_stock_actual(codigo_por_producto, stock_por_producto)
    mostrar_productos_no_vendidos(codigo_por_producto, cantidad_vendida_por_producto)
    mostrar_almacenes_con_venta_minima(ventas_por_almacen)

if __name__=="__main__":
    main()