USE saas_firewall_db;
SELECT
    I.direccion_ip,
    I.estado AS estado_actual,
    U.nombre_usuario,
    COUNT(DISTINCT LF.puerto_destino) AS total_puertos_diferentes
FROM Logs_Firewall LF
JOIN IPs I ON LF.id_ip = I.id_ip
JOIN Usuarios U ON LF.id_usuario_origen = U.id_usuario
WHERE
    
    LF.fecha_log >= DATE_SUB(NOW(), INTERVAL 60 DAY)
    AND LF.accion IN ('BLOQUEADO', 'PERMITIDO')
GROUP BY
    I.direccion_ip, I.estado, U.nombre_usuario
HAVING
    COUNT(DISTINCT LF.puerto_destino) >= 2
ORDER BY
    total_puertos_diferentes DESC;