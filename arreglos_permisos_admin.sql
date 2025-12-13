USE saas_firewall_db;
-- crear/asegurar rol_admin
CREATE USER IF NOT EXISTS 'rol_admin'@'localhost' IDENTIFIED BY 'drag0na';
ALTER USER 'rol_admin'@'localhost' IDENTIFIED BY 'drag0na';
GRANT ALL PRIVILEGES ON saas_firewall_db.* TO 'rol_admin'@'localhost';

-- crear/asegurar rol_analista (privilegios de lectura/ejecución)
CREATE USER IF NOT EXISTS 'rol_analista'@'localhost' IDENTIFIED BY 'mant1cora';
ALTER USER 'rol_analista'@'localhost' IDENTIFIED BY 'mant1cora';
GRANT SELECT, EXECUTE ON saas_firewall_db.* TO 'rol_analista'@'localhost';

FLUSH PRIVILEGES;
