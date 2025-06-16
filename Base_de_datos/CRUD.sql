USE ProyectoABP;

INSERT INTO Usuario (id_rol, nombre, email, contrasena)
SELECT id_rol, 'Juan Pérez', 'juan.perez@mail.com', 'juan1234'
FROM Rol
WHERE nombre_rol = 'usuario_estandar'
AND NOT EXISTS (
    SELECT 1 FROM Usuario WHERE email = 'juan.perez@mail.com'
);

SELECT U.id_usuario, U.nombre, U.email, R.nombre_rol
FROM Usuario U
JOIN Rol R ON U.id_rol = R.id_rol;

SELECT * FROM Usuario WHERE id_usuario = 1;

UPDATE Usuario
SET nombre = 'Juan P. González',
    email = 'juan.gonzalez@mail.com'
WHERE id_usuario = 1;

UPDATE Usuario
SET id_rol = (SELECT id_rol FROM Rol WHERE nombre_rol = 'admin')
WHERE id_usuario = 1;

DELETE FROM Usuario
WHERE id_usuario = 1;

SELECT U.id_usuario, U.nombre, U.email, R.nombre_rol
FROM Usuario U
JOIN Rol R ON U.id_rol = R.id_rol;
