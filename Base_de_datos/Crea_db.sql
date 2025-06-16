CREATE DATABASE ProyectoABP;
USE ProyectoABP;

CREATE TABLE Rol (
    id_rol      INT AUTO_INCREMENT PRIMARY KEY,
    nombre_rol  VARCHAR(30) UNIQUE NOT NULL
);

CREATE TABLE Permiso (
    id_permiso      INT AUTO_INCREMENT PRIMARY KEY,
    nombre_permiso  VARCHAR(50) UNIQUE NOT NULL
);

CREATE TABLE Rol_Permiso (
    id_rol     INT,
    id_permiso INT,
    PRIMARY KEY (id_rol, id_permiso),
    FOREIGN KEY (id_rol)     REFERENCES Rol(id_rol),
    FOREIGN KEY (id_permiso) REFERENCES Permiso(id_permiso)
);

CREATE TABLE Usuario (
    id_usuario  INT AUTO_INCREMENT PRIMARY KEY,
    id_rol      INT NOT NULL,
    nombre      VARCHAR(100) NOT NULL,
    email       VARCHAR(255) UNIQUE NOT NULL,
    contrasena  VARCHAR(255) NOT NULL,
    FOREIGN KEY (id_rol) REFERENCES Rol(id_rol)
);

CREATE TABLE Historial_Acceso (
    id_acceso  INT AUTO_INCREMENT PRIMARY KEY,
    id_usuario INT NOT NULL,
    fecha_hora DATETIME DEFAULT CURRENT_TIMESTAMP,
    tipo_acceso ENUM('Login','Logout') NOT NULL,
    FOREIGN KEY (id_usuario) REFERENCES Usuario(id_usuario)
);

INSERT INTO Rol (nombre_rol)
VALUES ('admin'), ('usuario_estandar');

INSERT INTO Permiso (nombre_permiso)
VALUES ('VER_LISTADO_USUARIOS'),
       ('CREAR_USUARIO'),
       ('ELIMINAR_USUARIO'),
       ('CAMBIAR_ROL');

INSERT INTO Rol_Permiso (id_rol, id_permiso)
SELECT (SELECT id_rol FROM Rol WHERE nombre_rol = 'admin'),
       id_permiso
FROM Permiso;

INSERT INTO Rol_Permiso (id_rol, id_permiso)
SELECT (SELECT id_rol FROM Rol WHERE nombre_rol = 'usuario_estandar'),
       id_permiso
FROM Permiso
WHERE nombre_permiso = 'VER_LISTADO_USUARIOS';

