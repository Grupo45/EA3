# Verifica si una contraseña cumple con los requisitos mínimos de seguridad:
# debe tener más de 8 caracteres, al menos una mayúscula y un número.
def validar_contrasena(contrasena):
    if len(contrasena) < 8:
        return False
    tiene_mayuscula = any(c.isupper() for c in contrasena)
    tiene_numero = any(c.isdigit() for c in contrasena)
    return tiene_mayuscula and tiene_numero

# Pide al usuario una confirmación tipo "¿Está seguro? (s/n)".
# Devuelve True si responde 's', False en cualquier otro caso. 
# Usado en Eliminar Usuario.
def confirmar_accion(mensaje):
    confirmacion = input(f"{mensaje} (s/n): ").lower()
    return confirmacion == 's'
