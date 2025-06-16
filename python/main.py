# main.py
from clases import Admin, UsuarioFinal
from base_simulada import usuarios
from menus import menu_principal

if __name__ == "__main__":
    usuarios["admin@mail.com"] = Admin("Super Admin", "admin@mail.com", "Admin1920")
    usuarios["ana@mail.com"] = UsuarioFinal("Ana López", "ana@mail.com", "ana123")

    print("Usuarios cargados:")
    for mail, u in usuarios.items():
        print(f" - {u.nombre} ({u.rol}) -> {mail}")

    menu_principal()
