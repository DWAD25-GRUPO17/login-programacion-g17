

#vemos los metodos de autenticacion que tenemos en el programa

import re
from clases import UsuarioFinal
from base_simulada import usuarios

PASS_CHAR_MIN = 6
MAX_INTENTOS = 3

def validar_contraseña(contraseña):
    if len(contraseña) < PASS_CHAR_MIN:
        return False
    if not re.search(r"[A-Za-z]", contraseña):
        return False
    if not re.search(r"\d", contraseña):
        return False
    if re.search(r"[Ññ]", contraseña):
        return False
    return True

def registrarse():
    print("\n=== Registro de Usuario ===")
    nombre = input("Nombre: ")

    while True:
        mail = input("Correo: ")
        if mail in usuarios:
            print("Ya existe un usuario con ese correo.")
        else:
            break

    while True:
        contraseña = input("Contraseña (mínimo 6 caracteres, letras y números): ")
        confirmacion = input("Confirmar contraseña: ")
        if contraseña != confirmacion:
            print("Las contraseñas no coinciden.")
            continue
        if not validar_contraseña(contraseña):
            print("La contraseña no cumple los requisitos.")
            continue
        break

    nuevo_usuario = UsuarioFinal(nombre, mail, contraseña)
    usuarios[mail] = nuevo_usuario
    print("Registro exitoso.")

def iniciar_sesion():
    print("\n=== Iniciar Sesión ===")
    mail = input("Correo: ")

    if mail not in usuarios:
        print("Usuario no registrado.")
        return

    usuario = usuarios[mail]
    for intento in range(MAX_INTENTOS):
        contraseña = input("Contraseña: ")
        if usuario.verificar_contraseña(contraseña):
            print(f"\n¡Bienvenido/a, {usuario.nombre} ({usuario.rol})!")
            usuario.mostrar_menu()
            return
        else:
            print(f"Contraseña incorrecta. Intento {intento + 1}/3")

    print("Error de autenticacion. Contacta al administrador.")
