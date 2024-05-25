class Nodo:
    def __init__(self, identidad, nombre):
        self.identidad = identidad
        self.nombre = nombre
        self.siguiente = None

class Cola:
    def __init__(self):
        self.frente = None
        self.final = None
    
    def esta_vacia(self):
        return self.frente is None
    
    def ingresar_usuario(self, identidad, nombre):
        nuevo_nodo = Nodo(identidad, nombre)
        if self.final is None:
            self.frente = self.final = nuevo_nodo
        else:
            self.final.siguiente = nuevo_nodo
            self.final = nuevo_nodo
        print(f"Usuario {nombre} con identidad {identidad} ingresado a la cola.")
    
    def atender_usuario(self):
        if self.esta_vacia():
            print("No hay usuarios en la cola para atender.")
            return None
        usuario_atendido = self.frente
        self.frente = self.frente.siguiente
        if self.frente is None:
            self.final = None
        print(f"Atendiendo a usuario {usuario_atendido.nombre} con identidad {usuario_atendido.identidad}.")
        return usuario_atendido

    def mostrar_cola(self):
        actual = self.frente
        if self.esta_vacia():
            print("La cola esta vacia.")
        else:
            print("Usuarios en la cola:")
            while actual:
                print(f"Identidad: {actual.identidad}, Nombre: {actual.nombre}")
                actual = actual.siguiente

# Ejemplo de uso interactivo
if __name__ == "__main__":
    cola = Cola()
    
    while True:
        print("\nMenu:")
        print("1. Ingresar usuario")
        print("2. Atender usuario")
        print("3. Mostrar cola")
        print("4. Salir")
        opcion = input("Seleccione una opcion: ")

        if opcion == "1":
            identidad = input("Ingrese la identidad del usuario: ")
            nombre = input("Ingrese el nombre del usuario: ")
            cola.ingresar_usuario(identidad, nombre)
        elif opcion == "2":
            cola.atender_usuario()
        elif opcion == "3":
            cola.mostrar_cola()
        elif opcion == "4":
            print("Saliendo del programa.")
            break
        else:
            print("Opción no valida, por favor intente de nuevo.")
