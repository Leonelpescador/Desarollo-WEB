almacen ={}
def agregar_articulo():
    while True:
        codigo = input("Introduce el código del artículo: ")
        nombre = input("Introduce el nombre del artículo: ")
        precio = float(input("Introduce el precio del artículo: "))
        existencia = int(input("Introduce la existencia del artículo: "))
        if codigo in almacen:
            print("El artículo ya existe.")
        else:
            almacen[codigo] = {'nombre': nombre, 'precio': precio, 'existencia': existencia}
            print("Artículo agregado con éxito.")
        opcion = input("¿Deseas agregar otro artículo? (s/n): ")
        if opcion.lower() != 's':
            break


def mostrar_articulo(codigo):
    if codigo in almacen:
        print(almacen[codigo])
    else:
        print("Artículo no encontrado.")

def modificar_articulo(codigo, nombre, precio, existencia):
    while True:
        codigo = input("Introduce el código del artículo: ")
        nombre = input("Introduce el nombre del artículo: ")
        precio = float(input("Introduce el precio del artículo: "))
        existencia = int(input("Introduce la existencia del artículo: "))
        if not codigo:
         print("Aun no ingreso un articulo")
        if codigo in almacen:
         almacen[codigo] = {'nombre': nombre, 'precio': precio, 'existencia': existencia}
        else:
         print("Artículo no encontrado.")
         opcion = input("¿Deseas agregar otro artículo? (s/n): ")
        if opcion.lower() != 's':
            break

def eliminar_articulo(codigo):
    if codigo in almacen:
        del almacen[codigo]
    else:
        print("Artículo no encontrado.")

while True:
    print("1. Agregar artículo")
    print("2. Mostrar artículos")
    print("3. Modificar artículos")
    print("4. Eliminar artículos")
    print("5. Salir")
    opcion = input("Elige una opción: ")
    if opcion == '1':
        codigo = input("Introduce el código del artículo: ")
        nombre = input("Introduce el nombre del artículo: ")
        precio = float(input("Introduce el precio del artículo: "))
        existencia = int(input("Introduce la existencia del artículo: "))
        agregar_articulo(codigo, nombre, precio, existencia)
    elif opcion == '2':
        codigo = input("Introduce el código del artículo: ")
        mostrar_articulo(codigo)
    elif opcion == '3':
        codigo = input("Introduce el código del artículo: ")
        nombre = input("Introduce el nuevo nombre del artículo: ")
        precio = float(input("Introduce el nuevo precio del artículo: "))
        existencia = int(input("Introduce la nueva existencia del artículo: "))
        modificar_articulo(codigo, nombre, precio, existencia)
    elif opcion == '4':
        codigo = input("Introduce el código del artículo: ")
        eliminar_articulo(codigo)
    elif opcion == '5':
        break