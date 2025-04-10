class Contacto:
    def __init__(self, nombre, telefono, correo):
        self.nombre = nombre
        self.telefono = telefono
        self.correo = correo

    def __str__(self):
        return f"{self.nombre} | Tel: {self.telefono} | Email: {self.correo}"
import os
import re

class GestionContactos:
    def __init__(self, archivo='contactos.txt'):
        self.contactos = []
        self.archivo = archivo
        self.cargar_contactos()

    def cargar_contactos(self):
        if not os.path.exists(self.archivo):
            return
        try:
            with open(self.archivo, 'r') as f:
                for linea in f:
                    nombre, telefono, correo = linea.strip().split(',')
                    self.contactos.append(Contacto(nombre, telefono, correo))
        except Exception as e:
            print(f"Error al leer el archivo: {e}")

    def guardar_contactos(self):
        try:
            with open(self.archivo, 'w') as f:
                for contacto in self.contactos:
                    f.write(f"{contacto.nombre},{contacto.telefono},{contacto.correo}\n")
        except Exception as e:
            print(f"Error al guardar el archivo: {e}")

    def agregar_contacto(self, nombre, telefono, correo):
        if not re.match(r"[^@]+@[^@]+\.[^@]+", correo):
            print("Correo electrónico inválido.")
            return
        self.contactos.append(Contacto(nombre, telefono, correo))
        self.guardar_contactos()
        print("✅ Contacto agregado.")

    def mostrar_contactos(self):
        if not self.contactos:
            print("No hay contactos guardados.")
        for contacto in self.contactos:
            print(contacto)

    def buscar_contacto(self, nombre):
        encontrados = [c for c in self.contactos if nombre.lower() in c.nombre.lower()]
        if encontrados:
            for c in encontrados:
                print(c)
        else:
            print("Contacto no encontrado.")

    def eliminar_contacto(self, nombre):
        original = len(self.contactos)
        self.contactos = [c for c in self.contactos if nombre.lower() not in c.nombre.lower()]
        if len(self.contactos) < original:
            self.guardar_contactos()
            print("✅ Contacto eliminado.")
        else:
            print("❌ No se encontró el contacto.")
def menu():
    sistema = GestionContactos()

    while True:
        print("\n--- MENÚ DE GESTIÓN DE CONTACTOS ---")
        print("1. Agregar contacto")
        print("2. Mostrar todos los contactos")
        print("3. Buscar contacto")
        print("4. Eliminar contacto")
        print("5. Salir")
        opcion = input("Selecciona una opción: ")

        if opcion == '1':
            nombre = input("Nombre: ").strip()
            telefono = input("Teléfono: ").strip()
            correo = input("Correo electrónico: ").strip()
            if nombre and telefono and correo:
                sistema.agregar_contacto(nombre, telefono, correo)
            else:
                print("❗ Todos los campos son obligatorios.")

        elif opcion == '2':
            sistema.mostrar_contactos()

        elif opcion == '3':
            nombre = input("Nombre a buscar: ").strip()
            sistema.buscar_contacto(nombre)

        elif opcion == '4':
            nombre = input("Nombre del contacto a eliminar: ").strip()
            sistema.eliminar_contacto(nombre)

        elif opcion == '5':
            print("¡Hasta luego!")
            break

        else:
            print("Opción no válida. Intenta otra vez.")

if __name__ == "__main__":
    menu()
