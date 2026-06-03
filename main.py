from scanner.discover import scan_ports, get_hostname
from scanner.export import export_csv
from scanner.html_report import export_html
from scanner.json_export import export_json
from scanner.workers import run_threads
from scanner.network import get_local_network

from scanner.database import (
    init_database,
    save_scan
)

from scanner.history import (
    get_last_scan,
    compare_scans
)

from scanner.stats_db import (
    get_total_scans,
    get_last_scan_date
)

from scanner.stats import (
    calculate_stats
)

from scanner.fingerprint import identify_device
from scanner.risk import calculate_risk

from scanner.alerts import (
    save_alerts
)

from datetime import datetime
import time


VERSION = "3.3"


def scan_host(ip):

    services = scan_ports(ip)

    if not services:
        return None

    hostname = get_hostname(ip)

    vendor, model, category = identify_device(
        hostname,
        services
    )

    risk = calculate_risk(
        services
    )

    return {
        "ip": ip,
        "hostname": hostname,
        "vendor": vendor,
        "model": model,
        "category": category,
        "risk": risk,
        "services": services
    }


print("=" * 50)
print(f"NETWORK SCANNER PRO v{VERSION}")
print("=" * 50)


init_database()


total_scans = get_total_scans()
last_scan_date = get_last_scan_date()

print(f"\nEscaneos guardados: {total_scans}")

if last_scan_date:
    print(f"Último escaneo: {last_scan_date}")
else:
    print("Último escaneo: ninguno")


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
        "Ingrese red manualmente: "
    ).strip()


previous_scan = get_last_scan(
    network
)


print("\nEscaneando red...\n")


targets = []

for i in range(1, 255):

    targets.append(
        f"{network}.{i}"
    )


start_time = time.time()


results = run_threads(
    scan_host,
    targets
)


end_time = time.time()


elapsed = round(
    end_time - start_time,
    2
)


scan_date = datetime.now().strftime(
    "%Y%m%d_%H%M%S"
)


print("=" * 50)
print("ESCANEO FINALIZADO")
print("=" * 50)

print(f"Red escaneada: {network}.0/24")
print(f"Hosts encontrados: {len(results)}")
print(f"Tiempo total: {elapsed} segundos")


if previous_scan:

    new_devices, removed_devices = compare_scans(
        network,
        previous_scan,
        results
    )

    print("\n" + "=" * 50)
    print("CAMBIOS DETECTADOS")
    print("=" * 50)

    print("Comparado contra último escaneo guardado.")

    print(f"\nNuevos: {len(new_devices)}")

    for ip in new_devices:
        print(f"+ {ip}")

    print(f"\nDesaparecidos: {len(removed_devices)}")

    for ip in removed_devices:
        print(f"- {ip}")

    save_alerts(
        new_devices,
        removed_devices
    )

else:

    print("\nNo hay escaneos anteriores para esta red.")


stats = calculate_stats(
    results
)


csv_file = export_csv(
    results
)

html_file = export_html(
    results,
    stats,
    elapsed
)

json_file = export_json(
    results
)


save_scan(
    results,
    scan_date,
    network
)


print("\nReportes guardados:")
print(csv_file)
print(html_file)
print(json_file)

print("\nInventario actualizado.")
