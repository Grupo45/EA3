# Función para verificar si las credenciales ingresadas coinciden con un usuario registrado.
# Recorre la lista de usuarios y compara nombre de usuario y contraseña.
# Si encuentra coincidencia, retorna el objeto Usuario correspondiente; si no, retorna None.
def login(usuario_input, contrasena_input, usuarios):
    for usuario in usuarios:
        if usuario.usuario == usuario_input and usuario.contrasena == contrasena_input:
            return usuario
    return None