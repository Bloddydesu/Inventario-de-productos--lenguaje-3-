from logica import (
    cargar_datos,
    registrar_producto,
    listar_productos,
    buscar_producto,
    modificar_producto,
    eliminar_producto,
    generar_reporte
)

def main():
    # Cargamos los datos del JSON al iniciar el programa
    inventario = cargar_datos()
    
    while True:
        print("\n==================================")
        print("   SISTEMA DE GESTIÓN DE INVENTARIO")
        print("==================================")
        print("1. Registrar producto")
        print("2. Listar productos")
        print("3. Buscar producto")
        print("4. Modificar producto")
        print("5. Eliminar producto")
        print("6. Ver reporte (Valor total y bajo stock)")
        print("7. Salir")
        
        opcion = input("Seleccione una opción (1-7): ").strip()
        
        if opcion == "1":
            registrar_producto(inventario)
        elif opcion == "2":
            listar_productos(inventario)
        elif opcion == "3":
            buscar_producto(inventario)
        elif opcion == "4":
            modificar_producto(inventario)
        elif opcion == "5":
            eliminar_producto(inventario)
        elif opcion == "6":
            generar_reporte(inventario)
        elif opcion == "7":
            print("\nSaliendo del sistema. ¡Hasta luego!")
            break
        else:
            print("\nError: Opción inválida. Ingrese un número del 1 al 7.")

if __name__ == "__main__":
    main()