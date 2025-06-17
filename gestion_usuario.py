from Modelos.usuario import Usuario
from herramientas import Herramientas


class GestionUsuario:
    # Permite registrar un nuevo usuario.
    # Verifica que la contraseña cumpla con requisitos y que el nombre de usuario no exista.
    # Crea un nuevo Usuario con rol estandar (2) y lo agrega a la lista.
    @staticmethod
    def registrar_usuario(usuarios, roles, contador_id):
        print("\n--- Registro de nuevo usuario ---")
        nombre = input("Nombre completo: ")
        usuario = input("Nombre de usuario: ")

        # Bucle para validar contraseña
        while True:
            contrasena = input("Contraseña (mínimo 8 caracteres, con al menos una mayúscula y un número): ")
            if Herramientas.validar_contrasena(contrasena):
                break
            print("Contraseña inválida. No cumple con los requisitos. Intente nuevamente.") 

        if any(u.usuario == usuario for u in usuarios):
            print("El nombre de usuario ya existe.")
            return contador_id

        nuevo_usuario = Usuario(contador_id, nombre, usuario, contrasena, roles[2])
        usuarios.append(nuevo_usuario)
        print("Usuario registrado exitosamente.")
        return contador_id + 1

    # Imprime todos los usuarios registrados en formato tabla.
    @staticmethod
    def listar_usuarios(usuarios):
        print("\n---------- LISTADO DE USUARIOS ----------")
        print(f"{'ID':<5}{'Nombre':<20}{'Usuario':<15}{'Rol':<15}")
        print("-" * 55)
        for u in usuarios:
            print(f"{u.id:<5}{u.nombre:<20}{u.usuario:<15}{u.rol.nombre:<15}")

    # Elimina un usuario por su ID, previa confirmación.
    # Si no se encuentra el ID, informa al usuario.
    @staticmethod
    def eliminar_usuario(usuarios):
        try:
            id_u = int(input("Ingrese el ID del usuario a eliminar: "))
            for u in usuarios:
                if u.id == id_u:
                    if Herramientas.confirmar_accion(f"Seguro que desea eliminar al usuario '{u.usuario}'?"):
                        usuarios.remove(u)
                        print("Usuario eliminado.")
                    return
            print("Usuario no encontrado.")
        except ValueError:
            print("ID invalido.")

    # Cambia el rol de un usuario por ID.
    # Muestra los roles disponibles y actualiza el rol si el nuevo ID de rol es válido.
    @staticmethod
    def cambiar_rol(usuarios, roles):
        try:
            id_u = int(input("Ingrese el ID del usuario: "))
            for u in usuarios:
                if u.id == id_u:
                    print("1 - Administrador\n2 - Usuario estándar")
                    nuevo_rol = int(input("Seleccione nuevo rol: "))
                    if nuevo_rol in roles:
                        u.rol = roles[nuevo_rol]
                        print("Rol actualizado correctamente.")
                        return
            print("Usuario no encontrado o rol inválido.")
        except ValueError:
            print("Entrada inválida.")

    # Permite al usuario cambiar su nombre y/o contraseña.
    # La contraseña nueva también se valida según las reglas de seguridad.
    @staticmethod
    def editar_datos_personales(usuario):
        print("\n--- Editar datos personales ---")
        nuevo_nombre = input("Nuevo nombre (dejar en blanco para mantener actual): ")
        nueva_contrasena = input("Nueva contraseña (dejar en blanco para mantener actual): ")

        if nuevo_nombre.strip():
            usuario.nombre = nuevo_nombre

        if nueva_contrasena.strip():
            if Herramientas.validar_contrasena(nueva_contrasena):
                usuario.contrasena = nueva_contrasena
            else:
                print("Contraseña no cumple los requisitos. No se actualizo.")

        print("Datos actualizados.")

    # Cuenta cuántos usuarios hay por cada tipo de rol y muestra un resumen.
    @staticmethod
    def mostrar_resumen_roles(usuarios):
        print("\n--- Resumen de usuarios por rol ---")
        conteo = {}
        for u in usuarios:
            rol = u.rol.nombre
            conteo[rol] = conteo.get(rol, 0) + 1
        for rol, cantidad in conteo.items():
            print(f"{rol}: {cantidad}")
