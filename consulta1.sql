USE saas_firewall_db;
SELECT
    U.nombre_usuario,
    I.direccion_ip,
    COUNT(LF.id_log) AS total_intentos_fallidos
FROM Logs_Firewall LF
JOIN Usuarios U ON LF.id_usuario_origen = U.id_usuario
JOIN IPs I ON LF.id_ip = I.id_ip
WHERE
    LF.accion = 'BLOQUEADO'
GROUP BY
    U.nombre_usuario, I.direccion_ip
HAVING
    COUNT(LF.id_log) > 3
ORDER BY
    total_intentos_fallidos DESC;
 
