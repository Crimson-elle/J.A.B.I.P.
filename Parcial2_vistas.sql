USE saas_firewall_db;
-- La Vista_1 es para que los usuarios vean y/o cambien sus datos
CREATE VIEW Vista_1 AS
SELECT nombre_usuario, contrasena_hash, email, fecha_nacimiento, contacto
FROM Usuarios;

-- Permisos (La lógica de actualización la gestiona la aplicación Python, pero el rol necesita el permiso)
GRANT SELECT ON saas_firewall_db.Vista_1 TO 'rol_invitado'@'localhost';
GRANT SELECT ON saas_firewall_db.Vista_1 TO 'rol_analista'@'localhost';
GRANT UPDATE (nombre_usuario, contrasena_hash, email, fecha_nacimiento, contacto) ON saas_firewall_db.Usuarios TO 'rol_invitado'@'localhost';
-- Nota: Se otorga UPDATE directamente a la tabla para que el código de Python pueda ejecutarlo.

-- La Vista_2 era para agregar nuevos usuarios pero se maneja con los permisos del rol_ananlista
-- La Vista_3 era para que un usuario vea datos de sus logs. Esto requiere que el código Python filtre los logs por el id_usuario_origen del empleado conectado.


-- La Vista_4 es para el invitado vea su IP
CREATE VIEW Vista_4 AS
SELECT
    U.id_usuario,
    U.nombre_usuario,
    D.nombre_activo AS 'Dispositivo_Activo',
    I.direccion_ip,
    I.estado AS 'Estado_IP'
FROM Usuarios U
JOIN Dispositivos D ON U.id_usuario = D.id_responsable -- El usuario es responsable del dispositivo
JOIN IPs I ON D.id_dispositivo = I.id_dispositivo;     -- El dispositivo tiene una IP asignada
GRANT SELECT ON saas_firewall_db.Vista_4 TO 'rol_invitado'@'localhost';


