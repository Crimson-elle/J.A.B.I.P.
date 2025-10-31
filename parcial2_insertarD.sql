USE SAAS_Firewall_DB;

INSERT INTO Roles (id_rol, nombre_rol) VALUES
(1, 'Administrador'),
(2, 'Analista'),
(3, 'Invitado');

INSERT INTO Usuarios (id_usuario, nombre_usuario, contrasena_hash, email, cargo, fecha_nacimiento, contacto, id_rol) VALUES
(1, 'admin_bd', 'HASH_ADMIN1', 'jefe.admin@lab.com', 'Administradora de BD', '1998-05-15', '(555) 100-2001', 1),
(2, 'admin_seg', 'HASH_ADMIN2', 'seg.admin@lab.com', 'Jefa de seguridad', '1999-11-22', '(555) 100-2002', 1),
(3, 'analista_a', 'HASH_ANL3', 'analista.a@lab.com', 'Analista Senior', '1994-01-30', '(555) 100-2003', 2),
(4, 'analista_b', 'HASH_ANL4', 'analista.b@lab.com', 'Analista Junior', '1998-07-19', '(555) 100-2004', 2),
(5, 'analista_c', 'HASH_ANL5', 'analista.c@lab.com', 'Analista Turno Noche', '1997-04-10', '(555) 100-2005', 2),
(6, 'analista_d', 'HASH_ANL6', 'analista.d@lab.com', 'Analista de Reportes', '1995-12-05', '(555) 100-2006', 2),
(7, 'cientifico_1', 'HASH_CTC1', 'c1@lab.com', 'Investigador Principal', '1975-03-01', '(555) 100-2007', 3),
(8, 'cientifico_2', 'HASH_CTC2', 'c2@lab.com', 'Asistente de Investigación', '1984-06-25', '(555) 100-2008', 3),
(9, 'cientifico_3', 'HASH_CTC3', 'c3@lab.com', 'Técnico de Laboratorio', '1993-09-12', '(555) 100-2009', 3),
(10, 'adm_oficina_1', 'HASH_OF1', 'adm1@lab.com', 'Administración', '1995-02-14', '(555) 100-3010', 3),
(11, 'adm_oficina_2', 'HASH_OF2', 'adm2@lab.com', 'Contable', '1990-08-08', '(555) 100-3011', 3),
(12, 'adm_oficina_3', 'HASH_OF3', 'adm3@lab.com', 'Directorio', '1975-01-20', '(555) 100-3512', 3),
(13, 'adm_oficina_4', 'HASH_OF4', 'adm4@lab.com', 'Directorio', '1981-05-01', '(555) 100-3513', 3),
(14, 'cientifico_4', 'HASH_CTC4', 'c4@lab.com', 'Investigador Principal', '1984-10-10', '(555) 100-2010', 3),
(15, 'cientifico_5', 'HASH_CTC5', 'c5@lab.com', 'Asistente de Investigación', '1989-04-03', '(555) 100-2011', 3),
(16, 'cientifico_6', 'HASH_CTC6', 'c6@lab.com', 'Técnico de Laboratorio', '1994-07-07', '(555) 100-2012', 3),
(17, 'cientifico_7', 'HASH_CTC7', 'c7@lab.com', 'Técnico de Laboratorio', '1997-11-11', '(555) 100-2013', 3),
(18, 'invitado_18', 'HASH_INV18', 'i18@lab.com', 'Pasante', '2007-09-09', '(555) 100-4012', 3),
(19, 'invitado_19', 'HASH_INV19', 'i19@lab.com', 'Pasante', '2008-03-03', '(555) 100-4013', 3),
(20, 'invitado_20', 'HASH_INV20', 'i20@lab.com', 'Invitado General', '1999-08-18', '(555) 100-3514', 3),
(21, 'invitado_21', 'HASH_INV21', 'i21@lab.com', 'Invitado General', '2007-12-31', '(555) 100-3515', 3);

INSERT INTO Dispositivos (id_dispositivo, nombre_activo, tipo_dispositivo, ubicacion_fisica, id_responsable, direccion_mac, sistema_operativo, criticidad) VALUES
(1, 'Main Gateway/Firewall', 'Firewall/Router', 'Rack Principal', 2, '00:A0:C9:14:C8:29', 'Firewall OS', 'Alta'),
(2, 'Network Switch', 'Switch', 'Rack Principal', 1, '00:1A:2B:3C:4D:5E', 'Cisco IOS', 'Alta'),
(3, 'Internal DNS Server', 'Servidor', 'Sala Servidores', 1, '00:50:56:AB:CDEF', 'Linux CentOS', 'Alta'),
(4, 'Servidor de Archivos', 'Servidor', 'Sala Servidores', 1, '00:1C:42:00:00:01', 'Windows Server', 'Alta'),
(5, 'Backup Server', 'Servidor', 'Sala Servidores', 1, '00:0A:95:9D:68:16', 'Linux Ubuntu', 'Media'),
(6, 'PC Lider IT', 'Estación de Trabajo', 'Oficina IT', 2, 'A1:B2:C3:D4:E5:F6', 'Windows 11', 'Media'),
(7, 'PC Contable', 'Estación de Trabajo', 'Oficina Adm', 11, '11:22:33:44:55:66', 'Windows 10', 'Alta'), 
(8, 'PC IT Senior', 'Estación de Trabajo', 'Oficina IT', 3, 'B4:A1:C8:D0:E7:F1', 'Linux Mint', 'Media'), 
(9, 'PC Director General', 'Estación de Trabajo', 'Oficina Director', 12, '77:88:99:AA:BB:CC', 'MacOS', 'Alta'), 
(10, 'PC Administrativo', 'Estación de Trabajo', 'Oficina Adm', 10, 'C1:D2:E3:F4:A5:B6', 'Windows 10', 'Media'), 
(11, 'Secuenciador ADN', 'Instrumento Científico', 'Sala Frio', 7, '08:00:27:11:11:11', 'Proprietary OS', 'Media'), 
(12, 'Mass Spectrometer', 'Instrumento Científico', 'Sala Instrumentos', 8, '00:E0:4C:55:55:55', 'Windows 7 Embedded', 'Media'), 
(13, 'Centrifugo de Alto Rendimiento', 'Instrumento Científico', 'Laboratorio 3', 14, '00:0C:29:A1:A1:A1', 'Linux RHEL', 'Media'), 
(14, 'Lector Microplates', 'Instrumento Científico', 'Laboratorio 3', 15, 'B0:C1:D2:E3:F4:A5', 'Windows XP (Legacy)', 'Media'), 
(15, 'Environmental Chamber', 'IoT/Monitoreo', 'Laboratorio 2', 16, 'F1:E2:D3:C4:B5:A6', 'Firmware', 'Baja'), 
(16, 'Panel Control Edificio', 'IoT/Control', 'Mantenimiento', 2, 'D1:E2:F3:A4:B5:C6', 'Firmware', 'Baja'),
(17, 'Fotocopiadora 1', 'Impresora/MFD', 'Oficina Adm', 10, 'C0:C1:C2:C3:C4:C5', 'Firmware', 'Baja'),
(18, 'Fotocopiadora 2', 'Impresora/MFD', 'Laboratorio 1', 17, 'A0:A1:A2:A3:A4:A5', 'Firmware', 'Baja');

INSERT INTO IPs (id_ip, direccion_ip, estado, fecha_ultimo_visto, id_dispositivo) VALUES
(1, '192.168.10.1', 'Confiable', NOW(), 1),  -- Main Gateway
(2, '192.168.10.2', 'Confiable', NOW(), 2),  -- Network Switch
(3, '192.168.10.10', 'Confiable', NOW(), 3), -- Internal DNS Server
(4, '192.168.10.11', 'Confiable', NOW(), 4), -- Servidor de archivos
(5, '192.168.10.12', 'Confiable', NOW(), 5), -- Backup Server
(6, '192.168.10.20', 'Confiable', NOW(), 6),  -- PC Lider IT
(7, '192.168.10.21', 'Confiable', NOW(), 7),  -- PC Contable
(8, '192.168.10.22', 'Confiable', NOW(), 8),  -- PC IT Senior
(9, '192.168.10.23', 'Confiable', NOW(), 9),  -- PC Director General
(10, '192.168.10.30', 'Confiable', NOW(), 10), -- PC Administrativo
(11, '192.168.20.5', 'Confiable', NOW(), 11), -- Secuenciador ADN
(12, '192.168.20.6', 'Confiable', NOW(), 12), -- Mass Spectrometer
(13, '192.168.20.7', 'Confiable', NOW(), 13), -- Centrifugo
(14, '192.168.20.8', 'Confiable', NOW(), 14), -- Lector Microplates
(15, '192.168.20.9', 'Confiable', NOW(), 15), -- Environmental Chamber
(16, '192.168.30.2', 'Confiable', NOW(), 16), -- Panel control edificio
(17, '192.168.30.10', 'Confiable', NOW(), 17), -- Fotocopiadora 1
(18, '192.168.30.50', 'Confiable', NOW(), 18), -- Fotocopiadora 2
-- IPs Sospechosas / Bloqueadas / Externas (ID 19-21, NULL en Dispositivo)
(19, '192.168.55.1', 'Sospechosa', NOW(), NULL), -- IP Privada ajena
(20, '203.45.217.16', 'Maliciosa', NOW(), NULL), -- IP Externa conocida como maliciosa
(21, '38.51.31.49', 'Maliciosa', NOW(), NULL),  -- IP Externa desconocida
(22, '0.0.0.0', 'Maliciosa', NOW(), NULL), 
(23, '172.217.10.1', 'Sospechosa', NOW(), NULL),
(24, '1.1.1.1', 'Maliciosa', NOW(), NULL),     
(25, '45.76.100.200', 'Maliciosa', NOW(), NULL); 


INSERT INTO Logs_Firewall (id_log, fecha_log, accion, puerto_destino, id_ip, id_usuario_origen, id_usuario_analista) VALUES
(1, '2025-10-01 08:05:00', 'PERMITIDO', 80, 6, 2, NULL),    -- PC Lider IT (Admin_seg)
(2, '2025-10-01 09:10:00', 'PERMITIDO', 445, 4, 1, NULL),    -- Servidor Archivos (Admin BD)
(3, '2025-10-01 13:00:00', 'PERMITIDO', 443, 7, 11, NULL),   -- PC Contable
(4, '2025-10-01 17:45:00', 'PERMITIDO', 53, 3, 1, NULL),    -- DNS Server
(5, '2025-10-01 21:30:00', 'PERMITIDO', 22, 8, 3, NULL),    -- PC IT Senior
(6, '2025-10-02 08:35:00', 'PERMITIDO', 80, 9, 12, NULL),    -- PC Director
(7, '2025-10-02 10:40:00', 'PERMITIDO', 8080, 11, 7, NULL),  -- Secuenciador
(8, '2025-10-02 14:00:00', 'PERMITIDO', 25, 17, 10, NULL),   -- Fotocopiadora 1
(9, '2025-10-02 19:15:00', 'PERMITIDO', 445, 4, 10, NULL),   -- PC Adm accede a archivos
(10, '2025-10-03 09:05:00', 'PERMITIDO', 5000, 13, 14, NULL), -- Centrifugo
(11, '2025-10-03 12:20:00', 'PERMITIDO', 443, 7, 11, NULL),
(12, '2025-10-03 16:30:00', 'PERMITIDO', 22, 8, 3, NULL),
(13, '2025-10-03 20:00:00', 'PERMITIDO', 53, 16, 2, NULL),   -- Panel control edificio
(14, '2025-10-06 08:15:00', 'PERMITIDO', 80, 6, 2, NULL),
(15, '2025-10-06 09:40:00', 'PERMITIDO', 445, 4, 1, NULL),
(16, '2025-10-06 13:30:00', 'PERMITIDO', 443, 7, 11, NULL),
(17, '2025-10-06 17:50:00', 'PERMITIDO', 53, 3, 1, NULL),
(18, '2025-10-07 08:25:00', 'PERMITIDO', 80, 9, 12, NULL),
(19, '2025-10-07 10:50:00', 'PERMITIDO', 8080, 11, 7, NULL),
(20, '2025-10-07 14:30:00', 'PERMITIDO', 25, 17, 10, NULL),
(21, '2025-10-07 19:30:00', 'PERMITIDO', 445, 4, 10, NULL),
(22, '2025-10-08 09:10:00', 'PERMITIDO', 5000, 13, 14, NULL),
(23, '2025-10-08 12:40:00', 'PERMITIDO', 443, 7, 11, NULL),
(24, '2025-10-08 16:40:00', 'PERMITIDO', 22, 8, 3, NULL),
(25, '2025-10-08 21:00:00', 'PERMITIDO', 53, 16, 2, NULL),
(26, '2025-10-09 08:45:00', 'PERMITIDO', 80, 6, 2, NULL),
(27, '2025-10-09 11:15:00', 'PERMITIDO', 445, 4, 1, NULL),
(28, '2025-10-09 13:50:00', 'PERMITIDO', 443, 7, 11, NULL),
(29, '2025-10-09 18:00:00', 'PERMITIDO', 53, 3, 1, NULL),
(30, '2025-10-10 08:55:00', 'PERMITIDO', 80, 9, 12, NULL),
(31, '2025-10-10 11:30:00', 'PERMITIDO', 8080, 11, 7, NULL),
(32, '2025-10-10 15:00:00', 'PERMITIDO', 25, 17, 10, NULL),
(33, '2025-10-10 20:30:00', 'PERMITIDO', 445, 4, 10, NULL),
(34, '2025-10-13 08:08:00', 'PERMITIDO', 80, 6, 2, NULL),
(35, '2025-10-13 09:20:00', 'PERMITIDO', 445, 4, 1, NULL),
(36, '2025-10-13 13:10:00', 'PERMITIDO', 443, 7, 11, NULL),
(37, '2025-10-13 17:35:00', 'PERMITIDO', 53, 3, 1, NULL),
(38, '2025-10-14 08:40:00', 'PERMITIDO', 80, 9, 12, NULL),
(39, '2025-10-14 10:35:00', 'PERMITIDO', 8080, 11, 7, NULL),
(40, '2025-10-14 14:10:00', 'PERMITIDO', 25, 17, 10, NULL),
(41, '2025-10-14 19:00:00', 'PERMITIDO', 445, 4, 10, NULL),
(42, '2025-10-15 09:00:00', 'PERMITIDO', 5000, 13, 14, NULL),
(43, '2025-10-15 12:30:00', 'PERMITIDO', 443, 7, 11, NULL),
(44, '2025-10-15 16:20:00', 'PERMITIDO', 22, 8, 3, NULL),
(45, '2025-10-15 20:40:00', 'PERMITIDO', 53, 16, 2, NULL),
(46, '2025-10-16 08:30:00', 'PERMITIDO', 80, 6, 2, NULL),
(47, '2025-10-16 11:00:00', 'PERMITIDO', 445, 4, 1, NULL),
(48, '2025-10-16 13:40:00', 'PERMITIDO', 443, 7, 11, NULL),
(49, '2025-10-16 17:55:00', 'PERMITIDO', 53, 3, 1, NULL),
(50, '2025-10-17 08:50:00', 'PERMITIDO', 80, 9, 12, NULL),
(51, '2025-10-17 11:20:00', 'PERMITIDO', 8080, 11, 7, NULL),
(52, '2025-10-17 14:50:00', 'PERMITIDO', 25, 17, 10, NULL),
(53, '2025-10-17 20:20:00', 'PERMITIDO', 445, 4, 10, NULL),
(54, '2025-10-20 08:20:00', 'PERMITIDO', 80, 6, 2, NULL),
(55, '2025-10-20 09:30:00', 'PERMITIDO', 445, 4, 1, NULL),
(56, '2025-10-20 13:20:00', 'PERMITIDO', 443, 7, 11, NULL),
(57, '2025-10-20 17:40:00', 'PERMITIDO', 53, 3, 1, NULL),
(58, '2025-10-21 08:10:00', 'PERMITIDO', 80, 9, 12, NULL),
(59, '2025-10-21 10:25:00', 'PERMITIDO', 8080, 11, 7, NULL),
(60, '2025-10-21 14:20:00', 'PERMITIDO', 25, 17, 10, NULL),
(61, '2025-10-21 19:20:00', 'PERMITIDO', 445, 4, 10, NULL),
(62, '2025-10-22 09:00:00', 'PERMITIDO', 5000, 13, 14, NULL),
(63, '2025-10-22 12:50:00', 'PERMITIDO', 443, 7, 11, NULL),
(64, '2025-10-22 16:10:00', 'PERMITIDO', 22, 8, 3, NULL),
(65, '2025-10-22 20:50:00', 'PERMITIDO', 53, 16, 2, NULL),
(66, '2025-10-23 08:55:00', 'PERMITIDO', 80, 6, 2, NULL),
(67, '2025-10-23 11:05:00', 'PERMITIDO', 445, 4, 1, NULL),
(68, '2025-10-23 13:55:00', 'PERMITIDO', 443, 7, 11, NULL),
(69, '2025-10-23 18:10:00', 'PERMITIDO', 53, 3, 1, NULL),
(70, '2025-10-24 08:45:00', 'PERMITIDO', 80, 9, 12, NULL),
(71, '2025-10-24 11:10:00', 'PERMITIDO', 8080, 11, 7, NULL),
(72, '2025-10-24 14:40:00', 'PERMITIDO', 25, 17, 10, NULL),
(73, '2025-10-24 20:10:00', 'PERMITIDO', 445, 4, 10, NULL),
(74, '2025-10-27 08:00:00', 'PERMITIDO', 80, 6, 2, NULL),
(75, '2025-10-27 09:15:00', 'PERMITIDO', 445, 4, 1, NULL),
(76, '2025-10-27 13:00:00', 'PERMITIDO', 443, 7, 11, NULL),
(77, '2025-10-27 17:00:00', 'PERMITIDO', 53, 3, 1, NULL),
(78, '2025-10-28 08:18:00', 'PERMITIDO', 80, 9, 12, NULL),
(79, '2025-10-28 10:20:00', 'PERMITIDO', 8080, 11, 7, NULL),
(80, '2025-10-28 14:00:00', 'PERMITIDO', 25, 17, 10, NULL),
(81, '2025-10-28 19:10:00', 'PERMITIDO', 445, 4, 10, NULL),
(82, '2025-10-29 09:05:00', 'PERMITIDO', 5000, 13, 14, NULL),
(83, '2025-10-29 12:45:00', 'PERMITIDO', 443, 7, 11, NULL),
(84, '2025-10-29 16:00:00', 'PERMITIDO', 22, 8, 3, NULL),
(85, '2025-10-29 20:30:00', 'PERMITIDO', 53, 16, 2, NULL),
(86, '2025-10-30 08:00:00', 'PERMITIDO', 80, 6, 2, NULL),
(87, '2025-10-30 11:30:00', 'PERMITIDO', 445, 4, 1, NULL),
(88, '2025-10-30 13:30:00', 'PERMITIDO', 443, 7, 11, NULL),
(89, '2025-10-30 17:20:00', 'PERMITIDO', 53, 3, 1, NULL),
(90, '2025-10-31 08:15:00', 'PERMITIDO', 80, 9, 12, NULL),
(91, '2025-10-31 10:40:00', 'PERMITIDO', 8080, 11, 7, NULL),
(92, '2025-10-31 14:15:00', 'PERMITIDO', 25, 17, 10, NULL),
(93, '2025-10-31 20:00:00', 'PERMITIDO', 445, 4, 10, NULL),
(94, '2025-10-01 10:00:00', 'PERMITIDO', 443, 10, 10, NULL),
(95, '2025-10-02 11:00:00', 'PERMITIDO', 80, 6, 2, NULL),
(96, '2025-10-03 14:00:00', 'PERMITIDO', 445, 4, 11, NULL),
(97, '2025-10-06 12:00:00', 'PERMITIDO', 53, 12, 8, NULL),
(98, '2025-10-07 15:00:00', 'PERMITIDO', 22, 8, 3, NULL),
(99, '2025-10-08 17:00:00', 'PERMITIDO', 8080, 14, 15, NULL),
(100, '2025-10-09 16:00:00', 'PERMITIDO', 443, 9, 12, NULL),
(101, '2025-10-10 12:00:00', 'PERMITIDO', 445, 4, 10, NULL),
(102, '2025-10-13 15:00:00', 'PERMITIDO', 80, 6, 2, NULL),
(103, '2025-10-14 16:00:00', 'PERMITIDO', 443, 7, 11, NULL),
(104, '2025-10-15 10:00:00', 'PERMITIDO', 53, 3, 1, NULL),
(105, '2025-10-16 12:00:00', 'PERMITIDO', 25, 17, 10, NULL),
(106, '2025-10-17 13:00:00', 'PERMITIDO', 445, 4, 11, NULL),
(107, '2025-10-20 16:00:00', 'PERMITIDO', 80, 9, 12, NULL),
(108, '2025-10-21 17:00:00', 'PERMITIDO', 443, 7, 11, NULL),
(109, '2025-10-22 10:00:00', 'PERMITIDO', 22, 8, 3, NULL),
(110, '2025-10-23 14:00:00', 'PERMITIDO', 8080, 11, 7, NULL),
(111, '2025-10-24 15:00:00', 'PERMITIDO', 53, 3, 1, NULL),
(112, '2025-10-27 12:00:00', 'PERMITIDO', 445, 4, 10, NULL),
(113, '2025-10-28 15:30:00', 'PERMITIDO', 80, 6, 2, NULL),
(114, '2025-10-29 11:15:00', 'PERMITIDO', 443, 7, 11, NULL),
(115, '2025-10-30 16:30:00', 'PERMITIDO', 25, 17, 10, NULL),
(116, '2025-10-31 12:10:00', 'PERMITIDO', 445, 4, 1, NULL),
(117, '2025-10-06 18:30:00', 'PERMITIDO', 8080, 12, 8, NULL),
(118, '2025-10-07 18:30:00', 'PERMITIDO', 5000, 13, 14, NULL),
(119, '2025-10-08 18:30:00', 'PERMITIDO', 445, 4, 11, NULL),
(120, '2025-10-09 18:30:00', 'PERMITIDO', 80, 6, 2, NULL),
-- Logs bloqueados por ataque
(121, '2025-10-01 00:00:00', 'BLOQUEADO', 80, 22, NULL, NULL),    
(122, '2025-10-02 11:35:00', 'BLOQUEADO', 3389, 20, NULL, 4),   
(123, '2025-10-02 11:35:01', 'BLOQUEADO', 21, 20, NULL, 4),    
(124, '2025-10-03 14:30:00', 'BLOQUEADO', 22, 24, NULL, 5),   
(125, '2025-10-04 16:00:00', 'BLOQUEADO', 8080, 25, NULL, NULL), 
(126, '2025-10-06 15:00:00', 'BLOQUEADO', 139, 20, NULL, 4),
(127, '2025-10-06 15:00:01', 'BLOQUEADO', 139, 20, NULL, 4),
(128, '2025-10-06 15:00:02', 'BLOQUEADO', 139, 20, NULL, 4),
(129, '2025-10-07 16:30:00', 'BLOQUEADO', 22, 24, NULL, 5),
(130, '2025-10-07 16:30:01', 'BLOQUEADO', 22, 24, NULL, 5),
(131, '2025-10-08 17:30:00', 'BLOQUEADO', 80, 25, NULL, NULL),
(132, '2025-10-09 18:30:00', 'BLOQUEADO', 443, 20, NULL, 4),
(133, '2025-10-10 19:30:00', 'BLOQUEADO', 21, 24, NULL, 5),
(134, '2025-10-13 14:00:00', 'BLOQUEADO', 23, 20, NULL, 4),
(135, '2025-10-14 15:30:00', 'BLOQUEADO', 23, 20, NULL, 4),
(136, '2025-10-15 16:30:00', 'BLOQUEADO', 23, 20, NULL, 4),
(137, '2025-10-16 17:30:00', 'BLOQUEADO', 23, 20, NULL, 4),
(138, '2025-10-17 18:30:00', 'BLOQUEADO', 23, 20, NULL, 4),
(139, '2025-10-20 14:30:00', 'BLOQUEADO', 22, 24, NULL, 5),
(140, '2025-10-21 15:30:00', 'BLOQUEADO', 22, 24, NULL, 5),
(141, '2025-10-22 16:30:00', 'BLOQUEADO', 22, 24, NULL, 5),
(142, '2025-10-23 17:30:00', 'BLOQUEADO', 22, 24, NULL, 5),
(143, '2025-10-24 18:30:00', 'BLOQUEADO', 22, 24, NULL, 5),
(144, '2025-10-27 14:30:00', 'BLOQUEADO', 80, 25, NULL, NULL),
(145, '2025-10-28 15:30:00', 'BLOQUEADO', 443, 25, NULL, NULL),
(146, '2025-10-29 16:30:00', 'BLOQUEADO', 21, 25, NULL, NULL),
(147, '2025-10-30 17:30:00', 'BLOQUEADO', 23, 25, NULL, NULL),
(148, '2025-10-31 18:30:00', 'BLOQUEADO', 5900, 25, NULL, NULL),
(149, '2025-10-16 09:30:00', 'BLOQUEADO', 137, 19, NULL, 3),  
-- Logs bloqueados por horario 
(150, '2025-10-01 22:39:03', 'BLOQUEADO', 80, 6, 2, NULL),    
(151, '2025-10-02 07:57:06', 'BLOQUEADO', 443, 7, 11, NULL),   
(152, '2025-10-04 22:10:00', 'BLOQUEADO', 22, 8, 3, NULL),
(153, '2025-10-05 10:00:00', 'BLOQUEADO', 445, 4, 1, NULL),   
(154, '2025-10-05 15:00:00', 'BLOQUEADO', 80, 6, 2, NULL),  
(155, '2025-10-06 00:30:00', 'BLOQUEADO', 53, 3, 1, NULL),
(156, '2025-10-06 23:00:00', 'BLOQUEADO', 80, 9, 12, NULL),
(157, '2025-10-10 22:05:00', 'BLOQUEADO', 8080, 11, 7, NULL),
(158, '2025-10-11 11:00:00', 'BLOQUEADO', 443, 7, 11, NULL),   
(159, '2025-10-11 16:00:00', 'BLOQUEADO', 25, 17, 10, NULL), 
(160, '2025-10-12 10:00:00', 'BLOQUEADO', 445, 4, 1, NULL),  
(161, '2025-10-12 15:00:00', 'BLOQUEADO', 80, 6, 2, NULL), 
(162, '2025-10-13 07:45:00', 'BLOQUEADO', 53, 3, 1, NULL),
(163, '2025-10-13 22:15:00', 'BLOQUEADO', 80, 9, 12, NULL),
(164, '2025-10-17 22:08:00', 'BLOQUEADO', 8080, 11, 7, NULL),
(165, '2025-10-18 11:00:00', 'BLOQUEADO', 443, 7, 11, NULL),   
(166, '2025-10-18 16:00:00', 'BLOQUEADO', 25, 17, 10, NULL), 
(167, '2025-10-19 10:00:00', 'BLOQUEADO', 445, 4, 1, NULL),   
(168, '2025-10-19 15:00:00', 'BLOQUEADO', 80, 6, 2, NULL),    
(169, '2025-10-20 07:30:00', 'BLOQUEADO', 53, 3, 1, NULL),
(170, '2025-10-20 22:20:00', 'BLOQUEADO', 80, 9, 12, NULL),
(171, '2025-10-24 22:12:00', 'BLOQUEADO', 8080, 11, 7, NULL),
(172, '2025-10-25 11:00:00', 'BLOQUEADO', 443, 7, 11, NULL),   
(173, '2025-10-25 16:00:00', 'BLOQUEADO', 25, 17, 10, NULL),
(174, '2025-10-26 10:00:00', 'BLOQUEADO', 445, 4, 1, NULL),   
(175, '2025-10-26 15:00:00', 'BLOQUEADO', 80, 6, 2, NULL),    
(176, '2025-10-27 07:00:00', 'BLOQUEADO', 53, 3, 1, NULL),
(177, '2025-10-27 22:30:00', 'BLOQUEADO', 80, 9, 12, NULL),
(178, '2025-10-31 22:00:06', 'BLOQUEADO', 445, 4, 10, NULL),  
(179, '2025-10-04 11:00:00', 'BLOQUEADO', 53, 22, NULL, NULL),  
(180, '2025-10-08 14:00:00', 'BLOQUEADO', 21, 22, NULL, NULL), 
(181, '2025-10-14 17:00:00', 'BLOQUEADO', 22, 22, NULL, NULL),
(182, '2025-10-22 18:00:00', 'BLOQUEADO', 25, 22, NULL, NULL),   
(183, '2025-10-30 19:00:00', 'BLOQUEADO', 8080, 22, NULL, NULL); 

INSERT INTO Alertas (id_alerta, tipo_alerta, fecha_alerta, gravedad, estado, id_log, id_analista_asignado) VALUES
(1, 'Tráfico 0.0.0.0 (Malicioso)', '2025-10-01 00:00:05', 'Crítica', 'En Progreso', 121, 3), -- Log 121: IP 22 (0.0.0.0)
(2, 'Escaneo RDP/SMB (Persistente)', '2025-10-02 11:35:05', 'Alta', 'Pendiente', 122, 4),    -- Log 122: IP 20 
(3, 'Fuerza Bruta SSH (Nueva IP)', '2025-10-03 14:30:05', 'Alta', 'Pendiente', 124, 5),   -- Log 124: IP 24 
(4, 'Tráfico Fuera de Horario (Reincidente)', '2025-10-18 11:00:05', 'Baja', 'Cerrada', 165, 6),   -- Log 165: Bloqueo SÁBADO 
(5, 'Patrón de Escaneo Desconocido', '2025-10-24 18:30:05', 'Media', 'Pendiente', 143, 4);   -- Log 143: IP 24 

INSERT INTO Reportes (id_reporte, fecha_creacion, titulo, contenido, id_usuario_creador) VALUES
(1, '2025-10-05', 'Reporte de bloqueos semanales (Oct 1-5)', 'El tráfico de fin de semana fue bloqueado correctamente. Se identificó tráfico de la IP 22 (0.0.0.0).', 6), -- Analista D
(2, '2025-10-10', 'Revisión de ataques IP 20 y 24', 'Las IPs 20 y 24 están realizando ataques constantes. Se revisaron los logs 122 a 138. Se sugiere bloqueo permanente.', 4), -- Analista B
(3, '2025-10-15', 'Informe de alerta crítica (0.0.0.0)', 'Se realizaron modificaciones en la configuración debido al tráfico de IP 0.0.0.0 (Log 121). La alerta #1 se mantiene En Progreso.', 3); -- Analista A

INSERT INTO Auditoria (id_auditoria, fecha, tabla_afectada, accion_realizada, detalle, id_usuario_sistema) VALUES
(1, '2025-10-02 11:35:10', 'Alertas', 'INSERT', 'Alerta #2 (IP 20) generada automáticamente tras violación de umbral.', 4),
(2, '2025-10-03 14:30:15', 'Alertas', 'INSERT', 'Alerta #3 (IP 24) creada por tráfico anómalo en puerto 22.', 5),
(3, '2025-10-05 18:00:00', 'Logs_Firewall', 'REVISION', 'Revisión manual de los logs de bloqueo de fin de semana (Logs 153-154).', 6),
(4, '2025-10-15 09:00:00', 'Alertas', 'UPDATE', 'Se actualiza Alerta #1 a "En Progreso" y se asigna al Analista A.', 3),
(5, '2025-10-18 12:00:00', 'Alertas', 'UPDATE', 'Alerta #4 cerrada después de confirmar bloqueo de fin de semana (Log 165).', 6),
(6, '2025-10-24 18:35:00', 'Logs_Firewall', 'REGLA MODIFICADA', 'Se actualizó la regla 300 para mitigar ataques de IPs maliciosas.', 4);

