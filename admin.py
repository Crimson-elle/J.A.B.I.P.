import customtkinter

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
