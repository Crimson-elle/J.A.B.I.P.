import customtkinter
import tkinter as tk

class AdminView:
    
    @staticmethod
    def show_usuarios(app):
        #Muestra los usuarios del sistema (solo admin)
        if not app.db:
            return
            
        for widget in app.result_frame.winfo_children():
            widget.destroy()
            
        app.status_var.set("Cargando usuarios...")
        
        try:
            query = """
                SELECT u.id_usuario, u.nombre_usuario, u.email, u.cargo, r.nombre_rol
                FROM Usuarios u
                JOIN Roles r ON u.id_rol = r.id_rol
                ORDER BY u.id_usuario
            """
            usuarios = app.db.fetch_data(query)
            
            title = customtkinter.CTkLabel(
                app.result_frame,
                text="USUARIOS DEL SISTEMA",
                font=("Arial", 16, "bold")
            )
            title.pack(pady=10)
            
            for user in usuarios:
                text = f"ID: {user['id_usuario']} | {user['nombre_usuario']} | " \
                    f"{user['email']} | {user['cargo']} | Rol: {user['nombre_rol']}"
                label = customtkinter.CTkLabel(
                    app.result_frame,
                    text=text,
                    anchor="w",
                    font=("Arial", 13)
                )
                label.pack(pady=2, padx=10, fill="x")
                
            app.status_var.set(f"Mostrando {len(usuarios)} usuarios")
        except Exception as e:
            error_label = customtkinter.CTkLabel(
                app.result_frame,
                text=f"Error al cargar usuarios: {str(e)}",
                text_color="red"
            )
            error_label.pack(pady=20)
    
    @staticmethod
    def show_alertas_admin(app):
        #Muestra las alertas del sistema con funcionalidad de gestión de IPs para administradores
        if not app.db:
            return
            
        for widget in app.result_frame.winfo_children():
            widget.destroy()
            
        app.status_var.set("Cargando alertas...")
        
        try:
            # Consulta para obtener alertas relacionadas con solicitudes de IP
            query = """
                SELECT a.id_alerta, a.tipo_alerta, a.gravedad, a.estado, 
                    a.fecha_alerta, u.nombre_usuario as analista
                FROM Alertas a
                LEFT JOIN Usuarios u ON a.id_analista_asignado = u.id_usuario
                WHERE a.tipo_alerta LIKE '%IP%' OR a.tipo_alerta LIKE '%solicita registro%'
                ORDER BY a.fecha_alerta DESC
                LIMIT 20
            """
            alertas = app.db.fetch_data(query)
            
            title = customtkinter.CTkLabel(
                app.result_frame, 
                text="GESTIÓN DE ALERTAS - CONTROL DE IPs",
                font=("Arial", 16, "bold")
            )
            title.pack(pady=10)
            
            if not alertas:
                no_alerts = customtkinter.CTkLabel(
                    app.result_frame,
                    text="No hay alertas de IP pendientes",
                    font=("Arial", 12)
                )
                no_alerts.pack(pady=20)
                app.status_var.set("No hay alertas de IP")
                return
            
            for alerta in alertas:
                # Frame contenedor para cada alerta
                alert_frame = customtkinter.CTkFrame(app.result_frame)
                alert_frame.pack(pady=5, padx=10, fill="x")
                
                # Información de la alerta
                alert_text = f"#{alerta['id_alerta']} - {alerta['tipo_alerta']}\n" \
                        f"Gravedad: {alerta['gravedad']} | Estado: {alerta['estado']} | " \
                        f"Fecha: {alerta['fecha_alerta']}"
                
                info_label = customtkinter.CTkLabel(
                    alert_frame,
                    text=alert_text,
                    anchor="w",
                    font=("Arial", 11),
                    justify="left"
                )
                info_label.pack(pady=5, padx=10, fill="x")
                
                # Extraer IP de la descripción de la alerta si existe
                ip_address = AdminView._extract_ip_from_alert(alerta['tipo_alerta'])
                
                if ip_address and alerta['estado'] == 'Pendiente':
                    # Frame para botones de acción
                    button_frame = customtkinter.CTkFrame(alert_frame)
                    button_frame.pack(pady=5, padx=10, fill="x")
                    
                    ip_label = customtkinter.CTkLabel(
                        button_frame,
                        text=f"IP: {ip_address}",
                        font=("Arial", 10, "bold")
                    )
                    ip_label.pack(side="left", padx=5)
                    
                    # Botón para permitir IP
                    allow_btn = customtkinter.CTkButton(
                        button_frame,
                        text="✓ Permitir IP",
                        command=lambda ip=ip_address, alert_id=alerta['id_alerta']: 
                            AdminView._handle_ip_action(app, ip, "Confiable", alert_id),
                        width=100,
                        height=25,
                        fg_color="#51cf66",
                        hover_color="#40c057",
                        text_color="black"
                    )
                    allow_btn.pack(side="right", padx=2)
                    
                    # Botón para bloquear IP
                    block_btn = customtkinter.CTkButton(
                        button_frame,
                        text="✗ Bloquear IP",
                        command=lambda ip=ip_address, alert_id=alerta['id_alerta']: 
                            AdminView._handle_ip_action(app, ip, "Maliciosa", alert_id),
                        width=100,
                        height=25,
                        fg_color="#ff6b6b",
                        hover_color="#fa5252",
                        text_color="black"
                    )
                    block_btn.pack(side="right", padx=2)
                    
                    # Botón para marcar como sospechosa
                    suspect_btn = customtkinter.CTkButton(
                        button_frame,
                        text="? Sospechosa",
                        command=lambda ip=ip_address, alert_id=alerta['id_alerta']: 
                            AdminView._handle_ip_action(app, ip, "Sospechosa", alert_id),
                        width=100,
                        height=25,
                        fg_color="#ffd43b",
                        hover_color="#fab005",
                        text_color="black"
                    )
                    suspect_btn.pack(side="right", padx=2)
                    
            app.status_var.set(f"Mostrando {len(alertas)} alertas de IP")
        except Exception as e:
            error_label = customtkinter.CTkLabel(
                app.result_frame,
                text=f"Error al cargar alertas: {str(e)}",
                text_color="red"
            )
            error_label.pack(pady=20)
    
    @staticmethod
    def _extract_ip_from_alert(alert_text):
        """Extrae la dirección IP del texto de la alerta"""
        import re
        # Buscar patrón de IP en el texto
        ip_pattern = r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b'
        match = re.search(ip_pattern, alert_text)
        return match.group() if match else None
    
    @staticmethod
    def _handle_ip_action(app, ip_address, new_status, alert_id):
        """Maneja las acciones sobre las IPs (permitir, bloquear, marcar como sospechosa)"""
        if not app.db or not app.usuario_id:
            return
            
        try:
            # Verificar si la IP ya existe en el sistema
            check_query = "SELECT id_ip, estado FROM IPs WHERE direccion_ip = %s"
            existing_ip = app.db.fetch_data(check_query, (ip_address,))
            
            if existing_ip:
                # La IP ya existe, actualizar su estado usando el stored procedure
                sp_query = "CALL SP_CambiarEstadoIP(%s, %s, %s)"
                success = app.db.execute_query(sp_query, (ip_address, new_status, app.usuario_id))
            else:
                # La IP no existe, crearla con el estado especificado
                insert_query = """
                    INSERT INTO IPs (direccion_ip, estado, fecha_ultimo_visto, id_dispositivo)
                    VALUES (%s, %s, NOW(), NULL)
                """
                success = app.db.execute_query(insert_query, (ip_address, new_status))
                
                # Registrar en auditoría
                audit_query = """
                    INSERT INTO Auditoria (fecha, tabla_afectada, accion_realizada, detalle, id_usuario_sistema)
                    VALUES (NOW(), 'IPs', 'INSERT_NEW_IP', %s, %s)
                """
                audit_detail = f"Nueva IP {ip_address} registrada con estado {new_status}"
                app.db.execute_query(audit_query, (audit_detail, app.usuario_id))
            
            if success:
                # Cerrar la alerta
                close_alert_query = """
                    UPDATE Alertas 
                    SET estado = 'Cerrada', id_analista_asignado = %s 
                    WHERE id_alerta = %s
                """
                app.db.execute_query(close_alert_query, (app.usuario_id, alert_id))
                
                # Mostrar mensaje de éxito
                status_messages = {
                    "Confiable": "IP permitida correctamente",
                    "Maliciosa": "IP bloqueada correctamente", 
                    "Sospechosa": "IP marcada como sospechosa"
                }
                app.status_var.set(f"{status_messages.get(new_status, 'Acción completada')} - {ip_address}")
                
                # Recargar las alertas
                AdminView.show_alertas_admin(app)
            else:
                app.status_var.set(f"Error al procesar IP {ip_address}")
                
        except Exception as e:
            app.status_var.set(f"Error: {str(e)}")
    
    @staticmethod
    def show_ip_management(app):
        """Muestra una interfaz completa para gestionar IPs del sistema"""
        if not app.db:
            return
            
        for widget in app.result_frame.winfo_children():
            widget.destroy()
            
        app.status_var.set("Cargando gestión de IPs...")
        
        try:
            title = customtkinter.CTkLabel(
                app.result_frame,
                text="GESTIÓN DE IPs DEL SISTEMA",
                font=("Arial", 16, "bold")
            )
            title.pack(pady=10)
            
            # Frame para búsqueda manual
            search_frame = customtkinter.CTkFrame(app.result_frame)
            search_frame.pack(pady=10, padx=10, fill="x")
            
            search_label = customtkinter.CTkLabel(
                search_frame,
                text="Gestionar IP específica:",
                font=("Arial", 12, "bold")
            )
            search_label.pack(pady=5)
            
            # Entry para ingresar IP
            ip_entry = customtkinter.CTkEntry(
                search_frame,
                placeholder_text="Ej: 192.168.1.100",
                width=200
            )
            ip_entry.pack(pady=5)
            
            # Frame para botones de acción manual
            manual_buttons_frame = customtkinter.CTkFrame(search_frame)
            manual_buttons_frame.pack(pady=5)
            
            allow_manual_btn = customtkinter.CTkButton(
                manual_buttons_frame,
                text="Permitir",
                command=lambda: AdminView._manual_ip_action(app, ip_entry.get(), "Confiable"),
                width=80,
                fg_color="#51cf66",
                hover_color="#40c057",
                text_color="black"
            )
            allow_manual_btn.pack(side="left", padx=5)
            
            suspect_manual_btn = customtkinter.CTkButton(
                manual_buttons_frame,
                text="Sospechosa",
                command=lambda: AdminView._manual_ip_action(app, ip_entry.get(), "Sospechosa"),
                width=80,
                fg_color="#ffd43b",
                hover_color="#fab005",
                text_color="black"
            )
            suspect_manual_btn.pack(side="left", padx=5)
            
            block_manual_btn = customtkinter.CTkButton(
                manual_buttons_frame,
                text="Bloquear",
                command=lambda: AdminView._manual_ip_action(app, ip_entry.get(), "Maliciosa"),
                width=80,
                fg_color="#ff6b6b",
                hover_color="#fa5252",
                text_color="black"
            )
            block_manual_btn.pack(side="left", padx=5)
            
            # Mostrar IPs existentes
            separator = customtkinter.CTkLabel(
                app.result_frame,
                text="─" * 50,
                font=("Arial", 10)
            )
            separator.pack(pady=10)
            
            ips_title = customtkinter.CTkLabel(
                app.result_frame,
                text="IPs REGISTRADAS EN EL SISTEMA",
                font=("Arial", 14, "bold")
            )
            ips_title.pack(pady=5)
            
            # Consultar IPs
            query = """
                SELECT i.direccion_ip, i.estado, i.fecha_ultimo_visto, d.nombre_activo
                FROM IPs i
                LEFT JOIN Dispositivos d ON i.id_dispositivo = d.id_dispositivo
                ORDER BY 
                    CASE i.estado
                        WHEN 'Maliciosa' THEN 1
                        WHEN 'Sospechosa' THEN 2
                        WHEN 'Confiable' THEN 3
                        ELSE 4
                    END,
                    i.fecha_ultimo_visto DESC
            """
            ips = app.db.fetch_data(query)
            
            for ip in ips:
                ip_frame = customtkinter.CTkFrame(app.result_frame)
                ip_frame.pack(pady=2, padx=10, fill="x")
                
                # Color según estado
                color_map = {
                    "Maliciosa": "#ff6b6b",
                    "Sospechosa": "#ffd43b", 
                    "Confiable": "#51cf66"
                }
                
                ip_text = f"{ip['direccion_ip']} | Estado: {ip['estado']} | " \
                        f"Último visto: {ip['fecha_ultimo_visto']}"
                if ip['nombre_activo']:
                    ip_text += f" | Dispositivo: {ip['nombre_activo']}"
                
                ip_label = customtkinter.CTkLabel(
                    ip_frame,
                    text=ip_text,
                    anchor="w",
                    font=("Arial", 10),
                    text_color=color_map.get(ip['estado'], "#ffffff")
                )
                ip_label.pack(side="left", pady=5, padx=10, fill="x", expand=True)
                
            app.status_var.set(f"Mostrando {len(ips)} IPs registradas")
            
        except Exception as e:
            error_label = customtkinter.CTkLabel(
                app.result_frame,
                text=f"Error al cargar gestión de IPs: {str(e)}",
                text_color="red"
            )
            error_label.pack(pady=20)
    
    @staticmethod
    def _manual_ip_action(app, ip_address, new_status):
        """Maneja acciones manuales sobre IPs"""
        if not ip_address or not ip_address.strip():
            app.status_var.set("Por favor ingrese una dirección IP válida")
            return
            
        ip_address = ip_address.strip()
        
        # Validar formato básico de IP
        import re
        ip_pattern = r'^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$'
        if not re.match(ip_pattern, ip_address):
            app.status_var.set("Formato de IP inválido")
            return
            
        AdminView._handle_ip_action(app, ip_address, new_status, None)
