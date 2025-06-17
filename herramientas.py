class Herramientas:
    @staticmethod
    def validar_contrasena(contrasena):
        if len(contrasena) < 8:
            return False
        tiene_mayuscula = any(c.isupper() for c in contrasena)
        tiene_numero = any(c.isdigit() for c in contrasena)
        return tiene_mayuscula and tiene_numero

    @staticmethod
    def confirmar_accion(mensaje):
        confirmacion = input(f"{mensaje} (s/n): ").lower()
        return confirmacion == 's'
