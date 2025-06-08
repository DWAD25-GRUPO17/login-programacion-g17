

#vemos los metodos de autenticacion que tenemos en el programa

import re
from clases import Usuario
from base_simulada import usuarios
from menus import menu_usuario, menu_admin

# METODO VALIDACION DE CONTRASEÑA

def validar_contraseña(contraseña):
    if len(contraseña) < 6:
        return False 
    if not re.search(r"[A-Za-z]", contraseña):
        return False
    if not re.search(r"\d", contraseña):
        return False 
    return True

# METODO REGISTRO DE SESION

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

    nuevo_usuario = Usuario(nombre, mail, contraseña)
    usuarios[mail] = nuevo_usuario 

    print("Registro exitoso.")

# INICIO DE SESION

def iniciar_sesion():
    print("\n=== Iniciar Sesión ===")
    mail = input("Correo: ")

    if mail not in usuarios:
        print("Usuario no registrado.")
        return 
    
    usuario = usuarios[mail]
    for intento in range(3):
        contraseña = input("Contraseña: ")
        if usuario.verificar_contraseña(contraseña):
            print(f"\n ¡Bienvenido/a, {usuario.nombre} ({usuario.rol}!)")
    #REDIRIGIR AL MENU SEGUN ROL ASIGNADO
            if usuario.rol == "admin":
                menu_admin(usuario)
            else:
                menu_usuario(usuario)
            return
        else:
            print(f"Contraseña incorrecta. Intento {intento + 1}/3")

    print("Error de autenticacion. Contacta al administrador.")
