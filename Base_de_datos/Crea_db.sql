CREATE DATABASE ProyectoABP;
USE ProyectoABP;

-- Se crea la base de datos para el proyecto ABP y se selecciona

CREATE TABLE Rol (
    id_rol      INT AUTO_INCREMENT PRIMARY KEY,
    nombre_rol  VARCHAR(30) UNIQUE NOT NULL
);

-- Se crea la tabla Rol, con clave primaria, asi cada ingreso tiene un identificador 
-- único, y se utiliza auto_increment para que cada id_rol tenga un id sequencial cada
-- vez que se genere un registro. se usa varchar(30) unique not null, lo que obliga
-- a que las celdas tengan contenido, y que los valores no se repitan

CREATE TABLE Permiso (
    id_permiso      INT AUTO_INCREMENT PRIMARY KEY,
    nombre_permiso  VARCHAR(50) UNIQUE NOT NULL
);

-- Lo mismo que Rol pero con mas capacidad de caracteres, aca se almacenan los conjuntos
-- de permisos

CREATE TABLE Rol_Permiso (
    id_rol     INT,
    id_permiso INT,
    PRIMARY KEY (id_rol, id_permiso),
    FOREIGN KEY (id_rol)     REFERENCES Rol(id_rol),
    FOREIGN KEY (id_permiso) REFERENCES Permiso(id_permiso)
);

-- Conecta roles y permisos, permitiendo que un rol tenga varios permisos y un permiso
-- pertenezca a varios roles, y se usa una PK compuesta, para que la relacion rol-permiso
-- sea unica

CREATE TABLE Usuario (
    id_usuario  INT AUTO_INCREMENT PRIMARY KEY,
    id_rol      INT NOT NULL,
    nombre      VARCHAR(100) NOT NULL,
    email       VARCHAR(255) UNIQUE NOT NULL,
    contrasena  VARCHAR(255) NOT NULL,
    FOREIGN KEY (id_rol) REFERENCES Rol(id_rol)
);

-- id_usuario se autoincrementa al igual que los roles, y se usa una FK para id_rol
-- para conectar cada usuario con un rol, email utiliza varchar(255) unique para evitar
-- registros duplicados, y contrasena se define como varchar(255) para acomodar el espacio
-- necesario

CREATE TABLE Historial_Acceso (
    id_acceso  INT AUTO_INCREMENT PRIMARY KEY,
    id_usuario INT NOT NULL,
    fecha_hora DATETIME DEFAULT CURRENT_TIMESTAMP,
    tipo_acceso ENUM('Login','Logout') NOT NULL,
    FOREIGN KEY (id_usuario) REFERENCES Usuario(id_usuario)
);

-- se registran los logueos de los usuarios, usando timestamps y el tipo de acceso que
-- solo pueden ser valor Login o Logout

INSERT INTO Rol (nombre_rol)
VALUES ('admin'), ('usuario_estandar');

-- Se agregan los valores de los roles, admin y usuario estandar (son unique asi que
-- no se pueden duplicar)

INSERT INTO Permiso (nombre_permiso)
VALUES ('VER_LISTADO_USUARIOS'),
       ('CREAR_USUARIO'),
       ('ELIMINAR_USUARIO'),
       ('CAMBIAR_ROL');
       
-- se registran algunos permisos de ejemplo (unique tambien, con VARCHAR(50) para que
-- puedan ser descriptivos brevemente)

INSERT INTO Rol_Permiso (id_rol, id_permiso)
SELECT (SELECT id_rol FROM Rol WHERE nombre_rol = 'admin'),
       id_permiso
FROM Permiso;

-- se le otorgan todos los permisos de "Permiso" al rol "admin"

INSERT INTO Rol_Permiso (id_rol, id_permiso)
SELECT (SELECT id_rol FROM Rol WHERE nombre_rol = 'usuario_estandar'),
       id_permiso
FROM Permiso
WHERE nombre_permiso = 'VER_LISTADO_USUARIOS';

-- consulta similar, pero le agrega solamente el permiso ver_listado_usuarios al usuario
-- estandar