# Biblioteca Digital Comunitaria:

Sistema en Python para gestionar usuarios mediante consola, con roles de "Administrador" y "Usuario Estándar". Incluye autenticación, menús interactivos, y funciones de registro, edición, eliminación y listados.

## Ejecución

1. Requiere Python 3.8+
2. Ejecutar desde consola:

```bash
python main.py
```

## Usuario predefinido

- Usuario: `admin`
- Contraseña: `Admin1234`

## Menú principal

1. Iniciar sesión
2. Registrarse
3. Salir

## Funciones según rol

**Administrador:**

- Listar usuarios
- Cambiar rol
- Eliminar usuarios
- Ver resumen de roles

**Usuario Estándar:**

- Ver/editar sus datos

## Validaciones

- Contraseña debe tener al menos 8 caracteres, una mayúscula y un número.

## Estructura de Archivos

- `main.py`: Inicio y menús
- `autentificacion.py`: Registro e inicio de sesión
- `usuario.py`: Funciones CRUD
- `modelos.py`: Clases `Usuario` y `Rol`
- `utilidades.py`: Validaciones

## Comentarios Finales

El código está comentado para facilitar su comprensión.

> Proyecto para fines académicos. Mejoras sugeridas: encapsulación completa, integración con base de datos, y logs de actividad.

## Aclaraciones

- El integrante **Juan Pablo Ramallo** participó en la realización del proyecto, sin embargo debido a unos inconvenientes técnicos no pudo realizar un commit en esta ocasión.
- Añadimos los archivos de la base de datos (.sql) para facilitar el acceso de los mismos.
