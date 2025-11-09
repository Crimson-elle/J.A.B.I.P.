import customtkinter
import json
import os
import socket
from BD import DatabaseConnection
from invitado import InvitadoView
from analista import AnalistaView
from admin import AdminView

def load_theme(path: str):
    if not os.path.exists(path):
        return {}
    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return {}

theme = load_theme(os.path.join(os.path.dirname(__file__), "theme.json"))
colors = theme.get("color", {})
widget_colors = theme.get("widget", {})

try:
    customtkinter.set_appearance_mode("Dark")
except Exception:
    pass

class FirewallApp:
    def __init__(self, root):
        self.root = root
        self.root.title("J.A.B.I.P.")
        self.root.geometry("600x500")
        
        self.db = None
        self.current_user = None
        self.current_role = "invitado"
        self.usuario_id = None
        self.user_ip = self.get_local_ip()
        # Flag para controlar si la IP actual no está registrada
        self.ip_unregistered = False
        
        self.setup_ui()
        self.auto_connect_guest()
        
    def get_local_ip(self):
        #Obtiene la IP local del usuario
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.connect(("8.8.8.8", 80))
            ip = s.getsockname()[0]
            s.close()
            return ip
        except Exception:
            return "127.0.0.1"
        
    def setup_ui(self):
        #Configura la interfaz de usuario
        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_rowconfigure(1, weight=1)
        
        btn_colors = widget_colors.get("button", {})
        
        # Frame de opciones
        self.options_frame = customtkinter.CTkFrame(self.root)
        self.options_frame.grid(row=0, column=0, padx=20, pady=10, sticky="ew")
        
        # Botón Iniciar Sesión
        self.login_button = customtkinter.CTkButton(
            self.options_frame,
            text="Iniciar Sesion",
            command=self.show_login_dialog,
            fg_color=btn_colors.get("fg_color", colors.get("primary", None)),
            hover_color=btn_colors.get("hover_color", None),
            text_color=btn_colors.get("text_color", None),
        )
        self.login_button.pack(pady=8, padx=20, fill="x")
        
        # Botón Ver Mis Datos
        self.mis_datos_button = customtkinter.CTkButton(
            self.options_frame,
            text="Ver Mis Datos",
            command=self.show_mis_datos,
            fg_color=btn_colors.get("fg_color", colors.get("primary", None)),
            hover_color=btn_colors.get("hover_color", None),
            text_color=btn_colors.get("text_color", None),
        )
        
        # Botón Notificaciones IP
        self.notificaciones_button = customtkinter.CTkButton(
            self.options_frame,
            text="Notificaciones de Red",
            command=self.show_notificaciones,
            fg_color=btn_colors.get("fg_color", colors.get("primary", None)),
            hover_color=btn_colors.get("hover_color", None),
            text_color=btn_colors.get("text_color", None),
        )
        # Guardar texto base del botón para poder mostrar/ocultar un "badge"
        self._notificaciones_base_text = "Notificaciones de Red"
        self._notificaciones_badge_active = False
        
        # Botón Solicitar Acceso IP
        self.solicitar_ip_button = customtkinter.CTkButton(
            self.options_frame,
            text="Solicitar Acceso de Red",
            command=self.solicitar_acceso_ip,
            fg_color=btn_colors.get("fg_color", colors.get("primary", None)),
            hover_color=btn_colors.get("hover_color", None),
            text_color=btn_colors.get("text_color", None),
        )
        
        # Botón Alertas
        self.alertas_button = customtkinter.CTkButton(
            self.options_frame,
            text="Ver Alertas",
            command=self.show_alertas,
            fg_color=btn_colors.get("fg_color", colors.get("primary", None)),
            hover_color=btn_colors.get("hover_color", None),
            text_color=btn_colors.get("text_color", None),
        )
        
        # Botón Logs
        self.logs_button = customtkinter.CTkButton(
            self.options_frame,
            text="Ver Logs",
            command=self.show_logs,
            fg_color=btn_colors.get("fg_color", colors.get("primary", None)),
            hover_color=btn_colors.get("hover_color", None),
            text_color=btn_colors.get("text_color", None),
        )
        
        # Botón Usuarios
        self.usuarios_button = customtkinter.CTkButton(
            self.options_frame,
            text="Gestionar Usuarios",
            command=self.show_usuarios,
            fg_color=btn_colors.get("fg_color", colors.get("primary", None)),
            hover_color=btn_colors.get("hover_color", None),
            text_color=btn_colors.get("text_color", None),
        )
        
        # Botón Gestión de IPs
        self.ip_management_button = customtkinter.CTkButton(
            self.options_frame,
            text="Gestionar IPs",
            command=self.show_ip_management,
            fg_color=btn_colors.get("fg_color", colors.get("primary", None)),
            hover_color=btn_colors.get("hover_color", None),
            text_color=btn_colors.get("text_color", None),
        )
        
        # Botón Reportes
        self.reportes_button = customtkinter.CTkButton(
            self.options_frame,
            text="Ver Reportes",
            command=self.show_reportes,
            fg_color=btn_colors.get("fg_color", colors.get("primary", None)),
            hover_color=btn_colors.get("hover_color", None),
            text_color=btn_colors.get("text_color", None),
        )
        
        # Área de resultados
        self.result_frame = customtkinter.CTkScrollableFrame(self.root, height=300)
        self.result_frame.grid(row=1, column=0, padx=20, pady=10, sticky="nsew")
        
        # Footer
        footer_colors = widget_colors.get("footer", {})
        self.status_var = customtkinter.StringVar(value="Conectando...")
        self.footer = customtkinter.CTkFrame(
            self.root, 
            height=24, 
            corner_radius=0, 
            fg_color=footer_colors.get("bg", colors.get("background", None))
        )
        self.footer.grid(row=2, column=0, sticky="ew")
        
        self.status_label = customtkinter.CTkLabel(
            self.footer, 
            textvariable=self.status_var, 
            anchor="w", 
            text_color=footer_colors.get("text", colors.get("foreground", None))
        )
        self.status_label.pack(side="left", fill="both", padx=8)
        
        self.user_var = customtkinter.StringVar(value="")
        self.user_label = customtkinter.CTkLabel(
            self.footer, 
            textvariable=self.user_var,
            anchor="e", 
            text_color=footer_colors.get("muted", colors.get("muted", None))
        )
        self.user_label.pack(side="right", padx=8)
        
    def auto_connect_guest(self):
        #Conecta automáticamente como invitado al iniciar
        self.db = DatabaseConnection()
        if self.db.connect(user='rol_invitado', password='esfing3'):
            self.current_role = "invitado"
            self.current_user = "Invitado"
            self.status_var.set("Conectado como Invitado")
            self.user_var.set(f"Invitado | IP: {self.user_ip}")
            self.update_ui_permissions()
            self.check_ip_status()
        else:
            self.status_var.set("Error de conexion")
            
    def check_ip_status(self):
        #Verifica si la IP del usuario está registrada en el sistema
        if not self.db:
            return
            
        try:
            query = "SELECT id_ip, estado FROM IPs WHERE direccion_ip = %s"
            result = self.db.fetch_data(query, (self.user_ip,))
            
            if not result or len(result) == 0:
                self.ip_unregistered = True
                self.create_ip_notification()
                # Activar badge en el botón de Notificaciones cuando la IP no está registrada
                self.set_notificaciones_alert(True)
            elif result[0]['estado'] in ['Bloqueada', 'Maliciosa']:
                self.ip_unregistered = False
                InvitadoView.show_blocked_message(self)
                # Mantener badge desactivado para estados diferentes a "no registrada"
                self.set_notificaciones_alert(False)
            else:
                # IP registrada: desactivar badge si estaba activo
                self.ip_unregistered = False
                self.set_notificaciones_alert(False)
        except Exception as e:
            print(f"Error verificando IP: {e}")
    
    def create_ip_notification(self):
        #Crea una notificación para IP no registrada
        if self.db:
            try:
                query = """
                    INSERT INTO Alertas (tipo_alerta, fecha_alerta, gravedad, estado, id_analista_asignado)
                    VALUES (%s, NOW(), 'Media', 'Pendiente', NULL)
                """
                self.db.execute_query(query, (f'IP no registrada: {self.user_ip}',))
                # Asegurar badge activo cuando se crea una alerta por IP no registrada
                self.ip_unregistered = True
                self.set_notificaciones_alert(True)
            except Exception as e:
                print(f"Error creando notificacion: {e}")

    def set_notificaciones_alert(self, active: bool):
        #Muestra/oculta un pequeño símbolo de alerta en el botón de Notificaciones.
        #active: True para mostrar el símbolo de alerta, False para ocultarlo.
        try:
            if active and not self._notificaciones_badge_active:
                self.notificaciones_button.configure(text=f"{self._notificaciones_base_text} ⚠")
                self._notificaciones_badge_active = True
            elif not active and self._notificaciones_badge_active:
                self.notificaciones_button.configure(text=self._notificaciones_base_text)
                self._notificaciones_badge_active = False
        except Exception:
            # No bloquear la app si por alguna razón no se puede actualizar el botón
            pass
    
    def show_login_dialog(self):
        #Muestra el diálogo de login
        if self.current_role != "invitado" or self.usuario_id:
            self.logout()
            return
            
        login_window = customtkinter.CTkToplevel(self.root)
        login_window.title("Iniciar Sesion")
        login_window.geometry("400x250")
        login_window.transient(self.root)
        login_window.grab_set()
        
        login_window.update_idletasks()
        x = (login_window.winfo_screenwidth() // 2) - (400 // 2)
        y = (login_window.winfo_screenheight() // 2) - (250 // 2)
        login_window.geometry(f"400x250+{x}+{y}")
        
        btn_colors = widget_colors.get("button", {})
        
        title_label = customtkinter.CTkLabel(
            login_window, 
            text="Iniciar Sesion",
            font=("Arial", 18, "bold")
        )
        title_label.pack(pady=20)
        
        user_label = customtkinter.CTkLabel(login_window, text="Usuario:")
        user_label.pack(pady=5)
        user_entry = customtkinter.CTkEntry(login_window, width=300, placeholder_text="nombre_usuario")
        user_entry.pack(pady=5)
        
        pass_label = customtkinter.CTkLabel(login_window, text="Contrasena:")
        pass_label.pack(pady=5)
        pass_entry = customtkinter.CTkEntry(login_window, width=300, show="*", placeholder_text="contrasena")
        pass_entry.pack(pady=5)
        
        error_var = customtkinter.StringVar(value="")
        error_label = customtkinter.CTkLabel(
            login_window, 
            textvariable=error_var,
            text_color="red"
        )
        error_label.pack(pady=5)
        
        def do_login():
            username = user_entry.get().strip()
            password = pass_entry.get().strip()
            
            if not username or not password:
                error_var.set("Por favor complete todos los campos")
                return
            
            if self.authenticate_user(username, password):
                login_window.destroy()
            else:
                error_var.set("Usuario o contrasena incorrectos")
                pass_entry.delete(0, 'end')
        
        login_btn = customtkinter.CTkButton(
            login_window,
            text="Iniciar Sesion",
            command=do_login,
            fg_color=btn_colors.get("fg_color", colors.get("primary", None)),
            hover_color=btn_colors.get("hover_color", None),
            text_color=btn_colors.get("text_color", None),
            width=200
        )
        login_btn.pack(pady=15)
        
        pass_entry.bind('<Return>', lambda e: do_login())
        user_entry.focus()
        
    def authenticate_user(self, username: str, password: str) -> bool:
        
        #Autentica un usuario contra la base de datos
        temp_db = DatabaseConnection()
        if not temp_db.connect(user='rol_invitado', password='esfing3'):
            return False
        
        query = """
            SELECT u.id_usuario, u.nombre_usuario, u.contrasena_hash, u.cargo, 
                r.id_rol, r.nombre_rol
            FROM Usuarios u
            JOIN Roles r ON u.id_rol = r.id_rol
            WHERE u.nombre_usuario = %s AND u.contrasena_hash = %s
        """
        result = temp_db.fetch_data(query, (username, password))
        temp_db.disconnect()
        
        if not result or len(result) == 0:
            return False
        
        user_data = result[0]
        
        if self.db:
            self.db.disconnect()
        
        role_map = {
            1: ('rol_admin', 'drag0na', 'admin'),
            2: ('rol_analista', 'mant1cora', 'analista'),
            3: ('rol_invitado', 'esfing3', 'invitado')
        }
        
        role_id = user_data['id_rol']
        if role_id not in role_map:
            return False
        
        db_user, db_pass, role_name = role_map[role_id]
        
        self.db = DatabaseConnection()
        if self.db.connect(user=db_user, password=db_pass):
            self.current_user = user_data['nombre_usuario']
            self.current_role = role_name
            self.usuario_id = user_data['id_usuario']
            
            role_display = user_data['nombre_rol']
            self.status_var.set(f"Conectado como {role_display}")
            self.user_var.set(f"{self.current_user} ({role_display})")
            
            self.update_ui_permissions()
            
            for widget in self.result_frame.winfo_children():
                widget.destroy()
            
            welcome = customtkinter.CTkLabel(
                self.result_frame,
                text=f"Bienvenido/a, {self.current_user}",
                font=("Arial", 16, "bold")
            )
            welcome.pack(pady=20)
            
            cargo_label = customtkinter.CTkLabel(
                self.result_frame,
                text=f"Cargo: {user_data['cargo']}",
                font=("Arial", 12)
            )
            cargo_label.pack(pady=5)
            
            return True
        
        return False
    
    def update_ui_permissions(self):
        #Actualiza la UI según los permisos del rol actual
        self.mis_datos_button.pack_forget()
        self.notificaciones_button.pack_forget()
        self.solicitar_ip_button.pack_forget()
        self.usuarios_button.pack_forget()
        self.reportes_button.pack_forget()
        self.alertas_button.pack_forget()
        self.logs_button.pack_forget()
        self.ip_management_button.pack_forget()
        
        if self.current_role == "admin":
            self.login_button.configure(text="Cerrar Sesion")
            self.mis_datos_button.pack(pady=8, padx=20, fill="x")
            self.alertas_button.pack(pady=8, padx=20, fill="x")
            self.logs_button.pack(pady=8, padx=20, fill="x")
            self.reportes_button.pack(pady=8, padx=20, fill="x")
            self.usuarios_button.pack(pady=8, padx=20, fill="x")
            self.ip_management_button.pack(pady=8, padx=20, fill="x")
            
        elif self.current_role == "analista":
            self.login_button.configure(text="Cerrar Sesion")
            self.mis_datos_button.pack(pady=8, padx=20, fill="x")
            self.alertas_button.pack(pady=8, padx=20, fill="x")
            self.logs_button.pack(pady=8, padx=20, fill="x")
            self.reportes_button.pack(pady=8, padx=20, fill="x")
            
        else:
            if self.usuario_id:
                self.login_button.configure(text="Cerrar Sesion")
                self.mis_datos_button.pack(pady=8, padx=20, fill="x")
                self.notificaciones_button.pack(pady=8, padx=20, fill="x")
            else:
                self.login_button.configure(text="Iniciar Sesion")
                self.notificaciones_button.pack(pady=8, padx=20, fill="x")
                # El botón de solicitud se mostrará dentro del panel de notificaciones
    
    def logout(self):
        #Cierra sesión y vuelve a modo invitado
        if self.db:
            self.db.disconnect()
        
        self.current_user = None
        self.usuario_id = None
        self.auto_connect_guest()
        
        for widget in self.result_frame.winfo_children():
            widget.destroy()
        
        logout_label = customtkinter.CTkLabel(
            self.result_frame,
            text="Sesion cerrada. Ahora esta como invitado.",
            font=("Arial", 14)
        )
        logout_label.pack(pady=20)
    
    # Invitado 
    def show_notificaciones(self):
        #Muestra notificaciones de red para el usuario
        InvitadoView.show_notificaciones(self)
    
    def solicitar_acceso_ip(self):
        #Solicita acceso para la IP del usuario
        InvitadoView.solicitar_acceso_ip(self)
    
    def show_mis_datos(self):
        #Muestra los datos del usuario actual
        InvitadoView.show_mis_datos(self)
    
    # Analista 
    def show_alertas(self):
        #Muestra las alertas del sistema
        if self.current_role == "admin":
            AdminView.show_alertas_admin(self)
        else:
            AnalistaView.show_alertas(self)
    
    def show_logs(self):
        #Muestra los logs del firewall
        AnalistaView.show_logs(self)
    
    def show_reportes(self):
        #Muestra los reportes del sistema
        AnalistaView.show_reportes(self)
    
    # Admin 
    def show_usuarios(self):
        #Muestra los usuarios del sistema (solo admin)
        AdminView.show_usuarios(self)
    
    def show_ip_management(self):
        #Muestra la gestión completa de IPs (solo admin)
        AdminView.show_ip_management(self)
    
    def on_closing(self):
        #Cierra la aplicación correctamente
        if self.db:
            self.db.disconnect()
        self.root.destroy()

if __name__ == "__main__":
    print("Iniciando aplicacion J.A.B.I.P...")
    app_root = customtkinter.CTk()
    app = FirewallApp(app_root)
    app_root.protocol("WM_DELETE_WINDOW", app.on_closing)
    print("Ventana creada, mostrando interfaz...")
    app_root.mainloop()
