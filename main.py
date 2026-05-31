from scanner.discover import scan_ports, get_hostname
from scanner.export import export_csv
from scanner.html_report import export_html
from scanner.json_export import export_json
from scanner.workers import run_threads
from scanner.network import get_local_network
from scanner.stats import calculate_stats
from scanner.fingerprint import identify_device
from scanner.risk import calculate_risk
from scanner.database import (
    init_database,
    save_scan
)

from datetime import datetime
import time

print("=" * 50)
print("NETWORK SCANNER PRO v3.0")
print("=" * 50)

init_database()

detected = get_local_network()

if detected:

    print(f"\nRed detectada: {detected}.0/24")

    choice = input(
        "¿Usar esta red? (s/n): "
    ).strip().lower()

    if choice == "s":
        network = detected
    else:
        network = input(
            "Ingrese red manualmente: "
        ).strip()

else:

    network = input(
        "Ingrese red (ej: 192.168.1): "
    ).strip()

parts = network.split(".")

if len(parts) != 3:

    print("Formato inválido.")
    exit()

print("\nEscaneando red...\n")

start_time = time.time()

ips = []

for i in range(1, 255):
    ips.append(f"{network}.{i}")


def scan_host(ip):

    services = scan_ports(ip)

    if services:

        hostname = get_hostname(ip)

        vendor, model, category = identify_device(
            hostname,
            services
        )

        risk = calculate_risk(
            services
        )

        print(f"[+] Host: {ip}")
        print(f"    Nombre: {hostname}")
        print(f"    Fabricante: {vendor}")
        print(f"    Modelo: {model}")
        print(f"    Categoria: {category}")
        print(f"    Riesgo: {risk}")

        for item in services:

            print(
                f"    {item['service']} "
                f"(Puerto {item['port']})"
            )

        print()

        return {
            "ip": ip,
            "hostname": hostname,
            "vendor": vendor,
            "model": model,
            "category": category,
            "risk": risk,
            "services": services
        }

    return None


results = run_threads(
    scan_host,
    ips,
    workers=20
)

elapsed = round(
    time.time() - start_time,
    2
)

stats = calculate_stats(results)

print("=" * 50)
print("ESTADISTICAS")
print("=" * 50)

for service, count in stats.items():

    print(
        f"{service:<6}: {count}"
    )

print()

print("=" * 50)
print("ESCANEO FINALIZADO")
print("=" * 50)

print(
    f"Hosts encontrados: {len(results)}"
)

print(
    f"Tiempo total: {elapsed} segundos"
)

if results:

    scan_date = datetime.now().strftime(
        "%Y-%m-%d %H:%M:%S"
    )

    save_scan(
        results,
        scan_date
    )

    csv_report = export_csv(results)

    html_report = export_html(
        results,
        stats,
        elapsed
    )

    json_report = export_json(
        results
    )

    print("\nReportes guardados:")
    print(csv_report)
    print(html_report)
    print(json_report)

    print(
        "\nInventario SQLite actualizado."
    )

else:

    print("\nNo se encontraron hosts.")
