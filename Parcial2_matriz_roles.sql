CREATE USER 'rol_admin'@'localhost' IDENTIFIED BY 'drag0na';
CREATE USER 'rol_analista'@'localhost' IDENTIFIED BY 'mant1cora';
CREATE USER 'rol_invitado'@'localhost' IDENTIFIED BY 'esfing3';
-- Si la aplicación se conecta desde otro host (ej. 192.168.1.10) o cualquier host:
-- CREATE USER 'rol_admin'@'%' IDENTIFIED BY 'drag0na';

GRANT ALL PRIVILEGES ON saas_firewall_db.* TO 'rol_admin'@'localhost';

GRANT SELECT ON saas_firewall_db.* TO 'rol_analista'@'localhost';
GRANT INSERT ON saas_firewall_db.Alertas TO 'rol_analista'@'localhost'; 
GRANT INSERT, UPDATE ON saas_firewall_db.Reportes TO 'rol_analista'@'localhost'; 
GRANT INSERT ON saas_firewall_db.Auditoria TO 'rol_analista'@'localhost'; 

-- GRANT INSERT ON saas_firewall_db.Logs_Firewall TO 'rol_analista'@'localhost';  <<Este es un permiso que no sé si dejar>>


