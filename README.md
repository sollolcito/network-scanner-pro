# Network Scanner Pro

Network Scanner Pro es una herramienta de descubrimiento y análisis de red desarrollada en Python.

Permite detectar dispositivos con servicios accesibles en una red local, identificar nombres de host, clasificar dispositivos, generar reportes CSV y obtener estadísticas de la infraestructura analizada.

---

## Características

### Descubrimiento de Red

- Escaneo de redes IPv4 (/24)
- Detección automática de red local
- Descubrimiento de dispositivos con servicios accesibles

### Detección de Servicios

Actualmente detecta:

- SSH (22)
- HTTP (80)
- HTTPS (443)
- SMB (445)
- RDP (3389)

### Identificación de Dispositivos

Clasificación automática basada en hostname y servicios detectados:

- Equipos Windows
- Dispositivos UniFi
- Access Points Ubiquiti
- Dispositivos con SSH
- Servidores Web
- Dispositivos desconocidos

### Reportes

- Exportación CSV
- Hostname
- Fabricante estimado
- Tipo de dispositivo
- Servicios detectados

### Estadísticas

Generación automática de estadísticas:

- Total de hosts detectados
- Cantidad de servicios por tipo
- Tiempo total de escaneo

### Rendimiento

- Escaneo concurrente mediante multithreading
- Optimizado para Python 3
- Compatible con Android (Termux), Linux y Windows

---

## Tecnologías Utilizadas

- Python 3
- Socket Programming
- ThreadPoolExecutor
- CSV Reporting
- Git
- GitHub

---

## Estructura del Proyecto

```text
network-scanner-pro/

├── main.py
├── reports/
│
├── scanner/
│   ├── discover.py
│   ├── export.py
│   ├── fingerprint.py
│   ├── network.py
│   ├── stats.py
│   └── workers.py
│
└── README.md
