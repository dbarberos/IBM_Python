import tkinter as tk
from tkinter import messagebox

# Clase que representa una tarea pendiente
class Tarea:
    def __init__(self, descripcion):
        self.descripcion = descripcion
        self.completada = False

    def completar(self):
        self.completada = True

    def __str__(self):
        estado = 'Completada' if self.completada else 'Pendiente'
        return f"{self.descripcion} - {estado}"

# Clase que representa la lista de tareas pendientes
class ListaTareas:
    def __init__(self):
        self.tareas = {}

    def agregar_tarea(self, descripcion):
        numero = len(self.tareas) + 1
        self.tareas[numero] = Tarea(descripcion)

    def completar_tarea(self, numero):
        if numero in self.tareas:
            self.tareas[numero].completar()

    def eliminar_tarea(self, numero):
        if numero in self.tareas:
            del self.tareas[numero]

    def editar_tarea(self, numero, nueva_descripcion):
        if numero in self.tareas:
            self.tareas[numero].descripcion = nueva_descripcion

    def obtener_tareas(self):
        return [f"{numero}. {tarea}" for numero, tarea in self.tareas.items()]

# Funciones para conectar la GUI con la lógica del programa
def agregar():
    descripcion = entrada_tarea.get()
    if descripcion:
        lista_tareas.agregar_tarea(descripcion)
        entrada_tarea.delete(0, tk.END)
        actualizar_lista_tareas()

def completar():
    try:
        numero = int(entrada_numero.get())
        lista_tareas.completar_tarea(numero)
        actualizar_lista_tareas()
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingrese un número válido.")

def eliminar():
    try:
        numero = int(entrada_numero.get())
        lista_tareas.eliminar_tarea(numero)
        actualizar_lista_tareas()
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingrese un número válido.")

def editar():
    try:
        numero = int(entrada_numero.get(6))
        nueva_descripcion = entrada_tarea.get()
        if nueva_descripcion:
            lista_tareas.editar_tarea(numero, nueva_descripcion)
            entrada_tarea.delete(0, tk.END)
            entrada_numero.delete(0, tk.END)
            actualizar_lista_tareas()
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingrese un número válido.")

def actualizar_lista_tareas():
    lista_tareas_texto.delete(1.0, tk.END)
    for tarea in lista_tareas.obtener_tareas():
        lista_tareas_texto.insert(tk.END, tarea + "\n")

# Crear la instancia de la lista de tareas
lista_tareas = ListaTareas()

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Gestor de Tareas")

# Crear los widgets
etiqueta_tarea = tk.Label(ventana, text="Descripción de la tarea:")
etiqueta_tarea.pack()

entrada_tarea = tk.Entry(ventana, width=50)
entrada_tarea.pack()

boton_agregar = tk.Button(ventana, text="Agregar Tarea", command=agregar)
boton_agregar.pack()

etiqueta_numero = tk.Label(ventana, text="Número de la tarea:")
etiqueta_numero.pack()

entrada_numero = tk.Entry(ventana, width=5)
entrada_numero.pack()

boton_completar = tk.Button(ventana, text="Completar Tarea", command=completar)
boton_completar.pack()

boton_eliminar = tk.Button(ventana, text="Eliminar Tarea", command=eliminar)
boton_eliminar.pack()

boton_editar = tk.Button(ventana, text="Editar Tarea", command=editar)
boton_editar.pack()

lista_tareas_texto = tk.Text(ventana, height=10, width=50)
lista_tareas_texto.pack()

# Ejecutar el bucle principal de la GUI
ventana.mainloop()