Network Scanner Pro

Network Scanner Pro es una herramienta de descubrimiento y análisis de red desarrollada en Python.

Permite detectar dispositivos con servicios accesibles en una red local, identificar nombres de host, generar reportes CSV y obtener estadísticas básicas de los servicios encontrados.

Características

- Escaneo de redes IPv4 (/24)
- Detección automática de red local
- Escaneo concurrente mediante multithreading
- Resolución de nombres de host (hostname)
- Detección de servicios comunes:
  - SSH (22)
  - HTTP (80)
  - HTTPS (443)
  - SMB (445)
  - RDP (3389)
- Generación de reportes CSV
- Estadísticas automáticas de servicios detectados
- Compatible con Linux, Android (Termux) y Windows

Tecnologías utilizadas

- Python 3
- Socket Programming
- ThreadPoolExecutor
- CSV Reporting
- Git
- GitHub

Instalación

git clone https://github.com/sollolcito/network-scanner-pro.git
cd network-scanner-pro
python main.py

Ejemplo de salida

==================================================
NETWORK SCANNER PRO
==================================================

Red detectada: 192.168.0.0/24

[+] Host: 192.168.0.42
    Nombre: ARANDNBK24523
    SMB (Puerto 445)
    RDP (Puerto 3389)

==================================================
ESTADISTICAS
==================================================

SSH   : 17
HTTP  : 6
HTTPS : 2
SMB   : 1
RDP   : 1

Historial de versiones

v1.0

- Escaneo básico de red
- Detección de servicios
- Exportación CSV

v2.0

- Escaneo multithreading
- Mejoras de rendimiento

v2.1

- Detección automática de red

v2.2

- Estadísticas de servicios
- Reportes CSV mejorados
- Inclusión de hostname en reportes

Próximas mejoras

v2.3

- Device Fingerprinting
- Identificación de fabricantes y tipos de dispositivos

v2.4

- Descubrimiento avanzado de hosts

v3.0

- Reportes HTML

Autor

Esteban Gustavo Herrera González
