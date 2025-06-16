from modelos import Usuario
from utilidades import validar_contrasena, confirmar_accion


def registrar_usuario(usuarios, roles, contador_id):
    print("\n--- Registro de nuevo usuario ---")
    nombre = input("Nombre completo: ")
    usuario = input("Nombre de usuario: ")
    contrasena = input("Contrasena (minimo 8 caracteres, con al menos una mayuscula y un numero): ")

    if not validar_contrasena(contrasena):
        print("Contrasena invalida. No cumple con los requisitos.")
        return contador_id

    if any(u.usuario == usuario for u in usuarios):
        print("El nombre de usuario ya existe.")
        return contador_id

    nuevo_usuario = Usuario(contador_id, nombre, usuario, contrasena, roles[2])
    usuarios.append(nuevo_usuario)
    print("Usuario registrado exitosamente.")
    return contador_id + 1

def listar_usuarios(usuarios):
    print("\n---------- LISTADO DE USUARIOS ----------")
    print(f"{'ID':<5}{'Nombre':<20}{'Usuario':<15}{'Rol':<15}")
    print("-" * 55)
    for u in usuarios:
        print(f"{u.id:<5}{u.nombre:<20}{u.usuario:<15}{u.rol.nombre:<15}")

def eliminar_usuario(usuarios):
    try:
        id_u = int(input("Ingrese el ID del usuario a eliminar: "))
        for u in usuarios:
            if u.id == id_u:
                if confirmar_accion(f"Seguro que desea eliminar al usuario '{u.usuario}'?"):
                    usuarios.remove(u)
                    print("Usuario eliminado.")
                return
        print("Usuario no encontrado.")
    except ValueError:
        print("ID invalido.")

def cambiar_rol(usuarios, roles):
    try:
        id_u = int(input("Ingrese el ID del usuario: "))
        for u in usuarios:
            if u.id == id_u:
                print("1 - Administrador\n2 - Usuario estandar")
                nuevo_rol = int(input("Seleccione nuevo rol: "))
                if nuevo_rol in roles:
                    u.rol = roles[nuevo_rol]
                    print("Rol actualizado correctamente.")
                    return
        print("Usuario no encontrado o rol invalido.")
    except ValueError:
        print("Entrada invalida.")

def editar_datos_personales(usuario):
    print("\n--- Editar datos personales ---")
    nuevo_nombre = input("Nuevo nombre (dejar en blanco para mantener actual): ")
    nueva_contrasena = input("Nueva contrasena (dejar en blanco para mantener actual): ")

    if nuevo_nombre.strip():
        usuario.nombre = nuevo_nombre

    if nueva_contrasena.strip():
        if validar_contrasena(nueva_contrasena):
            usuario.contrasena = nueva_contrasena
        else:
            print("Contrasena no cumple los requisitos. No se actualizo.")

    print("Datos actualizados.")

def mostrar_resumen_roles(usuarios):
    print("\n--- Resumen de usuarios por rol ---")
    conteo = {}
    for u in usuarios:
        rol = u.rol.nombre
        conteo[rol] = conteo.get(rol, 0) + 1
    for rol, cantidad in conteo.items():
        print(f"{rol}: {cantidad}")