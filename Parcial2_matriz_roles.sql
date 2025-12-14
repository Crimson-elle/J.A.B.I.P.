CREATE USER 'rol_admin'@'localhost' IDENTIFIED BY 'drag0na';
CREATE USER 'rol_analista'@'localhost' IDENTIFIED BY 'mant1cora';
CREATE USER 'rol_invitado'@'localhost' IDENTIFIED BY 'esfing3';

GRANT ALL PRIVILEGES ON saas_firewall_db.* TO 'rol_admin'@'localhost';

GRANT SELECT ON saas_firewall_db.* TO 'rol_analista'@'localhost';
GRANT INSERT ON saas_firewall_db.Alertas TO 'rol_analista'@'localhost'; 
GRANT INSERT, UPDATE ON saas_firewall_db.Reportes TO 'rol_analista'@'localhost'; 
GRANT INSERT ON saas_firewall_db.Auditoria TO 'rol_analista'@'localhost'; 

GRANT SELECT ON saas_firewall_db.Usuarios TO 'rol_invitado'@'localhost';
GRANT SELECT ON saas_firewall_db.Roles TO 'rol_invitado'@'localhost';
GRANT SELECT ON saas_firewall_db.IPs TO 'rol_invitado'@'localhost';
GRANT INSERT ON saas_firewall_db.Alertas TO 'rol_invitado'@'localhost';
GRANT SELECT ON saas_firewall_db.Vista_1 TO 'rol_invitado'@'localhost';
GRANT SELECT ON saas_firewall_db.Vista_4 TO 'rol_invitado'@'localhost';
GRANT EXECUTE ON PROCEDURE saas_firewall_db.SP_ObtenerLogsPorUsuario TO 'rol_invitado'@'localhost';

FLUSH PRIVILEGES;

