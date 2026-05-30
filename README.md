Network Scanner Pro v1.0

Descripción

Network Scanner Pro es una herramienta desarrollada en Python para descubrir dispositivos activos en una red local, identificar servicios comunes y generar reportes en formato CSV.

El proyecto fue diseñado con una arquitectura modular para facilitar futuras mejoras y servir como base para herramientas de administración de redes y ciberseguridad.

---

Características

- Escaneo de una subred completa.
- Detección de hosts activos.
- Identificación de servicios comunes:
  - SSH (22)
  - HTTP (80)
  - HTTPS (443)
  - SMB (445)
  - RDP (3389)
- Resolución de hostname.
- Exportación de resultados a CSV.
- Compatible con Linux y Termux.

---

Estructura del Proyecto

network-scanner-pro/

├── scanner/

│   ├── discover.py

│   └── export.py

├── reports/

├── main.py

└── README.md

---

Instalación

Clonar el repositorio:

git clone https://github.com/sollolcito/network-scanner-pro.git

Entrar al proyecto:

cd network-scanner-pro

---

Ejecución

python main.py

Ingresar una red en formato:

192.168.0

Ejemplo:

Ingrese red (ej: 192.168.0): 192.168.0

---

Ejemplo de salida

[+] Host: 192.168.0.1

Nombre: router

HTTP (Puerto 80)

HTTPS (Puerto 443)

[+] Host: 192.168.0.15

Nombre: PC-OFICINA

SMB (Puerto 445)

---

Reportes

Los resultados se almacenan automáticamente en la carpeta:

reports/

Formato:

scan_AAAAMMDD_HHMMSS.csv

---

Tecnologías Utilizadas

- Python
- Socket Programming
- CSV
- Networking
- TCP/IP

---

Próximas Versiones

v2.0

- Escaneo concurrente (multithreading)
- Mejor rendimiento

v3.0

- Reportes HTML
- Estadísticas visuales

v4.0

- Dashboard Web con Flask
- Historial de escaneos

---

Autor

Proyecto desarrollado como parte de un portafolio de aprendizaje en redes, IT y ciberseguridad.
