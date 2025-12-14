USE saas_firewall_db;

CREATE VIEW Vista_1 AS
SELECT nombre_usuario, contrasena_hash, email, fecha_nacimiento, contacto
FROM Usuarios;


GRANT SELECT ON saas_firewall_db.Vista_1 TO 'rol_invitado'@'localhost';
GRANT SELECT ON saas_firewall_db.Vista_1 TO 'rol_analista'@'localhost';
GRANT UPDATE (nombre_usuario, contrasena_hash, email, fecha_nacimiento, contacto) ON saas_firewall_db.Usuarios TO 'rol_invitado'@'localhost';

CREATE VIEW Vista_4 AS
SELECT
    U.id_usuario,
    U.nombre_usuario,
    D.nombre_activo AS 'Dispositivo_Activo',
    I.direccion_ip,
    I.estado AS 'Estado_IP'
FROM Usuarios U
JOIN Dispositivos D ON U.id_usuario = D.id_responsable
JOIN IPs I ON D.id_dispositivo = I.id_dispositivo;     
GRANT SELECT ON saas_firewall_db.Vista_4 TO 'rol_invitado'@'localhost';

DROP VIEW IF EXISTS Vista_4;

CREATE VIEW Vista_4 AS
SELECT
    COALESCE(U.nombre_usuario, 'SIN RESPONSABLE') AS nombre_usuario,
    COALESCE(D.nombre_activo, 'SIN ASIGNAR') AS Dispositivo_Activo,
    I.direccion_ip,
    I.estado AS Estado_IP
FROM IPs I
LEFT JOIN Dispositivos D ON I.id_dispositivo = D.id_dispositivo 
LEFT JOIN Usuarios U ON D.id_responsable = U.id_usuario; 
