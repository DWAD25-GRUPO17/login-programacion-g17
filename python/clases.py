# clases.py
from base_simulada import usuarios

class Usuario:
    def __init__(self, nombre, mail, contraseña):
        self.nombre = nombre
        self.mail = mail
        self._contraseña = contraseña
        self.rol = None

    def verificar_contraseña(self, contraseña):
        return self._contraseña == contraseña

    def ver_datos_sesion(self):
        print(f"\nPerfil:\nNombre: {self.nombre}\nCorreo: {self.mail}\nRol: {self.rol}")

class UsuarioFinal(Usuario):
    def __init__(self, nombre, mail, contraseña):
        super().__init__(nombre, mail, contraseña)
        self.rol = "usuario"

    def mostrar_menu(self):
        while True:
            print("\nMenú de Usuario")
            print("1. Ver datos de sesión.")
            print("2. Cerrar sesión.")
            opcion = input("Opción: ")

            if opcion == "1":
                self.ver_datos_sesion()
            elif opcion == "2":
                print("Sesión cerrada.")
                break
            else:
                print("Opción no válida.")

class Admin(Usuario):
    def __init__(self, nombre, mail, contraseña):
        super().__init__(nombre, mail, contraseña)
        self.rol = "admin"

    def crear_usuario(self, gestor, nombre, mail, contraseña):
        if mail in gestor:
            print("El usuario ya existe.")
        else:
            gestor[mail] = UsuarioFinal(nombre, mail, contraseña)
            print("Usuario creado correctamente.")

    def eliminar_usuario(self, gestor, mail):
        if mail in gestor:
            del gestor[mail]
            print("Usuario eliminado correctamente.")
        else:
            print("Usuario no encontrado.")

    def mostrar_menu(self):
        while True:
            print("\nMenú de Admin")
            print("1. Crear usuario.")
            print("2. Eliminar usuario.")
            print("3. Cerrar sesión.")
            opcion = input("Opción: ")

            if opcion == "1":
                nombre = input("Nombre nuevo usuario: ")
                mail = input("Correo: ")
                contraseña = input("Contraseña: ")
                self.crear_usuario(usuarios, nombre, mail, contraseña)
            elif opcion == "2":
                mail = input("Correo del usuario a eliminar: ")
                self.eliminar_usuario(usuarios, mail)
            elif opcion == "3":
                print("Sesión cerrada.")
                break
            else:
                print("Opción no válida.")
