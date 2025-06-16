# menus.py
from auth import registrarse, iniciar_sesion
# COMENTARIO

def menu_principal():
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
