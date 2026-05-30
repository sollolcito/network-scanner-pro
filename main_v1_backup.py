from scanner.discover import scan_ports, get_hostname
from scanner.export import export_csv

print("=" * 50)
print("NETWORK SCANNER PRO")
print("=" * 50)

network = input(
    "Ingrese red (ej: 192.168.0): "
).strip()

parts = network.split(".")

if len(parts) != 3:

    print("Formato inválido.")
    exit()

results = []

print("\nEscaneando red...\n")

for i in range(1, 255):

    ip = f"{network}.{i}"

    services = scan_ports(ip)

    if services:

        hostname = get_hostname(ip)

        print(f"[+] Host: {ip}")
        print(f"    Nombre: {hostname}")

        for item in services:

            print(
                f"    {item['service']} "
                f"(Puerto {item['port']})"
            )

        print()

        results.append({
            "ip": ip,
            "hostname": hostname,
            "services": services
        })

print("=" * 50)
print("ESCANEO FINALIZADO")
print("=" * 50)

print(
    f"Hosts encontrados: {len(results)}"
)

if results:

    report = export_csv(results)

    print("\nReporte guardado:")
    print(report)

else:

    print("\nNo se encontraron hosts.")
