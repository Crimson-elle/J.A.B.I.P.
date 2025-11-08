import mysql.connector
from mysql.connector import Error
import os
from typing import Optional, Dict, Any, List

class DatabaseConnection:
    #Maneja la conexión a la base de datos MySQL
    
    def __init__(self):
        self.connection = None
        self.cursor = None
        
    def connect(self, user: str, password: str, host: str = 'localhost', 
                database: str = 'saas_firewall_db') -> bool:
        
        #Establece conexión con la base de datos
        
        try:
            self.connection = mysql.connector.connect(
                host=host,
                user=user,
                password=password,
                database=database,
                charset='utf8mb4',
                collation='utf8mb4_general_ci'
            )
            
            if self.connection.is_connected():
                self.cursor = self.connection.cursor(dictionary=True)
                db_info = self.connection.get_server_info()
                print(f"✓ Conectado exitosamente a MySQL Server v{db_info}")
                return True
                
        except Error as e:
            print(f"✗ Error al conectar a MySQL: {e}")
            return False
            
    def disconnect(self):
        #Cierra la conexión a la base de datos
        if self.cursor:
            self.cursor.close()
        if self.connection and self.connection.is_connected():
            self.connection.close()
            print("✓ Conexión cerrada")
            
    def execute_query(self, query: str, params: tuple = None) -> bool:
        #Ejecuta una query de modificación (INSERT, UPDATE, DELETE)
        try:
            if params:
                self.cursor.execute(query, params)
            else:
                self.cursor.execute(query)
            self.connection.commit()
            print(f"✓ Query ejecutada: {self.cursor.rowcount} fila(s) afectada(s)")
            return True
        except Error as e:
            print(f"✗ Error ejecutando query: {e}")
            self.connection.rollback()
            return False
            
    def fetch_data(self, query: str, params: tuple = None) -> List[Dict[str, Any]]:
        
        #Ejecuta una query de consulta (SELECT) y retorna los resultados
        try:
            if params:
                self.cursor.execute(query, params)
            else:
                self.cursor.execute(query)
            results = self.cursor.fetchall()
            return results
        except Error as e:
            print(f"✗ Error consultando datos: {e}")
            return []
            
    def call_procedure(self, procedure_name: str, args: tuple = ()) -> List[Dict[str, Any]]:
        
        #Llama a un stored procedure
        try:
            self.cursor.callproc(procedure_name, args)
            results = []
            for result in self.cursor.stored_results():
                results.extend(result.fetchall())
            return results
        except Error as e:
            print(f"✗ Error llamando procedimiento: {e}")
            return []

def get_admin_connection() -> Optional[DatabaseConnection]:
    #Obtiene conexión con privilegios de administrador
    db = DatabaseConnection()
    if db.connect(user='rol_admin', password='drag0na'):
        return db
    return None

def get_analista_connection() -> Optional[DatabaseConnection]:
    #Obtiene conexión con privilegios de analista
    db = DatabaseConnection()
    if db.connect(user='rol_analista', password='mant1cora'):
        return db
    return None

def get_invitado_connection() -> Optional[DatabaseConnection]:
    #Obtiene conexión con privilegios de invitado
    db = DatabaseConnection()
    if db.connect(user='rol_invitado', password='esfing3'):
        return db
    return None


if __name__ == "__main__":
    print("\n=== Ejemplo 1: Conexión como Administrador ===")
    db_admin = get_admin_connection()
    if db_admin:
        usuarios = db_admin.fetch_data("SELECT id_usuario, nombre_usuario, email, cargo FROM Usuarios LIMIT 5")
        print(f"\nUsuarios en el sistema:")
        for user in usuarios:
            print(f"  - {user['nombre_usuario']}: {user['cargo']}")
        db_admin.disconnect()
    
    print("\n=== Ejemplo 2: Conexión como Analista ===")
    db_analista = get_analista_connection()
    if db_analista:
        alertas = db_analista.fetch_data(
            "SELECT id_alerta, tipo_alerta, gravedad, estado FROM Alertas WHERE estado = 'Pendiente'"
        )
        print(f"\nAlertas pendientes: {len(alertas)}")
        for alerta in alertas:
            print(f"  - Alerta #{alerta['id_alerta']}: {alerta['tipo_alerta']} ({alerta['gravedad']})")
        db_analista.disconnect()
    
    print("\n=== Ejemplo 3: Conexión como Invitado ===")
    db_invitado = get_invitado_connection()
    if db_invitado:
        datos = db_invitado.fetch_data("SELECT nombre_usuario, email FROM Vista_1 LIMIT 1")
        print(f"\nDatos de usuario:")
        for dato in datos:
            print(f"  Usuario: {dato['nombre_usuario']}")
            print(f"  Email: {dato['email']}")
            
        logs = db_invitado.call_procedure('SP_ObtenerLogsPorUsuario', (7,))
        print(f"\nLogs del usuario: {len(logs)} registros")
        
        db_invitado.disconnect()