# Sistema de Gestión de Inventarios

Este proyecto es un sistema de gestión de inventarios que permite agregar, 
modificar, eliminar, buscar y mostrar productos, así como generar un reporte de productos con bajo stock.
 Utiliza una base de datos SQLite para almacenar la información de los productos y la biblioteca `colorama` para mejorar la presentación de la interfaz de usuario en la terminal.

## Requisitos

- Python 3.x
- `colorama` (instalable con `pip install colorama`)
- SQLite3 (viene incluido con Python)

## Funcionalidades

El sistema permite realizar las siguientes operaciones sobre el inventario:

### 1. Agregar Producto
Permite agregar un nuevo producto al inventario, especificando:
- Nombre
- Descripción
- Cantidad
- Valor
- Categoría

### 2. Modificar Producto
Permite modificar los detalles de un producto existente. Se puede modificar:
- Nombre
- Descripción
- Cantidad
- Valor
- Categoría

### 3. Eliminar Producto
Permite eliminar un producto del inventario mediante su código de identificación (ID).

### 4. Mostrar Todos los Productos
Muestra una lista con todos los productos registrados en el inventario.

### 5. Buscar Producto
Permite buscar un producto por su nombre, mostrando todos los detalles del producto encontrado.

### 6. Reporte de Productos con Bajo Stock
Permite generar un reporte de productos cuyo stock (cantidad) es inferior a un límite especificado por el usuario.

### 0. Salir
Cierra el programa y la conexión a la base de datos.

## Instalacion

Si deseas trabajar fuera de la terminal de VSC, puedes generar un ejecutable con:
'pip install auto-py-to-exe'
