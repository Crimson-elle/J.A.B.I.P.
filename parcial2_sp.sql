DELIMITER //
CREATE PROCEDURE SP_ObtenerLogsPorUsuario (
    IN p_id_usuario INT
)
BEGIN
    SELECT
        LF.fecha_log,
        LF.accion,
        LF.puerto_destino,
        I.direccion_ip
    FROM Logs_Firewall LF
    JOIN IPs I ON LF.id_ip = I.id_ip
    WHERE LF.id_usuario_origen = p_id_usuario;
END //
DELIMITER ;

DELIMITER //
CREATE PROCEDURE SP_ProcesarNuevaAlerta (
    IN p_id_log INT,
    IN p_tipo_alerta VARCHAR(100),
    IN p_gravedad ENUM('Baja', 'Media', 'Alta', 'Crítica'),
    IN p_analista_id INT
)
BEGIN
    INSERT INTO Alertas (tipo_alerta, fecha_alerta, gravedad, estado, id_log, id_analista_asignado)
    VALUES (p_tipo_alerta, NOW(), p_gravedad, 'Pendiente', p_id_log, p_analista_id);

    INSERT INTO Auditoria (fecha, tabla_afectada, accion_realizada, detalle, id_usuario_sistema)
    VALUES (NOW(), 'Alertas', 'INSERT', CONCAT('Alerta #', LAST_INSERT_ID(), ' generada a partir de Log #', p_id_log), p_analista_id);

END //
DELIMITER ;

DELIMITER //
CREATE PROCEDURE SP_CambiarEstadoIP (
    IN p_direccion_ip VARCHAR(45),
    IN p_nuevo_estado VARCHAR(50),
    IN p_analista_id INT
)
BEGIN
    UPDATE IPs
    SET estado = p_nuevo_estado, fecha_ultimo_visto = NOW()
    WHERE direccion_ip = p_direccion_ip;

    INSERT INTO Auditoria (fecha, tabla_afectada, accion_realizada, detalle, id_usuario_sistema)
    VALUES (NOW(), 'IPs', 'UPDATE_ESTADO', CONCAT('IP ', p_direccion_ip, ' cambió a estado ', p_nuevo_estado), p_analista_id);
END //
DELIMITER ;


GRANT EXECUTE ON PROCEDURE saas_firewall_db.SP_ProcesarNuevaAlerta TO 'rol_analista'@'localhost';
GRANT EXECUTE ON PROCEDURE saas_firewall_db.SP_ProcesarNuevaAlerta TO 'rol_admin'@'localhost';
GRANT EXECUTE ON PROCEDURE saas_firewall_db.SP_CambiarEstadoIP TO 'rol_admin'@'localhost';
REVOKE EXECUTE ON PROCEDURE saas_firewall_db.SP_CambiarEstadoIP FROM 'rol_analista'@'localhost';
