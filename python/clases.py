
# Solo vemos las clases, como Usuario, Admin. 

from base_simulada import usuarios


class Usuario:
    def __init__(self, nombre, mail, contraseña):
        self.nombre = nombre
        self.mail = mail
        self.contraseña = contraseña 
        self.rol = "usuario"


#metodo usuario verificar contraseña

    def verificar_contraseña(self, contraseña):
        return self.contraseña == contraseña 
    

 #clase heredada de usuario 

class Admin(Usuario):
    def __init__(self, nombre, mail, contraseña):
        super().__init__(nombre, mail, contraseña)
        self.rol ="admin"

 
#metodo admin crear usuario
    def crear_usuario(self, nombre, mail, contraseña):
        if mail in usuarios:
            print("El usuario ya existe.")
        else:
            usuarios[mail] = Usuario(nombre, mail, contraseña)
            print("Usuario creado correctamente.")
    
#metodo admin eliminar usuario

    def eliminar_usuario(self, mail):
        if mail in usuarios:
            del usuarios[mail]
            print("Usuario eliminado correctamente.")
        else:
            print("Usuario no encontrado")