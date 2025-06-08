-- Crear la base de datos
CREATE DATABASE IF NOT EXISTS abpturismo;
USE abpturismo;

-- Tabla generalizada: Persona
CREATE TABLE persona (
    id_persona INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL,
    apellido VARCHAR(50) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    direccion VARCHAR(100),
    telefono VARCHAR(20)
);

-- Tabla: Ente Administrador
CREATE TABLE ente_administrador (
    id_admin INT AUTO_INCREMENT PRIMARY KEY,
    id_persona INT NOT NULL,
    FOREIGN KEY (id_persona) REFERENCES persona(id_persona)
);

-- Tabla: Dueños
CREATE TABLE dueno (
    id_dueno INT AUTO_INCREMENT PRIMARY KEY,
    id_persona INT NOT NULL,
    FOREIGN KEY (id_persona) REFERENCES persona(id_persona)
);

-- Tabla: Turistas
CREATE TABLE turista (
    id_turista INT AUTO_INCREMENT PRIMARY KEY,
    id_persona INT NOT NULL,
    FOREIGN KEY (id_persona) REFERENCES persona(id_persona)
);

-- Tabla: Alojamientos
CREATE TABLE alojamiento (
    id_alojamiento INT AUTO_INCREMENT PRIMARY KEY,
    id_dueno INT NOT NULL,
    direccion VARCHAR(100) NOT NULL,
    tipo VARCHAR(50),
    precio DECIMAL(10,2),
    capacidad INT,
    descripcion TEXT,
    FOREIGN KEY (id_dueno) REFERENCES dueno(id_dueno)
);

-- Tabla: Reservas
CREATE TABLE reserva (
    id_reserva INT AUTO_INCREMENT PRIMARY KEY,
    id_turista INT NOT NULL,
    id_alojamiento INT NOT NULL,
    fecha_inicio DATE NOT NULL,
    fecha_fin DATE NOT NULL,
    estado ENUM('Pendiente', 'Confirmado', 'Cancelado', 'Finalizado') DEFAULT 'Pendiente',
    FOREIGN KEY (id_turista) REFERENCES turista(id_turista),
    FOREIGN KEY (id_alojamiento) REFERENCES alojamiento(id_alojamiento)
);

CREATE TABLE usuario (
    id_usuario INT AUTO_INCREMENT PRIMARY KEY,
    id_persona INT NOT NULL,
    nombre_usuario VARCHAR(50) NOT NULL UNIQUE,
    contrasena VARCHAR(100) NOT NULL,
    rol ENUM('turista', 'dueno', 'admin') NOT NULL,
    FOREIGN KEY (id_persona) REFERENCES persona(id_persona)
);