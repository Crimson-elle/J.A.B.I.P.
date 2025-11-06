CREATE DATABASE IF NOT EXISTS SAAS_Firewall_DB;
USE SAAS_Firewall_DB;

CREATE TABLE Roles (
    id_rol INT PRIMARY KEY AUTO_INCREMENT,
    nombre_rol VARCHAR(50) NOT NULL UNIQUE
);

CREATE TABLE Usuarios (
    id_usuario INT PRIMARY KEY AUTO_INCREMENT,
    nombre_usuario VARCHAR(100) NOT NULL UNIQUE,
    contrasena_hash VARCHAR(255) NOT NULL, 
    email VARCHAR(100) UNIQUE,
    cargo VARCHAR(100),
    fecha_nacimiento DATE,
    contacto VARCHAR(100),
    id_rol INT NOT NULL,
    FOREIGN KEY (id_rol) REFERENCES Roles(id_rol)
);

CREATE TABLE Dispositivos (
    id_dispositivo INT PRIMARY KEY AUTO_INCREMENT,
    nombre_activo VARCHAR(150) NOT NULL UNIQUE, 
    tipo_dispositivo VARCHAR(50), 
    ubicacion_fisica VARCHAR(150),
    id_responsable INT,    
    FOREIGN KEY (id_responsable) REFERENCES Usuarios(id_usuario)
);

CREATE TABLE IPs (
    id_ip INT PRIMARY KEY AUTO_INCREMENT,
    direccion_ip VARCHAR(45) NOT NULL UNIQUE,
    estado VARCHAR(50), 
    fecha_ultimo_visto DATETIME,
    id_dispositivo INT, 
    FOREIGN KEY (id_dispositivo) REFERENCES Dispositivos(id_dispositivo)
);

CREATE TABLE Logs_Firewall (
    id_log INT PRIMARY KEY AUTO_INCREMENT,
    fecha_log DATETIME NOT NULL,
    accion VARCHAR(50), 
    puerto_destino INT,
    id_ip INT, 
    id_usuario_origen INT, 
    id_usuario_analista INT, 
    FOREIGN KEY (id_ip) REFERENCES IPs(id_ip),
    FOREIGN KEY (id_usuario_origen) REFERENCES Usuarios(id_usuario),
    FOREIGN KEY (id_usuario_analista) REFERENCES Usuarios(id_usuario)
);

CREATE TABLE Alertas (
    id_alerta INT PRIMARY KEY AUTO_INCREMENT,
    tipo_alerta VARCHAR(100) NOT NULL,
    fecha_alerta DATETIME NOT NULL,
    gravedad ENUM('Baja', 'Media', 'Alta', 'Crítica') NOT NULL,
    estado ENUM('Pendiente', 'En Progreso', 'Cerrada') NOT NULL DEFAULT 'Pendiente',
    id_log INT UNIQUE, 
    id_analista_asignado INT,
    FOREIGN KEY (id_log) REFERENCES Logs_Firewall(id_log),
    FOREIGN KEY (id_analista_asignado) REFERENCES Usuarios(id_usuario)
);

CREATE TABLE Reportes (
    id_reporte INT PRIMARY KEY AUTO_INCREMENT,
    fecha_creacion DATE NOT NULL,
    titulo VARCHAR(50) NOT NULL,
    contenido TEXT,
    id_usuario_creador INT NOT NULL,
    FOREIGN KEY (id_usuario_creador) REFERENCES Usuarios(id_usuario)
);

CREATE TABLE Auditoria (
    id_auditoria INT PRIMARY KEY AUTO_INCREMENT,
    fecha DATETIME NOT NULL,
    tabla_afectada VARCHAR(100), 
    accion_realizada VARCHAR(100), 
    detalle TEXT,
    id_usuario_sistema INT,     
    FOREIGN KEY (id_usuario_sistema) REFERENCES Usuarios(id_usuario)
);

ALTER TABLE Dispositivos
ADD COLUMN direccion_mac VARCHAR(17) AFTER id_responsable;

ALTER TABLE Dispositivos
ADD COLUMN sistema_operativo VARCHAR(100) AFTER direccion_mac;

ALTER TABLE Dispositivos
ADD COLUMN criticidad ENUM('Alta', 'Media', 'Baja') AFTER sistema_operativo;

