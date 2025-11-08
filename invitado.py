#Menú de Invitado
import customtkinter

class InvitadoView:
    
    @staticmethod
    def show_notificaciones(app):
        #Muestra notificaciones de red para el usuario
        if not app.db:
            return
            
        for widget in app.result_frame.winfo_children():
            widget.destroy()
            
        app.status_var.set("Cargando notificaciones...")
        
        title = customtkinter.CTkLabel(
            app.result_frame,
            text="NOTIFICACIONES DE RED",
            font=("Arial", 16, "bold")
        )
        title.pack(pady=10)
        
        try:
            query = "SELECT id_ip, estado, fecha_ultimo_visto FROM IPs WHERE direccion_ip = %s"
            result = app.db.fetch_data(query, (app.user_ip,))
            
            if not result or len(result) == 0:
                warning = customtkinter.CTkLabel(
                    app.result_frame,
                    text="ALERTA: IP No Registrada",
                    font=("Arial", 16, "bold"),
                    text_color="#ff6b6b"
                )
                warning.pack(pady=10)
                
                msg = customtkinter.CTkLabel(
                    app.result_frame,
                    text=f"Su direccion IP ({app.user_ip}) no esta registrada en el sistema.\n\n"
                        "Por razones de seguridad, esta IP sera bloqueada si no solicita acceso.\n\n"
                        "Por favor, haga clic en 'Solicitar Acceso de Red' para registrar su IP o inicie sesión.",
                        font=("Arial", 15),
                    justify="left"
                )
                msg.pack(pady=10, padx=20)

                # Botón inline para solicitar acceso de red (solo visible si la IP no existe)
                solicitar_btn = customtkinter.CTkButton(
                    app.result_frame,
                    text="Solicitar Acceso de Red",
                    command=lambda: InvitadoView._inline_solicitar_wrapper(app),
                    fg_color="#2563eb",
                    hover_color="#3b82f6",
                    text_color="#ffffff"
                )
                solicitar_btn.pack(pady=6)
                
            else:
                ip_data = result[0]
                estado = ip_data['estado']
                
                if estado == 'Confiable':
                    info = customtkinter.CTkLabel(
                        app.result_frame,
                        text="Estado: Confiable",
                        font=("Arial", 14, "bold"),
                        text_color="#51cf66"
                    )
                    info.pack(pady=10)
                    
                    msg = customtkinter.CTkLabel(
                        app.result_frame,
                        text=f"Su IP ({app.user_ip}) esta registrada y autorizada en el sistema.",
                            font=("Arial", 13)
                    )
                    msg.pack(pady=10)
                    
                elif estado == 'Sospechosa':
                    warning = customtkinter.CTkLabel(
                        app.result_frame,
                        text="Estado: Sospechosa",
                        font=("Arial", 14, "bold"),
                        text_color="#ffd43b"
                    )
                    warning.pack(pady=10)
                    
                    msg = customtkinter.CTkLabel(
                        app.result_frame,
                        text=f"Su IP ({app.user_ip}) ha sido marcada como sospechosa.\n"
                            "Contacte al administrador del sistema.",
                            font=("Arial", 13)
                    )
                    msg.pack(pady=10)
                    
                else:
                    InvitadoView.show_blocked_message(app)
                    return
            
            app.status_var.set("Notificaciones cargadas")
        except Exception as e:
            error_label = customtkinter.CTkLabel(
                app.result_frame,
                text=f"Error al cargar notificaciones: {str(e)}",
                text_color="red"
            )
            error_label.pack(pady=20)
    
    @staticmethod
    def solicitar_acceso_ip(app):
#Solicita acceso para la IP del usuario
        if not app.db:
            return
            
        for widget in app.result_frame.winfo_children():
            widget.destroy()
            
        title = customtkinter.CTkLabel(
            app.result_frame,
            text="SOLICITAR ACCESO DE RED",
            font=("Arial", 16, "bold")
        )
        title.pack(pady=10)
        
        try:
            query = "SELECT id_ip FROM IPs WHERE direccion_ip = %s"
            result = app.db.fetch_data(query, (app.user_ip,))
            
            if result and len(result) > 0:
                msg = customtkinter.CTkLabel(
                    app.result_frame,
                    text=f"Su IP ({app.user_ip}) ya esta registrada en el sistema.",
                    font=("Arial", 12)
                )
                msg.pack(pady=20)
            else:
                if app.usuario_id:
                    detalle = f"Usuario {app.current_user} (ID: {app.usuario_id}) solicita registro de IP {app.user_ip}"
                else:
                    detalle = f"Usuario no autenticado solicita registro de IP {app.user_ip}"
                
                insert_query = """
                    INSERT INTO Alertas (tipo_alerta, fecha_alerta, gravedad, estado, id_analista_asignado)
                    VALUES (%s, NOW(), 'Media', 'Pendiente', NULL)
                """
                
                if app.db.execute_query(insert_query, (detalle,)):
                    success = customtkinter.CTkLabel(
                        app.result_frame,
                        text="Solicitud Enviada",
                        font=("Arial", 14, "bold"),
                        text_color="#51cf66"
                    )
                    success.pack(pady=10)
                    
                    msg = customtkinter.CTkLabel(
                        app.result_frame,
                        text=f"Se ha enviado una solicitud para registrar su IP ({app.user_ip}).\n\n"
                            "Un administrador revisara su solicitud pronto.\n"
                            "Recibira una notificacion cuando su IP sea autorizada.",
                            font=("Arial", 13),
                        justify="left"
                    )
                    msg.pack(pady=10, padx=20)
                else:
                    error = customtkinter.CTkLabel(
                        app.result_frame,
                        text="Error al enviar la solicitud. Intente nuevamente.",
                        font=("Arial", 12),
                        text_color="#ff6b6b"
                    )
                    error.pack(pady=20)
            
            app.status_var.set("Solicitud procesada")
        except Exception as e:
            error_label = customtkinter.CTkLabel(
                app.result_frame,
                text=f"Error: {str(e)}",
                text_color="red"
            )
            error_label.pack(pady=20)

    @staticmethod
    def _inline_solicitar_wrapper(app):
        #Wrapper para usar el flujo existente y luego volver a mostrar notificaciones.
        InvitadoView.solicitar_acceso_ip(app)
        # Después de procesar la solicitud vuelve a mostrar notificaciones para refrescar estado
        app.show_notificaciones()
    
    @staticmethod
    def show_blocked_message(app):
        #Muestra mensaje si la IP está bloqueada.
        for widget in app.result_frame.winfo_children():
            widget.destroy()
        
        warning = customtkinter.CTkLabel(
            app.result_frame,
            text="ACCESO BLOQUEADO",
            font=("Arial", 18, "bold"),
            text_color="red"
        )
        warning.pack(pady=20)
        
        msg = customtkinter.CTkLabel(
            app.result_frame,
            text=f"Su direccion IP ({app.user_ip}) ha sido bloqueada.\nContacte al administrador del sistema.",
            font=("Arial", 12)
        )
        msg.pack(pady=10)
    
    @staticmethod
    def show_mis_datos(app):
#Muestra los datos del usuario actual
        if not app.db:
            return
            
        for widget in app.result_frame.winfo_children():
            widget.destroy()
            
        app.status_var.set("Cargando datos...")
        
        title = customtkinter.CTkLabel(
            app.result_frame,
            text="MIS DATOS",
            font=("Arial", 16, "bold")
        )
        title.pack(pady=10)
        
        try:
            if app.usuario_id:
                query = """
                    SELECT nombre_usuario, email, cargo, fecha_nacimiento, contacto
                    FROM Usuarios
                    WHERE id_usuario = %s
                """
                datos = app.db.fetch_data(query, (app.usuario_id,))
            else:
                datos = app.db.fetch_data("SELECT nombre_usuario, email FROM Vista_1 LIMIT 1")
            
            if datos:
                data = datos[0]
                info_text = f"Usuario: {data.get('nombre_usuario', 'N/A')}\n"
                info_text += f"Email: {data.get('email', 'N/A')}\n"
                
                if 'cargo' in data:
                    info_text += f"Cargo: {data.get('cargo', 'N/A')}\n"
                if 'contacto' in data:
                    info_text += f"Contacto: {data.get('contacto', 'N/A')}\n"
                    
                info_label = customtkinter.CTkLabel(
                    app.result_frame,
                    text=info_text,
                    justify="left",
                        font=("Arial", 13)
                )
                info_label.pack(pady=10)
            
            app.status_var.set("Datos cargados")
        except Exception as e:
            error_label = customtkinter.CTkLabel(
                app.result_frame,
                text=f"Error al cargar datos: {str(e)}",
                text_color="red"
            )
            error_label.pack(pady=20)
