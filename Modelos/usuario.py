# Clase que representa a un usuario del sistema, con ID, nombre, usuario, contraseña y su rol.
class Usuario:
    def __init__(self, id, nombre, usuario, contrasena, rol):
        self.id = id
        self.nombre = nombre
        self.usuario = usuario
        self.contrasena = contrasena
        self.rol = rol
