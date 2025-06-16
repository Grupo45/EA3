class Rol:
    def __init__(self, id, nombre):
        self.id = id
        self.nombre = nombre

class Usuario:
    def __init__(self, id, nombre, usuario, contrasena, rol):
        self.id = id
        self.nombre = nombre
        self.usuario = usuario
        self.contrasena = contrasena
        self.rol = rol
