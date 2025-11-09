USE saas_firewall_db;
SELECT
    A.tipo_alerta,
    COUNT(A.id_alerta) AS total_bloqueos,
    U_analista.nombre_usuario AS analista_asignado,
    MAX(A.fecha_alerta) AS ultimo_bloqueo_registrado
FROM Alertas A
JOIN Logs_Firewall LF ON A.id_log = LF.id_log
JOIN Usuarios U_analista ON A.id_analista_asignado = U_analista.id_usuario
WHERE
    A.estado = 'Pendiente' 
GROUP BY
    A.tipo_alerta, U_analista.nombre_usuario
ORDER BY
    total_bloqueos DESC;