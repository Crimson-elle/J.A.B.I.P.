# Sistema de Gestión de Seguridad de Firewall: J.A.B.I.P.

## Descripción general del proyecto

El Sistema de Gestión de Seguridad de Firewall (SGS-AF) es una aplicación de escritorio diseñada para simular la gestión de eventos de seguridad de un entorno de red. Su objetivo principal es centralizar la ingesta de logs simulados de un firewall, permitiendo a los equipos de seguridad analizar incidentes, gestionar alertas y aplicar control de acceso estricto a la información sensible.

El proyecto demuestra una arquitectura completa que abarca la interfaz de usuario, la lógica de la aplicación y una robusta capa de seguridad en la base de datos.

## Tecnologías clave

El proyecto se sustenta en un stack tecnológico robusto y especializado:

* Backend / Lógica (Python 3.9+): el lenguaje principal que maneja la lógica de la aplicación, el pre-procesamiento de logs y la gestión segura de la conexión con la base de datos.

* Base de Datos (MySQL / MariaDB): BD relacional elegida para garantizar la integridad, la estructura de los datos (logs) y la implementación de la seguridad a nivel de base de datos.

* Interfaz de Usuario (customtkinter): librería utilizada para construir una Interfaz Gráfica de Usuario (GUI) moderna, modular y con tema oscuro, adecuada para entornos de monitoreo.

* Conexión DB (mysql.connector): módulo esencial para establecer la conexión, gestionar transacciones de forma segura y realizar llamadas controladas a procedimientos almacenados.

## Arquitectura y Seguridad

La aplicación opera bajo una arquitectura de tres niveles, donde la seguridad es un principio fundamental:

### 1. Control de Acceso basado en Roles (RBAC)

El sistema soporta tres roles de usuario cada uno con un menú y permisos definidos:

* Administrador: tiene control total sobre la gestión de usuarios, configuración y datos del sistema.

* Analista: el rol operativo, técnicos en sistemas del laboratorio, con acceso de lectura a todos los logs y permisos de escritura para crear y actualizar Alertas y Reportes de incidentes.

* Invitado: el rol más restringido, trabajadores del laboratorio, limitado a consultar su información personal y logs propios.

### 2. Seguridad en la Base de Datos (DB-Level Security)

Los privilegios se otorgan a través de usuarios de MySQL (rol_admin, rol_analista, rol_invitado), aplicando los siguientes principios:

* Principio de Mínimo Privilegio: cada rol solo tiene los permisos SQL estrictamente necesarios. Por ejemplo, al rol_analista se le revoca el permiso de modificar la configuración crítica (como el estado de una IP).

* Seguridad a Nivel de Fila (RLS): el acceso del Invitado a la evidencia (Logs_Firewall) está prohibido. En su lugar, debe ejecutar un Stored Procedure (SP_ObtenerLogsPorUsuario) que filtra los datos basándose únicamente en su ID de usuario, garantizando que solo vea sus propios logs.

* Auditoría (Accountability): La tabla Auditoria se puebla automáticamente mediante Triggers de MySQL, registrando acciones críticas como cambios de contraseña, inserciones de logs y modificaciones en reportes.

## Estructura del repositorio

La lógica de programación se organiza modularmente para mantener la separación de intereses:

* Lógica DB (DB.py): centraliza la conexión y todas las consultas SQL, incluyendo el pre-procesamiento de datos de log antes del INSERT.

* Módulos de menú (invitado.py, analista.py, admin.py): contienen la interfaz gráfica y las opciones específicas para cada rol.

* SQL Scripts: archivos que definen la estructura, las Vistas, los Stored Procedures, Triggers y la matriz de permisos de la base de datos.
