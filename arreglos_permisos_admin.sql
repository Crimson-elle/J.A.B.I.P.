USE saas_firewall_db;
CREATE USER IF NOT EXISTS 'rol_admin'@'localhost' IDENTIFIED BY 'drag0na';
ALTER USER 'rol_admin'@'localhost' IDENTIFIED BY 'drag0na';
GRANT ALL PRIVILEGES ON saas_firewall_db.* TO 'rol_admin'@'localhost';

CREATE USER IF NOT EXISTS 'rol_analista'@'localhost' IDENTIFIED BY 'mant1cora';
ALTER USER 'rol_analista'@'localhost' IDENTIFIED BY 'mant1cora';
GRANT SELECT, EXECUTE ON saas_firewall_db.* TO 'rol_analista'@'localhost';

FLUSH PRIVILEGES;
