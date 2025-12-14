USE saas_firewall_db;

GRANT SELECT ON saas_firewall_db.Usuarios TO 'rol_invitado'@'localhost';
GRANT SELECT ON saas_firewall_db.Roles TO 'rol_invitado'@'localhost';
GRANT SELECT ON saas_firewall_db.IPs TO 'rol_invitado'@'localhost';
GRANT INSERT ON saas_firewall_db.Alertas TO 'rol_invitado'@'localhost';

GRANT SELECT ON saas_firewall_db.Vista_1 TO 'rol_invitado'@'localhost';
GRANT SELECT ON saas_firewall_db.Vista_4 TO 'rol_invitado'@'localhost';

GRANT EXECUTE ON PROCEDURE saas_firewall_db.SP_ObtenerLogsPorUsuario TO 'rol_invitado'@'localhost';

FLUSH PRIVILEGES;

SELECT 'Permisos aplicados correctamente' AS Resultado;
