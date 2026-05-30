from scanner.discover import scan_ports, get_hostname
from scanner.export import export_csv
from scanner.workers import run_threads
from scanner.network import get_local_network
from scanner.stats import calculate_stats
from scanner.fingerprint import identify_device

import time

print("=" * 50)
print("NETWORK SCANNER PRO v2.3")
print("=" * 50)

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

        vendor, device_type = identify_device(
            hostname,
            services
        )

        print(f"[+] Host: {ip}")
        print(f"    Nombre: {hostname}")
        print(f"    Fabricante: {vendor}")
        print(f"    Tipo: {device_type}")

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
            "device_type": device_type,
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

    report = export_csv(results)

    print("\nReporte guardado:")
    print(report)

else:

    print("\nNo se encontraron hosts.")
