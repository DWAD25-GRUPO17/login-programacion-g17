USE abpturismo;

-- Crear nueva persona
INSERT INTO persona (nombre, apellido, email, direccion, telefono)
VALUES ('Camila', 'Fernández', 'cami.fernandez2025@gmail.com', 'Av. Colón 789', '3513344566');

-- Crear usuario relacionado con esa persona
INSERT INTO usuario (id_persona, nombre_usuario, contrasena, rol)
VALUES (
    (SELECT id_persona FROM persona WHERE email = 'cami.fernandez2025@gmail.com'),
    'CamiFdez',
    'ClaveCamila2025',
    'admin');

-- Ver todos los usuarios actuales
SELECT * FROM usuario;

-- Actualizar contraseña de ese usuario
UPDATE usuario
SET contrasena = 'AdminClaveSegura2025'
WHERE nombre_usuario = 'CamiFdez';

-- Eliminar solo el usuario (conserva los datos de persona)
DELETE FROM usuario
WHERE nombre_usuario = 'CamiFdez';
