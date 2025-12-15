from utils.helper import *                                  #traigo todas las funciones de helper
from utils import db_manager    
import sys                                                  #para salir del programa
from prettytable import PrettyTable                         #agrego este modulo para formatear la tabla


def mostrar_tabla(productos):                                  
    if not productos:
        print("No hay productos para mostrar")
        return

    tabla = PrettyTable()
    tabla.field_names = ["ID", "NOMBRE", "CATEGORIA", "PRECIO", "STOCK"]

    for prod in productos:
        tabla.add_row([
            prod[0],
            prod[1][:18],
            prod[5][:13],
            f"${float(prod[4]):.2f}",
            prod[3]
        ])

    print(tabla)
    
def menu_registracion():
    imprimir_titulo("Registrar nuevo item")
    nombre = validar_input_string("Ingresa el nombre del item ")
    descripcion = validar_input_string("Descripcion producto ")
    cantidad = validar_input_int("Stock inicial ")
    precio = validar_input_float("Precio unitario ")
    categoria = validar_input_string("Ingresar categorioa ")

    if db_manager.registrar_producto(nombre,descripcion,cantidad,precio,categoria):         #la funcion registrar_producto me devuelve un True o False por eso puedo hacer esto
        imprimir_exito("Registro Exitoso.")                                             

def menu_mostrar():
    imprimir_titulo("Listado de productos")
    productos = db_manager.obtener_producto()
    mostrar_tabla(productos)                                             #muestra la tabla de productos

def menu_actualizar():
    imprimir_titulo("Actualizar producto")
    menu_mostrar()                                              #para ver que producto vamos a actualizar
    id_prod = validar_input_int("Ingrese el id del item a modificar")
    producto_actual = db_manager.buscar_producto_id(id_prod)
    if not producto_actual:
        imprimir_error("Item no encontrado.")
        return
    print(f"Edit:{producto_actual[1]}")
    
    nuevo_nombre = input(f"Nombre actual \"{producto_actual[1]}\", Nuevo: ").strip() or producto_actual[1]
    
    nuevo_descripcion = input(f"Descripcion actual \"{producto_actual[2]}\", Nuevo: ").strip() or producto_actual[2]
        
    cantidad_str = input(f"Cantidad actual \"{producto_actual[3]}\", Nuevo: ").strip()
    nuevo_cantidad = int(cantidad_str) if cantidad_str.isdigit() else producto_actual[3]
    
    precio_str = input(f"Precio actual \"{producto_actual[4]}\", Nuevo: ").strip()
    nuevo_precio = float(precio_str) if precio_str else producto_actual[4]
    
    nuevo_categoria = input(f"Categoria actual \"{producto_actual[5]}\", Nuevo: ").strip() or producto_actual[5]

    if db_manager.actualizar_producto(id_prod,nuevo_nombre,nuevo_descripcion,nuevo_cantidad,nuevo_precio,nuevo_categoria):
        imprimir_exito("\n Producto Actualizado.")
    else:
        imprimir_error("\n Error al actualizar")

def menu_eliminar():
    imprimir_titulo("Eliminar Producto")
    menu_mostrar()                                                      #para ver que producto vamos a eliminar

    id_prod = validar_input_int("ID del producto a eliminar")
    
    confirm = input(f"¿Seguro que desea eliminar el ID {id_prod}? (s/n): ").lower()
    if confirm == 's':                                             
        if db_manager.eliminar_productos(id_prod):                        #ya que eliminar_prod devuelve un False o un True
            imprimir_exito("Producto eliminado.")
        else:
            imprimir_error("No se encontró ese ID.")

def menu_buscar():
    imprimir_titulo("Búsqueda de Productos")
    print("1. Buscar por ID")
    print("2. Buscar por Nombre o Categoría")
    opcion = input("Opción: ")
    
    if opcion == "1":
        id_prod = validar_input_int("ID")
        res = db_manager.buscar_producto_id(id_prod)
        if res:
            mostrar_tabla([res])                                            #por que el id es unico nos devuelve solo un dato
        else:
            imprimir_error("No encontrado.")
    elif opcion == "2":
        termino = validar_input_string("Término de búsqueda")
        res = db_manager.buscar_producto_texto(termino)
        mostrar_tabla(res)                                                  #nos devuelve una lista
    else:
        imprimir_error("Opción inválida.")

def main():
    db_manager.inicializar_db()
    while True:
        print("\n" + "="*30)
        print("   GESTIÓN DE INVENTARIO")
        print("="*30)
        print("1. Registrar Producto")
        print("2. Mostrar Todos")
        print("3. Actualizar Producto")
        print("4. Eliminar Producto")
        print("5. Buscar Producto")
        print("6. Salir")
        
        opcion = input("\nSeleccione una opción: ")
        
        if opcion == '1':
            menu_registracion()
        elif opcion == '2':
            menu_mostrar()
        elif opcion == '3':
            menu_actualizar()
        elif opcion == '4':
            menu_eliminar()
        elif opcion == '5':
            menu_buscar()
        elif opcion == '6':
            print("Saliendo del sistema...")
            sys.exit()
        else:
            imprimir_error("Opción no válida, intente nuevamente.")

if __name__ == "__main__":
    main()
    


