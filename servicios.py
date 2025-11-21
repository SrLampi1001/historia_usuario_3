def agregar_producto(inventario):
    """
    Agregra un producto al inventario
    """
    pass

def mostrar_inventario(inventario):
    """
    Muestra el inventario
    """
    print("inventario")
    pass

def buscar_producto(inventario, nombre):
    """
    Busca un producto en el inventario
    """
    pass

def actualizar_producto(inventario, nombre, nuevo_precio = None, nueva_cantidad = None):
    """
    Actualiza el precio y/o cantidad del producto seleccionado en el inventario
    """
    pass

def eliminar_producto(inventario, nombre):
    """
    Elimina un producto del inventario
    """
    pass

def calcular_estadisticas(inventario):
    """
    Calcula las estadísticas del inventario:

    unidades_totales = suma de cantidad
    valor_total = suma de precio * cantidad
    producto_mas_caro (nombre y precio)
    producto_mayor_stock (nombre y cantidad)

    (Opcional) Usa una lambda para calcular el subtotal de cada producto:

    subtotal = (lambda p: p["precio"] * p["cantidad"]) (Funciones anidadas)
    """
    pass
    #return elm1, elm2