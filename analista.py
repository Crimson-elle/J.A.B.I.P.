import customtkinter

class AnalistaView:
    
    @staticmethod
    def show_alertas(app):
        #Muestra las alertas del sistema
        if not app.db:
            return
            
        for widget in app.result_frame.winfo_children():
            widget.destroy()
            
        app.status_var.set("Cargando alertas...")
        
        try:
            query = """
                SELECT a.id_alerta, a.tipo_alerta, a.gravedad, a.estado, 
                    a.fecha_alerta, u.nombre_usuario as analista
                FROM Alertas a
                LEFT JOIN Usuarios u ON a.id_analista_asignado = u.id_usuario
                ORDER BY a.fecha_alerta DESC
                LIMIT 20
            """
            alertas = app.db.fetch_data(query)
            
            title = customtkinter.CTkLabel(
                app.result_frame, 
                text="ALERTAS DEL SISTEMA",
                font=("Arial", 16, "bold")
            )
            title.pack(pady=10)
            
            for alerta in alertas:
                text = f"#{alerta['id_alerta']} - {alerta['tipo_alerta']} | " \
                    f"Gravedad: {alerta['gravedad']} | Estado: {alerta['estado']} | " \
                    f"Analista: {alerta['analista'] or 'Sin asignar'}"
                label = customtkinter.CTkLabel(
                    app.result_frame,
                    text=text,
                    anchor="w",
                    font=("Arial", 13)
                )
                label.pack(pady=2, padx=10, fill="x")
                    
            app.status_var.set(f"Mostrando {len(alertas)} alertas")
        except Exception as e:
            error_label = customtkinter.CTkLabel(
                app.result_frame,
                text=f"Error al cargar alertas: {str(e)}",
                text_color="red"
            )
            error_label.pack(pady=20)
    
    @staticmethod
    def show_logs(app):
        #Muestra los logs del firewall
        if not app.db:
            return
            
        for widget in app.result_frame.winfo_children():
            widget.destroy()
            
        app.status_var.set("Cargando logs...")
        
        try:
            query = """
                SELECT l.id_log, l.fecha_log, l.accion, l.puerto_destino,
                    i.direccion_ip, u.nombre_usuario
                FROM Logs_Firewall l
                JOIN IPs i ON l.id_ip = i.id_ip
                LEFT JOIN Usuarios u ON l.id_usuario_origen = u.id_usuario
                ORDER BY l.fecha_log DESC
                LIMIT 30
            """
            logs = app.db.fetch_data(query)
                
            title = customtkinter.CTkLabel(
                app.result_frame,
                text="LOGS DEL FIREWALL",
                font=("Arial", 16, "bold")
            )
            title.pack(pady=10)
            
            for log in logs:
                text = f"{log.get('fecha_log', 'N/A')} | {log.get('accion', 'N/A')} | " \
                    f"IP: {log.get('direccion_ip', 'N/A')} | Puerto: {log.get('puerto_destino', 'N/A')}"
                if 'nombre_usuario' in log and log.get('nombre_usuario'):
                    text += f" | Usuario: {log.get('nombre_usuario')}"
                label = customtkinter.CTkLabel(
                    app.result_frame,
                    text=text,
                    anchor="w",
                    font=("Arial", 13)
                )
                label.pack(pady=2, padx=10, fill="x")
                
            app.status_var.set(f"Mostrando {len(logs)} logs")
        except Exception as e:
            error_label = customtkinter.CTkLabel(
                app.result_frame,
                text=f"Error al cargar logs: {str(e)}",
                text_color="red"
            )
            error_label.pack(pady=20)
    
    @staticmethod
    def show_reportes(app):
        #Muestra los reportes del sistema
        if not app.db:
            return
            
        for widget in app.result_frame.winfo_children():
            widget.destroy()
            
        app.status_var.set("Cargando reportes...")
        
        try:
            query = """
                SELECT r.id_reporte, r.fecha_creacion, r.titulo, 
                    u.nombre_usuario as creador
                FROM Reportes r
                JOIN Usuarios u ON r.id_usuario_creador = u.id_usuario
                ORDER BY r.fecha_creacion DESC
            """
            reportes = app.db.fetch_data(query)
            
            title = customtkinter.CTkLabel(
                app.result_frame,
                text="REPORTES DEL SISTEMA",
                font=("Arial", 16, "bold")
            )
            title.pack(pady=10)
            
            for reporte in reportes:
                text = f"#{reporte['id_reporte']} - {reporte['titulo']} | " \
                    f"Fecha: {reporte['fecha_creacion']} | Creador: {reporte['creador']}"
                label = customtkinter.CTkLabel(
                    app.result_frame,
                    text=text,
                    anchor="w",
                    font=("Arial", 13)
                )
                label.pack(pady=2, padx=10, fill="x")
                
            app.status_var.set(f"Mostrando {len(reportes)} reportes")
        except Exception as e:
            error_label = customtkinter.CTkLabel(
                app.result_frame,
                text=f"Error al cargar reportes: {str(e)}",
                text_color="red"
            )
            error_label.pack(pady=20)
