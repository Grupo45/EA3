-- Selecciona la base de datos donde se ejecutarán las operaciones
USE ProyectoABP;

--INSERCIÓN DE USUARIO
-- Crea un nuevo usuario con rol 'usuario_estandar'
-- Verifica primero que no exista un usuario con el mismo email
-- La contraseña se almacena en texto plano (problema de seguridad)
INSERT INTO Usuario (id_rol, nombre, email, contrasena)
SELECT id_rol, 'Juan Pérez', 'juan.perez@mail.com', 'juan1234'
FROM Rol
WHERE nombre_rol = 'usuario_estandar'
AND NOT EXISTS (
    SELECT 1 FROM Usuario WHERE email = 'juan.perez@mail.com'
);

--CONSULTA DE USUARIOS CON SUS ROLES
-- Muestra todos los usuarios registrados
-- Incluye información del rol asociado a cada usuario
SELECT U.id_usuario, U.nombre, U.email, R.nombre_rol
FROM Usuario U
JOIN Rol R ON U.id_rol = R.id_rol;

-- Consulta específica del usuario con ID = 1
SELECT * FROM Usuario WHERE id_usuario = 1;

-- ACTUALIZACIÓN DE DATOS DEL USUARIO
-- Modifica el nombre y email del usuario con ID = 1
-- Ejemplo de operación UPDATE básica
UPDATE Usuario
SET nombre = 'Juan P. González',
    email = 'juan.gonzalez@mail.com'
WHERE id_usuario = 1;

--CAMBIO DE ROL DE USUARIO
-- Actualiza el rol del usuario con ID = 1 a 'admin'
-- Usa una subconsulta para obtener el ID del rol 'admin'
UPDATE Usuario
SET id_rol = (SELECT id_rol FROM Rol WHERE nombre_rol = 'admin')
WHERE id_usuario = 1;

-- ELIMINACIÓN DEL USUARIO con ID = 1
DELETE FROM Usuario
WHERE id_usuario = 1;

--CONSULTA FINAL DE USUARIOS
-- Muestra el estado actual de la tabla de usuarios
-- Permite verificar los cambios después de las operaciones CRUD
SELECT U.id_usuario, U.nombre, U.email, R.nombre_rol
FROM Usuario U
JOIN Rol R ON U.id_rol = R.id_rol;
