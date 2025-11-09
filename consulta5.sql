USE saas_firewall_db;
SELECT
    V4.nombre_usuario,
    V4.Dispositivo_Activo,
    V4.direccion_ip
FROM Vista_4 V4
WHERE
    V4.Estado_IP = 'Maliciosa';