import sqlite3
from colorama import init, Fore, Back, Style
init()

#Establezco la conexion
conexion=sqlite3.connect("Inventario.db")
cursor=conexion.cursor()
#conexion.close()

#cursor.execute('''DROP TABLE Productos''')
#Creo mi tabla productos
cursor.execute('''
                CREATE TABLE IF NOT EXISTS Productos(
        id_producto INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT,
        descripcion TEXT,
        cantidad INTEGER,
        valor FLOAT,
        categoria TEXT
        )''')

#Defino la funcion de mi menú inicial.
def mostrar_menu():
    print(Fore.CYAN  +"*" * 31 + Style.RESET_ALL)
    print(Back.LIGHTCYAN_EX+Style.BRIGHT+"       MENÚ DE OPCIONES        \n"+Style.RESET_ALL)
    print("1_Agregar producto")
    print("2_Modificar producto")
    print("3_Eliminar producto")
    print("4_Mostrar todos los productos")
    print("5_Buscar productos")
    print("6_Reporte de productos con bajo stock")
    print(Fore.LIGHTRED_EX+"0_Salir"+Style.RESET_ALL)
    print(Fore.CYAN  +"*" * 31 + Style.RESET_ALL)
#Defino las opciones de mi menú de busqueda de la opcion modificar producto.
def menu_modificaciones():
    print("Qué desea modificar del producto?\n")
    print("1_Nombre.")
    print("2_Descripcion.")
    print("3_Cantidad.")
    print("4_Valor.")
    print("5_Categoria.")
    print(Fore.LIGHTRED_EX+"6_Salir."+Style.RESET_ALL)


#Funcion que me permite agregar productos
def agregar_producto():

    nombre=input("Ingresá el nombre del producto: ")
    descripcion=input("Ingresa una descripcion: ")
    cantidad=int(input("¿Cuantas unidades? "))
    valor=float(input("Ingresa el valor del producto: "))
    categoria=input("Ingresa la categoria del producto: ")

    cursor.execute("Insert into Productos(nombre, descripcion, cantidad, valor, categoria) VALUES (?,?,?,?,?)",(nombre, descripcion, cantidad, valor, categoria))
    conexion.commit()
    print("Producto añadido con exito.")

#Funcion que modifica mis productos.
def modificar_producto():
    id_producto = str(input("Ingrese el código del producto que desea modificar: "))
    cursor.execute("""
        SELECT * FROM Productos WHERE id_producto= ? """, (id_producto)
                )
    producto = cursor.fetchone()

    if not producto:
        print("Producto no encontrado")
        return 
    while True:
            menu_modificaciones()
            opcion_modificacion = int(input("Ingrese una opcion: "))
            if opcion_modificacion==1:#Modifico nombre
                nuevo_nombre = str(input("Ingrese el nuevo nombre: "))
                cursor.execute(f""" UPDATE Productos SET nombre = ? WHERE id_producto = ? """,(nuevo_nombre, id_producto))
                if cursor.rowcount > 0:
                        print("Producto", id_producto, " actualizado con éxito.")
                        conexion.commit()
                else:
                        print("No se encontró un producto con ese codigo.")
        
            elif opcion_modificacion==2:#modifico descripcion
                nueva_descripcion = str(input("Ingrese la nueva descripción: "))
                cursor.execute(f"""
                    UPDATE Productos SET descripcion = ? WHERE id_producto = ? """,(nueva_descripcion, id_producto))
                if cursor.rowcount > 0:
                    print("Producto", id_producto, " actualizado con éxito.")
                    conexion.commit()
                else:
                    print("No se encontró un producto con ese codigo.")
                    
            elif opcion_modificacion==3:#modifico la cantidad
                nueva_cantidad = int(input("Ingrese la nueva cantidad: "))
                cursor.execute("""UPDATE Productos SET cantidad=? WHERE id_producto= ?""", (nueva_cantidad,id_producto))
                if cursor.rowcount > 0:
                    print("Producto", id_producto, " actualizado con éxito.")
                    conexion.commit()
                else:
                    print("No se encontró un producto con ese codigo.")
            elif opcion_modificacion==4:#modifico el precio
                nuevo_valor = input("Ingrese el nuevo valor: ")
                cursor.execute("""UPDATE Productos SET valor=? WHERE id_producto= ?""", (nuevo_valor,id_producto))
                if cursor.rowcount > 0:
                    print("Producto", id_producto, " actualizado con éxito.")
                    conexion.commit()
                else:
                    print("No se encontró un producto con ese codigo.")
                    
            elif opcion_modificacion==5:#modifico la categoria a la cual pertenece
                nueva_categoria = input("Ingrese la nueva categoria: ")
                cursor.execute("""UPDATE Productos SET categoria=? WHERE id_producto= ?""", (nueva_categoria,id_producto))
                if cursor.rowcount > 0:
                    print("Producto", id_producto, " actualizado con éxito.")
                    conexion.commit()  
                else:
                    print("No se encontró un producto con ese codigo.")
                    
            elif opcion_modificacion==6:#Salgo del menu de modificaciones
                print("Cancelando modificacion")
                break
            
            else:
                print("Producto no encontrado.")

#Funcion que me permite eliminar productos.            
def eliminar_producto():
    id_producto = str(input("Ingrese el código del producto que desea eliminar: "))
    cursor.execute("""DELETE FROM Productos WHERE id_producto = ? """,(id_producto))
    cursor.fetchone()
    if cursor.rowcount > 0: 
        print("Producto con código", id_producto,"eliminado con éxito.")
        conexion.commit()
    else:
        print("Producto no encontrado.")

#Funcion que me permite mostrar mis productos.
def mostrar_productos():
    cursor.execute('''SELECT * FROM Productos''')
    Productos= cursor.fetchall()
    
    if Productos:
        print(Back.LIGHTMAGENTA_EX+"Inventario de productos".center(80)+Style.RESET_ALL)
        print(Fore.LIGHTBLACK_EX + "ID".ljust(6) + "Nombre".ljust(18) + "Descripcion".ljust(30) + "Cantidad".ljust(10) + "    Valor".ljust(10)+ "    Categoria".ljust(30))
        for producto in Productos:
            print(
                str(producto[0]).ljust(6),
                str(producto[1]).ljust(18),
                str(producto[2]).ljust(30),
                str(producto[3]).ljust(10),
                str(producto[4]).ljust(10),
                str(producto[5]).ljust(30)+Style.RESET_ALL)
        
    else:
        print("No hay productos en el inventario.")


#Funcion que me permite buscar mis productos por su codigo
def buscar_productos():
    nombre = input("Ingrese el nombre del producto que desea buscar: ")
    cursor.execute("SELECT * FROM Productos WHERE nombre LIKE ? ",('%'+nombre+'%',))
    resultado=cursor.fetchone()
    if resultado:
        print(Back.LIGHTBLUE_EX+"Acerca del producto: ".center(31) + Style.RESET_ALL)
        print(Fore.LIGHTWHITE_EX+"Codigo: ",str(resultado[0]).rjust(23))
        print("Nombre: ",str(resultado[1]).rjust(23))
        print("Descripcion: ",str(resultado[2]).rjust(18))
        print("Cantidad: ",str(resultado[3]).rjust(21))
        print("Valor: ",str(resultado[4]).rjust(24))
        print("Categoria: ",str(resultado[5]).rjust(20) + Style.RESET_ALL)
    else:
        print("No se encontró un producto con ese nombre.")
        
#Funcion que me permite generar un reporte de productos con bajo stock       
def control_stock():
    limite = str(input("Ingrese el límite de stock para generar el reporte: "))
    cursor.execute("SELECT * FROM Productos WHERE cantidad < ?",(limite,))
    resultados = cursor.fetchall()
    if resultados:
        print (Back.GREEN+"PRODUCTOS CON BAJO STOCK: ".center(30)+Style.RESET_ALL)
        for registro in resultados:
            print("Codigo:",str(registro[0]).rjust(23))
            print("Nombre:",str(registro[1]).rjust(23))
            print("Descripcion:",str(registro[2]).rjust(18))
            print("Cantidad:",str(registro[3]).rjust(21))
            print("Valor:",str(registro[4]).rjust(24))
            print("Categoria:",str(registro[5]).rjust(20))
            print(Fore.LIGHTGREEN_EX+"*"*31+Style.RESET_ALL)
    else:
        print("No se encontraron prdouctos con bajo stock.")
#defino la funcion de Iniciación del programa con todas las funciones integradas a cada opcion
def iniciar_programa():
    while True:
        mostrar_menu()
        opcion= int(input("Por favor, elegí una opción: "))
        if opcion == 1:
            agregar_producto()
        elif opcion == 2:
            modificar_producto()
        elif opcion == 3:
            eliminar_producto()
        elif opcion==4:
            mostrar_productos()
        elif opcion==5:
            buscar_productos()
        elif opcion==6:
            control_stock()
        elif opcion==0:
            print(" Estas saliendo del programa...")
            conexion.close()
            break
        else:
            print("Opción inválida, intentá de nuevo.")
#inicializo la funcion del programa
iniciar_programa()
cursor=conexion.close()