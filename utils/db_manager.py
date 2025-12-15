
#Aca vamos a manejar nuestra base de datos y van a estar 
#las funciones para manejar la base de datos


import sqlite3
from utils.helper import imprimir_error                                   #Traemos del archivo helpers que creamos
from utils.config import BD_NAME, TABLE_NAME 

def conectar_db():                                                        #le paso el nombre de la base de datos y la funcion se encarga de crearla o conectarla si ya existe
    return sqlite3.connect(BD_NAME) 

def inicializar_db():                                                     #uso los comandos sql para crear la tabla
    try:
        with conectar_db() as conexion:                                   #Se encarga de abrir y cerrar en un solo comando
            cursor = conexion.cursor()                                   #guardo en la variable curso, y con esto puedo usar los comandos de sqlit3
            sql = f'''
            CREATE TABLE IF NOT EXISTS {TABLE_NAME}(       
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT NOT NULL,
                descripcion TEXT,
                cantidad INTEGER NOT NULL,
                precio REAL NOT NULL,
                categoria TEXT)
                '''                                                        #este es el comando para crear la tabla  que lo guardo en la variable sql
        cursor.execute(sql)                                                # este comando ejecuta el comando alamcenado en la variable sql
        conexion.commit()                                                 # cada vez que uso un comando de sql tenemos que hacer commit a la conexion
    except sqlite3.Error as error:
        imprimir_error(f"Error en la inicializacion de la base de datos. {error}")

def registrar_producto(nombre,descripcion,cantidad,precio,categoria):      # id se crea con la tabla y es autoincremental   
    try:
        with conectar_db() as conexion:                                    #Medida de seguridad que hay que tomar siempre para evitar sql inyection
            cursor = conexion.cursor()
            cursor.execute(                                                 # usar triple comilla
            f'''INSERT INTO {TABLE_NAME}                                    
            (nombre,descripcion,cantidad,precio,categoria)
            VALUES(?,?,?,?,?)''',(nombre,descripcion,cantidad,precio,categoria)
            )                                                               
            conexion.commit()
            return True
    except sqlit3.Error as error:
        imprimir_error(f"Error en el registro del producto. {error}")
        return False

def obtener_producto():
    try:
        with conectar_db() as conexion:                                 
            cursor = conexion.cursor()
            cursor.execute(f"SELECT * FROM {TABLE_NAME}")
            return cursor.fetchall()
    except sqlite3.Error as error:
        imprimir_error(f"Error al leer datos. {error}")
        return []                                                           #devuelve una lista vacia

def buscar_producto_id(id_prod):
    try:
        with conectar_db() as conexion:                                 
            cursor = conexion.cursor()
            cursor.execute(f"SELECT * FROM {TABLE_NAME} WHERE id = ?", (id_prod,))
            return cursor.fetchone()
    except sqlite3.Error as error:
        imprimir_error(f"Error al buscar. {error}")
        return None
                    
def buscar_producto_texto(termino):                                                           #segun categoria o nombre
    try:
        with conectar_db() as conexion:                                 
            cursor = conexion.cursor()
            busqueda = f"SELECT * FROM {TABLE_NAME} WHERE nombre LIKE ? OR categoria LIKE ?"
            cursor.execute(busqueda,(f'%{termino}%',f'%{termino}%'))
            return cursor.fetchall()
    except sqlite3.Error as error:
        imprimir_error(f"Error al buscar. {error}")
        return []    
    
def actualizar_producto(id_prod,nombre,descripcion,cantidad,precio,categoria):
    try:
        with conectar_db() as conexion:                                 
            cursor = conexion.cursor()
            sql = f"UPDATE {TABLE_NAME} SET nombre=?, descripcion=?, cantidad=?, precio=?, categoria=? WHERE id = ?"
            cursor.execute(sql,(nombre,descripcion,cantidad,precio,categoria,id_prod))
            if cursor.rowcount > 0 :
                conexion.commit()
                return True
            return False
    except sqlite3.Error as error:
        imprimir_error(f"Error al actualizar. {error}")
        return False

def eliminar_productos(id_prod):
        try:
            with conectar_db() as conexion:                                 
                cursor = conexion.cursor()
                cursor.execute(f"DELETE FROM {TABLE_NAME} WHERE id = ?",(id_prod,))
                if cursor.rowcount > 0 :
                    conexion.commit()
                    return True
                return False
        except sqlite3.Error as error:
            imprimir_error(f"Error al eliminar. {error}")
            return False