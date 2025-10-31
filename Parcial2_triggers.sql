DELIMITER //
CREATE TRIGGER trg_auditoria_actualizacion_usuario
AFTER UPDATE ON Usuarios
FOR EACH ROW
BEGIN
    IF NEW.nombre_usuario <> OLD.nombre_usuario OR NEW.contrasena_hash <> OLD.contrasena_hash THEN
        INSERT INTO Auditoria (fecha, tabla_afectada, accion_realizada, detalle)
        VALUES (NOW(), 'Usuarios', 'UPDATE', CONCAT('Datos sensibles (Nombre/Contraseña) modificados para el usuario ID: ', NEW.id_usuario));
    END IF;
END; //
DELIMITER ;


DELIMITER //
CREATE TRIGGER trg_auditoria_log_insert
AFTER INSERT ON Logs_Firewall
FOR EACH ROW
BEGIN
    INSERT INTO Auditoria (fecha, tabla_afectada, accion_realizada, detalle, id_usuario_sistema)
    VALUES (NOW(), 'Logs_Firewall', 'INSERT', CONCAT('Log de Firewall #', NEW.id_log, ' insertado. Acción: ', NEW.accion), NEW.id_usuario_analista);
  
END; //
DELIMITER ;


DELIMITER //
CREATE TRIGGER trg_auditoria_alerta_insert
AFTER INSERT ON Alertas
FOR EACH ROW
BEGIN
    INSERT INTO Auditoria (fecha, tabla_afectada, accion_realizada, detalle, id_usuario_sistema)
    VALUES (
        NOW(),
        'Alertas',
        'INSERT',
        CONCAT('Nueva Alerta #', NEW.id_alerta, ' creada. Tipo: ', NEW.tipo_alerta, '. Gravedad: ', NEW.gravedad),
        NEW.id_analista_asignado -- El analista asignado es quien inició el proceso o el sistema.
    );
END; //
DELIMITER ;

DELIMITER //
CREATE TRIGGER trg_auditoria_reporte_insert
AFTER INSERT ON Reportes
FOR EACH ROW
BEGIN
    INSERT INTO Auditoria (fecha, tabla_afectada, accion_realizada, detalle, id_usuario_sistema)
    VALUES (
        NOW(),
        'Reportes',
        'INSERT',
        CONCAT('Nuevo Reporte #', NEW.id_reporte, ' creado. Título: ', NEW.titulo),
        NEW.id_usuario_creador
    );
END; //
DELIMITER ;


DELIMITER //
CREATE TRIGGER trg_auditoria_reporte_actualizado
AFTER UPDATE ON Reportes
FOR EACH ROW
BEGIN
    INSERT INTO Auditoria (fecha, tabla_afectada, accion_realizada, detalle, id_usuario_sistema)
    VALUES (NOW(), 'Reportes', 'UPDATE', CONCAT('Reporte ID: ', NEW.id_reporte, ' modificado. Título: ', NEW.titulo), NEW.id_usuario_creador);
   
END; //
DELIMITER ;

