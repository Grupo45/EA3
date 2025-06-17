class Autentificacion:
    @staticmethod
    def login(usuario_input, contrasena_input, usuarios):
        for usuario in usuarios:
            if usuario.usuario == usuario_input and usuario.contrasena == contrasena_input:
                return usuario
        return None
