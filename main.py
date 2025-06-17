from modelos import Rol, Usuario
from usuario import (
    registrar_usuario,
    listar_usuarios,
    eliminar_usuario,
    cambiar_rol,
    editar_datos_personales,
    mostrar_resumen_roles
)
from autentificacion import login

roles = {
    1: Rol(1, "administrador"),
    2: Rol(2, "usuario_estandar")
}

usuarios = []
contador_id = 1

usuarios.append(Usuario(contador_id, "Admin", "admin", "Admin1234", roles[1]))
contador_id += 1

# Menú exclusivo para usuarios administradores.
# Permite listar usuarios, cambiar roles, eliminar usuarios, ver resumen de roles o cerrar sesión.
def menu_admin():
    while True:
        print("\n======================================")
        print("           MENÚ ADMINISTRADOR         ")
        print("======================================")
        print("1. Listar usuarios")
        print("2. Cambiar rol de usuario")
        print("3. Eliminar usuario")
        print("4. Ver resumen de roles")
        print("5. Cerrar sesión")
        print("--------------------------------------")
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            listar_usuarios(usuarios)
        elif opcion == "2":
            cambiar_rol(usuarios, roles)
        elif opcion == "3":
            eliminar_usuario(usuarios)
        elif opcion == "4":
            mostrar_resumen_roles(usuarios)
        elif opcion == "5":
            break
        else:
            print("Opcion inválida. Intente nuevamente.")
        
        input("\nPresione Enter para volver al menú...")

# Menú para usuarios estándar.
# Permite ver sus propios datos, editar nombre o contraseña, o cerrar sesión.
def menu_usuario(usuario):
    while True:
        print("\n======================================")
        print(f"     BIENVENIDO, {usuario.nombre.upper()}        ")
        print("======================================")
        print("1. Ver mis datos")
        print("2. Editar mis datos")
        print("3. Cerrar sesión")
        print("--------------------------------------")
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            print("\n---------- TUS DATOS PERSONALES ----------")
            print(f"ID:        {usuario.id}")
            print(f"Usuario:   {usuario.usuario}")
            print(f"Nombre:    {usuario.nombre}")
            print(f"Rol:       {usuario.rol.nombre}")
            print("------------------------------------------")
        elif opcion == "2":
            editar_datos_personales(usuario)
        elif opcion == "3":
            break
        else:
            print("Opción inválida. Intente nuevamente.")  
        
        input("\nPresione Enter para volver al menú...")


# Función principal que se ejecuta al iniciar el programa.
# Muestra un menú inicial para iniciar sesión, registrarse o salir del sistema.
# Según el rol del usuario logueado, lo dirige al menú correspondiente.
def main():
    global contador_id
    while True:
        print("\n===========================================")
        print("     BIBLIOTECA DIGITAL CÓRDOBA USUARIOS    ")
        print("===========================================")
        print("1. Iniciar sesion")
        print("2. Registrarse")
        print("3. Salir")
        print("--------------------------------------")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            u = input("Usuario: ")
            c = input("Contraseña: ")
            usuario_actual = login(u, c, usuarios)
            if usuario_actual:
                if usuario_actual.rol.id == 1:
                    menu_admin()
                else:
                    menu_usuario(usuario_actual)
            else:
                print("Credenciales incorrectas. Intente nuevamente.")

        elif opcion == "2":
            contador_id = registrar_usuario(usuarios, roles, contador_id)

        elif opcion == "3":
            print("Gracias por usar el sistema. Hasta luego.")
            break
        else:
            print("Opcion inválida. Intente nuevamente.")

if __name__ == "__main__":
    main()
