

# ARCHIVO PRINCIPAL DONDE SE EJECUTA EL PROGRAMA

import re 
from clases import Admin, Usuario
from base_simulada import usuarios
from auth import registrarse, iniciar_sesion

    # MENU PRINCIPAL

def menu():
    while True:
        print("\n=== MENÚ PRINCIPAL ===")
        print("1. Registrarse")
        print("2. Iniciar sesión")
        print("3. Salir")

        opcion = input("Elegí una opción: ")

        if opcion == "1":
            registrarse()
        elif opcion == "2":
            iniciar_sesion()
        elif opcion == "3":
            print("Gracias por usar el sistema.")
            break
        else:
            print("Opción inválida.")

# PROGRAMA PRINCIPAL!

if __name__ == "__main__":
    # Precarga de datos
    usuarios["admin@mail.com"] = Admin("Super Admin", "admin@mail.com", "Admin1920")
    usuarios["ana@mail.com"] = Usuario("Ana López", "ana@mail.com", "ana123")

    print("Usuarios cargados:")
    for mail, u in usuarios.items():
        print(f" - {u.nombre} ({u.rol}) -> {mail}")

    menu()