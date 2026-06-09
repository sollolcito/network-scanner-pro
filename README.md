NETWORK SCANNER PRO

CLI de descubrimiento, inventario y auditoría de red desarrollado principalmente desde Android usando Termux.

---

Estado del Proyecto

Versión estable pública:

v3.1 — Mobile Stable

Estado:

- Desarrollo móvil congelado
- Repositorio público
- Próxima etapa: refactor y expansión desde PC

---

Objetivo

Construir una herramienta profesional de:

- Network Discovery
- Asset Inventory
- Auditoría de red
- Clasificación de dispositivos
- Seguimiento histórico de cambios

Sin dependencias pesadas y manteniendo una arquitectura simple.

---

Funcionalidades

Descubrimiento

- Descubrimiento automático de red local
- Escaneo por rango /24
- Escaneo TCP

Puertos monitoreados:

- SSH (22)
- HTTP (80)
- HTTPS (443)
- SMB (445)
- RTSP (554)
- RDP (3389)
- HTTP-ALT (8080)

---

Rendimiento

- Multithreading
- Escaneo paralelo
- Detección rápida de hosts

---

Identificación

- Resolución de hostname
- Fingerprinting básico
- Detección de fabricante
- Clasificación por tipo

Ejemplos:

- Ubiquiti
- Windows
- Linux
- Access Point
- Network Device

---

Riesgo

Evaluación automática:

- BAJO
- MEDIO
- ALTO
- CRÍTICO

---

Exportación

Formatos soportados:

- CSV
- HTML
- JSON

---

Inventario

Base de datos:

SQLite

Características:

- Persistencia local
- Historial de escaneos
- Comparación entre escaneos
- Inventario separado por red

---

Arquitectura

network-scanner-pro/

main.py

scanner/

discover.py
network.py
workers.py

fingerprint.py
risk.py

database.py
history.py

export.py
html_report.py
json_export.py

stats.py

reports/

network_inventory.db

---

Roadmap

v1

- Escaneo básico

v2

- Multithreading
- Auto detección
- Estadísticas
- Fingerprinting
- Clasificación
- HTML
- JSON
- Riesgo

v3

- SQLite
- Historial
- Comparación entre escaneos
- Inventario por red

---

Próxima etapa (PC)

v4

Objetivos:

- Device dataclass
- Repository Pattern
- Tests
- Refactor de exportadores
- Separación CLI
- Arquitectura más limpia

No se planea agregar funcionalidades nuevas antes del refactor.

---

Instalación

Clonar:

git clone https://github.com/sollolcito/network-scanner-pro.git

Entrar:

cd network-scanner-pro

Ejecutar:

python main.py

---

Capturas

Los reportes generados se almacenan en:

reports/

Formatos:

scan.csv
scan.html
scan.json

---

Tecnologías

- Python 3.13
- SQLite
- Git
- GitHub
- Termux
- Android

---

Licencia

Este repositorio se publica con fines educativos y de portfolio.

Reservados los derechos sobre futuras versiones privadas y extensiones comerciales.

---

Nota del Autor

Este proyecto fue desarrollado y evolucionado principalmente desde un teléfono Android utilizando Termux.

El objetivo fue demostrar capacidad de aprendizaje, diseño incremental y construcción de herramientas reales con recursos limitados.

Última versión móvil:

v3.1 — Mobile Stablex
