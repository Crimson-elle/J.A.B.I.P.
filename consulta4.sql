USE saas_firewall_db;
SELECT
    R.nombre_rol,
    U.nombre_usuario,
    LF.fecha_log,
    LF.puerto_destino
FROM Logs_Firewall LF
JOIN Usuarios U ON LF.id_usuario_origen = U.id_usuario
JOIN Roles R ON U.id_rol = R.id_rol
WHERE
    LF.accion = 'PERMITIDO'
    AND R.nombre_rol = 'Analista' -- Filtrar por el rol que se desee
ORDER BY
    LF.fecha_log DESC
LIMIT 10;