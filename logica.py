import json
import os

ARCHIVO_DATOS = "datos/inventario.json"

def cargar_datos():
    """Carga el inventario desde el archivo JSON. Si no existe, retorna una lista vacía."""
    if not os.path.exists("datos"):
        os.makedirs("datos")
    if not os.path.exists(ARCHIVO_DATOS):
        return []
    try:
        with open(ARCHIVO_DATOS, "r", encoding="utf-8") as archivo:
            return json.load(archivo)
    except Exception:
        return []

def guardar_datos(inventario):
    """Guarda el inventario actual en el archivo JSON de forma permanente."""
    if not os.path.exists("datos"):
        os.makedirs("datos")
    with open(ARCHIVO_DATOS, "w", encoding="utf-8") as archivo:
        json.dump(inventario, archivo, indent=4, ensure_ascii=False)

def registrar_producto(inventario):
    print("\n--- Registrar Nuevo Producto ---")
    nombre = input("Ingrese el nombre del producto: ").strip()
    if not nombre:
        print("Error: El nombre no puede estar vacío.")
        return

    # Validar que no exista un producto con el mismo nombre
    for p in inventario:
        if p["nombre"].lower() == nombre.lower():
            print("Error: Ya existe un producto con ese nombre.")
            return

    categoria = input("Ingrese la categoría: ").strip()
    if not categoria:
        print("Error: La categoría no puede estar vacía.")
        return

    # Uso de try/except para validar que el precio sea un número válido y no negativo
    try:
        precio = float(input("Ingrese el precio: "))
        if precio < 0:
            print("Error: El precio no puede ser negativo.")
            return
    except ValueError:
        print("Error: Debe ingresar un valor numérico válido para el precio.")
        return

    # Uso de try/except para validar que el stock sea un entero válido y no negativo
    try:
        stock = int(input("Ingrese el stock (cantidad): "))
        if stock < 0:
            print("Error: El stock no puede ser negativo.")
            return
    except ValueError:
        print("Error: Debe ingresar un número entero válido para el stock.")
        return

    nuevo_producto = {
        "nombre": nombre,
        "categoria": categoria,
        "precio": precio,
        "stock": stock
    }
    
    inventario.append(nuevo_producto)
    guardar_datos(inventario)
    print("¡Producto registrado y guardado con éxito!")

def listar_productos(inventario):
    print("\n--- Lista de Productos ---")
    if not inventario:
        print("No hay productos registrados en el inventario.")
        return
    for i, p in enumerate(inventario, 1):
        print(f"{i}. Nombre: {p['nombre']} | Categoría: {p['categoria']} | Precio: ${p['precio']:.2f} | Stock: {p['stock']}")

def buscar_producto(inventario):
    print("\n--- Buscar Producto ---")
    nombre_buscar = input("Ingrese el nombre del producto a buscar: ").strip().lower()
    encontrados = [p for p in inventario if nombre_buscar in p['nombre'].lower()]
    
    if not encontrados:
        print("No se encontraron productos con ese nombre.")
        return
    
    print(f"\nResultados encontrados ({len(encontrados)}):")
    for p in encontrados:
        print(f"- Nombre: {p['nombre']} | Categoría: {p['categoria']} | Precio: ${p['precio']:.2f} | Stock: {p['stock']}")

def modificar_producto(inventario):
    print("\n--- Modificar Producto ---")
    nombre_buscar = input("Ingrese el nombre exacto del producto a modificar: ").strip().lower()
    producto = None
    for p in inventario:
        if p['nombre'].lower() == nombre_buscar:
            producto = p
            break
            
    if not producto:
        print("Error: Producto no encontrado.")
        return
    
    print(f"Producto actual -> Precio: ${producto['precio']}, Stock: {producto['stock']}")
    opcion = input("¿Qué desea modificar? (1: Precio, 2: Stock, 3: Ambos): ").strip()
    
    if opcion in ["1", "3"]:
        try:
            nuevo_precio = float(input("Ingrese el nuevo precio: "))
            if nuevo_precio < 0:
                print("Error: El precio no puede ser negativo.")
                return
            producto['precio'] = nuevo_precio
        except ValueError:
            print("Error: Valor numérico inválido.")
            return

    if opcion in ["2", "3"]:
        try:
            nuevo_stock = int(input("Ingrese el nuevo stock: "))
            if nuevo_stock < 0:
                print("Error: El stock no puede ser negativo.")
                return
            producto['stock'] = nuevo_stock
        except ValueError:
            print("Error: Valor entero inválido.")
            return
            
    if opcion not in ["1", "2", "3"]:
        print("Opción inválida.")
        return

    guardar_datos(inventario)
    print("¡Producto modificado con éxito!")

def eliminar_producto(inventario):
    print("\n--- Eliminar Producto ---")
    nombre_buscar = input("Ingrese el nombre exacto del producto a eliminar: ").strip().lower()
    for i, p in enumerate(inventario):
        if p['nombre'].lower() == nombre_buscar:
            confirmacion = input(f"¿Está seguro de eliminar '{p['nombre']}'? (s/n): ").strip().lower()
            if confirmacion == 's':
                inventario.pop(i)
                guardar_datos(inventario)
                print("¡Producto eliminado con éxito!")
            else:
                print("Operación cancelada.")
            return
    print("Error: Producto no encontrado.")

def generar_reporte(inventario):
    print("\n--- Reporte del Inventario ---")
    if not inventario:
        print("No hay datos para generar reportes.")
        return
    
    # Cálculo del valor total (precio * stock de cada producto sumado)
    valor_total = sum(p['precio'] * p['stock'] for p in inventario)
    print(f"Valor total monetario del inventario: ${valor_total:.2f}")
    
    # Productos con poco stock (menor a 5 unidades)
    print("\nProductos con stock crítico (Menos de 5 unidades):")
    escasos = [p for p in inventario if p['stock'] < 5]
    if not escasos:
        print("¡Excelente! No hay productos con stock crítico.")
    else:
        for p in escasos:
            print(f"- {p['nombre']} (Stock actual: {p['stock']})")
# Este es una prueba del commit
