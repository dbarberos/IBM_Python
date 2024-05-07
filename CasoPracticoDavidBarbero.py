# Clase que representa una tarea pendiente
class Tarea:
    # Constructor de la clase
    def __init__(self, descripcion):
        self.descripcion = descripcion
        self.completada = False

    # Método para marcar la tarea como completada
    def completar(self):
        self.completada = True

    # Método para obtener la descripción de la tarea
    def __str__(self):
        return self.descripcion


# Clase que representa la lista de tareas pendientes
class ListaTareas:
    # Constructor de la clase
    def __init__(self):
        self.tareas = {}

    # Método para agregar una nueva tarea
    def agregar_tarea(self, descripcion):
        # Generamos un número único para la nueva tarea
        numero = len(self.tareas) + 1
        # Creamos la nueva tarea
        nueva_tarea = Tarea(descripcion)
        # Agregamos la nueva tarea a la lista
        self.tareas[numero] = nueva_tarea
        # Imprimimos un mensaje de confirmación
        print(f"Se ha agregado la tarea {descripcion}")

    # Método para marcar una tarea como completada
    def completar_tarea(self, numero):
        # Verificamos si el número de tarea existe en la lista
        if numero in self.tareas:
            # Marcamos la tarea como completada
            self.tareas[numero].completar()
            # Imprimimos un mensaje de confirmación
            print(f"Se ha marcado la tarea {self.tareas[numero]} como completada")
        else:
            # Imprimimos un mensaje de error
            print("No existe una tarea con ese número")

    # Método para mostrar todas las tareas
    def mostrar_tareas(self):
        # Recorremos todas las tareas de la lista
        for numero, tarea in self.tareas.items():
            # Imprimimos el número de tarea y su descripción
            print(f"{numero}. {tarea}")

    # Método para eliminar una tarea.
    def eliminar_tarea(self, numero):
        # Verificamos si el número de tarea existe en la lista
        if numero in self.tareas:
            # Eliminamos la tarea de la lista
            del self.tareas[numero]
            # Imprimimos un mensaje de confirmación
            print(f"Se ha eliminado la tarea {numero}")
        else:
            # Imprimimos un mensaje de error
            print("No existe una tarea con ese número")
    
    # Método para editar la descripción de una tarea.
    def editar_tarea(self, numero, nueva_descripcion):
        #Verificamos si el número de tarea existe en la lista
        if numero in self.tareas:
            # Actualizamos la descripcón de la tarea
            self.tareas[numero].descripcion = nueva_descripcion 
            # Imprimimos un mensaje de confirmación
            print(f"Se ha actualizado la tarea {numero} con la nueva descripción")
        else:
            # Imprimimos un mensaje de error
            print("No existe una tarea con ese número")
        

3
# Creamos una nueva lista de tareas
lista_tareas = ListaTareas()

# Bucle principal del programa
while True:
    try:
        # Mostramos el menú de opciones
        print("\nMenú de opciones:")
        print("1. Agregar tarea")
        print("2. Marcar tarea como completada")
        print("3. Mostrar tareas")
        print("4. Eliminar tarea")
        print("5. Editar la descripción de una tarea")
        print("6. Salir")

        # Pedimos al usuario que ingrese una opción
        opcion = int(input("Ingrese una opción: "))

        # Verificamos la opción ingresada
        if opcion == 1:
            # Pedimos al usuario que ingrese la descripción de la nueva tarea
            descripcion = input("Ingrese la descripción de la nueva tarea: ")
            # Agregamos la nueva tarea a la lista
            lista_tareas.agregar_tarea(descripcion)
        elif opcion == 2:
            # Pedimos al usuario que ingrese el número de tarea a marcar como completada
            numero = int(input("Ingrese el número de tarea a marcar como completada: "))
            # Marcamos la tarea como completada
            lista_tareas.completar_tarea(numero)
        elif opcion == 3:
            # Mostramos todas las tareas de la lista
            lista_tareas.mostrar_tareas()
        elif opcion == 4:
            # Pedimos al usuario que ingrese el número de tarea a eliminar
            numero = int(input("Ingrese el número de tarea a eliminar: "))
            # Eliminamos la tarea de la lista
            lista_tareas.eliminar_tarea(numero)
        elif opcion == 5:
            # Pedimos al usuario que ingrese el número de tarea a editar
            numero = int(input("Ingrese el número de tarea a editar: "))
            # Pedimos al usuario que ingrese la nueva descripción de la tarea
            nueva_descripcion = input("Ingrese la nueva descripción de la tarea: ")
            # Editamos la descripción de la tarea
            lista_tareas.editar_tarea(numero,nueva_descripcion)
        elif opcion == 6:
            # Salimos del bucle principal del programa
            break
        else:
            # Imprimimos un mensaje de error
            print("Opción no válida")
    except ValueError:
        print("Por favor, ingrese un número válido:")