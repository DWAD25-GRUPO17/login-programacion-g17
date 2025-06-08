# vemos los diferentes menus segun el rol

    #MENU DE USUARIO

def menu_usuario(usuario):

    while True:
        print("\n Menú de Usuario")
        print("1. Ver datos de sesion.")
        print("2. Cerrar sesion.")
        opcion = input("Opcion: ")

        if opcion == "1":
            print(f"\n Perfil:\n Nombre de usuario: {usuario.nombre}\n Correo: {usuario.mail}")
        elif opcion == "2":
            print("Sesion cerrada.")
            break
        else:
            print("Opcion no valida.")



    #MENU DE ADMINISTRADOR

def menu_admin(admin):
    while True:
        print("\n Menu de Admin")
        print("1. Crear usuario.")
        print("2. Eliminar usuario.")
        print("3. Cerrar sesion.")
        opcion = input("Opcion: ")
        if opcion == "1":
            nombre = input("Nombre nuevo usuario: ")
            mail = input("Correo: ")
            contraseña = input("Contraseña: ")
            admin.crear_usuario(nombre, mail, contraseña)
        elif opcion == "2":
            mail = input("Correo del usuario a eliminar: ")
            admin.eliminar_usuario(mail)
        elif opcion == "3":
            print("Sesion cerrada.")
            break 
        else:
            print("Opcion no valida.")

   

