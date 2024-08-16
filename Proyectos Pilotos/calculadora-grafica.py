import tkinter as tk
import math

def calcular(expr):
    try:
        return str(eval(expr))
    except Exception:
        return "Error"

def agregar(expr, caracter):
    return expr + str(caracter)

def borrar(expr):
    return expr[:-1]

ventana = tk.Tk()
ventana.title("Calculadora Científica")

expr = tk.StringVar()

campo = tk.Entry(ventana, textvariable=expr)
campo.grid(row=0, column=0, columnspan=4)

botones = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+',
    '(', ')', 'C', 'sin',
    'cos', 'tan', 'log', 'sqrt'
]

row_val = 1
col_val = 0
for boton in botones:
    def cmd(x=boton):
        if x == '=':
            expr.set(calcular(expr.get()))
        elif x == 'C':
            expr.set('')
        elif x in '0123456789.+-*/()':
            expr.set(agregar(expr.get(), x))
        elif x == 'sin':
            expr.set(agregar(expr.get(), 'math.sin('))
        elif x == 'cos':
            expr.set(agregar(expr.get(), 'math.cos('))
        elif x == 'tan':
            expr.set(agregar(expr.get(), 'math.tan('))
        elif x == 'log':
            expr.set(agregar(expr.get(), 'math.log('))
        elif x == 'sqrt':
            expr.set(agregar(expr.get(), 'math.sqrt('))

    tk.Button(ventana, text=boton, width=5, command=cmd).grid(row=row_val, column=col_val)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

ventana.mainloop()
tareas = {}
tareas_eliminadas = {}

def agregar_tarea():
    while True:
        tarea = input("Ingrese el nombre de la tarea: ")
        if not tarea:
            print("El nombre de la tarea no puede estar vacío. Intente de nuevo.")
            continue
        tareas[tarea] = "incompleta"
        otra_tarea = input("¿Quieres agregar otra tarea? (si/no): ")
        if otra_tarea.lower() != "si":
            break

def mostrar_tareas():
    if tareas:
        for tarea, estado in tareas.items():
            print(f"Tarea: {tarea}, Estado: {estado}")
    else:
        print("Aún no se ha generado una tarea.")
        agregar = input("¿Desea generar una tarea? (si/no): ")
        if agregar.lower() == "si":
            agregar_tarea()

def mostrar_tareas_incompletas():
    tareas_incompletas = {tarea: estado for tarea, estado in tareas.items() if estado == "incompleta"}
    if tareas_incompletas:
        for tarea, estado in tareas_incompletas.items():
            print(f"Tarea: {tarea}, Estado: {estado}")
    else:
        print("No hay tareas incompletas para mostrar.")

def completar_tarea():
    tarea = input("Ingrese el nombre de la tarea a completar: ")
    if tarea in tareas:
        tareas[tarea] = "completada"
    else:
        print("La tarea no existe.")

def eliminar_tarea():
    tarea = input("Ingrese el nombre de la tarea a eliminar: ")
    if tarea in tareas:
        confirmacion = input(f"¿Estás seguro de que quieres eliminar esta tarea: {tarea}? (si/no): ")
        if confirmacion.lower() == "si":
            tareas_eliminadas[tarea] = tareas[tarea]
            del tareas[tarea]
            print(f"Tarea eliminada: {tarea}.")
        else:
            print("Operación cancelada, volviendo al menú.")
    else:
        print("La tarea no existe.")

def mostrar_tareas_eliminadas():
    if tareas_eliminadas:
        for tarea, estado in tareas_eliminadas.items():
            print(f"Tarea eliminada: {tarea}, Estado antes de eliminar: {estado}")
    else:
        print("No hay tareas eliminadas para mostrar.")

while True:
    print("\n1. Agregar una tarea")
    print("2. Mostrar todas las tareas")
    print("3. Mostrar solo las tareas incompletas")
    print("4. Marcar una tarea como completada")
    print("5. Eliminar una tarea")
    print("6. Mostrar tareas eliminadas")
    print("7. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        agregar_tarea()
    elif opcion == "2":
        mostrar_tareas()
    elif opcion == "3":
        mostrar_tareas_incompletas()
    elif opcion == "4":
        completar_tarea()
    elif opcion == "5":
        eliminar_tarea()
    elif opcion == "6":
        mostrar_tareas_eliminadas()
    elif opcion == "7":
        break
    else:
        print("Opción no válida. Intente de nuevo.")
