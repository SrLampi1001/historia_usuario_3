import csv
import os
def guardar_csv(inventario, ruta, incluir_header=True):
    """
    Formato de archivo: CSV con separador coma y encabezado: nombre, precio, cantidad

    Valida que el inventario no esté vacío antes de guardar (mensaje si lo está)

    Manejo de errores con try/except
        Problema de permisos/escritura -> informar sin cerrar el programa
    Impresión de mensaje: #si todo va bien
        "Inventario guardado {ruta}"
    """

    if len(inventario)==0:
        print("El inventario que está intentando guardar está vacío")
        return
    with open(ruta, "w", newline="") as archivo:
        fieldnames = ["Nombre", "Precio", "Cantidad"]
        writer = csv.DictWriter(archivo, fieldnames=fieldnames)
        if incluir_header:
            writer.writeheader() 
        writer.writerows(inventario)
    

def cargar_csv(ruta):
    """
    Retorna lista de productos con la misma estructura de inventario

    El archivo debe tener encabezado: nombre, precio, cantidad
    Cada fila debe tener exactamente 3 columnas
    Precio debe convertirse a Floar, cantidad a Int, no negativos

    Si hay filas inválidas, son omitidas, se acumula un contador de errores que se informa al final
    Manejo de FileNotFoundError, UnicodeDecodeError, ValueError y errores genéricos con mensajes claros

    al cargar:
        ¿sobrescribir inventario actual? S/N:
        S - reemplaza inventario por lo cargado
        N - fuciona por nombre:
            Sí un nombre (producto) existe, sobrescribe con el precio del csv cargado, y suma la cantidad de csv cargado al inventario
        
    Al final, refresca salida/menú y muestra resumen: productos cargados, filas inválidas, acción (reemplazo, fusión)
    """
    try:
        with open(ruta, "r", newline="") as archivo:
            fieldnames = ["Nombre", "Precio", "Cantidad"]
            reader = csv.DictReader(archivo, fieldnames=fieldnames)
            for row in reader:
                print(row)
    except Exception as e:
        print(f"Hubo un error al intentar cargar el csv: {e}")

def crear_ruta(ruta_final):
    """
        Crea la ruta seleccionada por el usuario para crear el archivo .csv
        usa os.makedirs()
    """
    ruta_directorio = os.path.dirname(ruta_final) #Extrae el directorio de una ruta -> si termina en inventario.csv, lo quita
    try:
        os.makedirs(ruta_directorio, exist_ok=True) #Crea los directorios
        print("Ruta creada con éxito.")
    except Exception as e:
        print(f"Error al crear la ruta: {e}")

    