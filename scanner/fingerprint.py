def identify_device(hostname, services):

    hostname = hostname.lower()

    ports = []

    for service in services:
        ports.append(service["port"])

    # Ubiquiti

    if "uap" in hostname:
        return "Ubiquiti", "Access Point"

    if "u6pro" in hostname:
        return "Ubiquiti", "WiFi 6 Access Point"

    if "unifi" in hostname:
        return "Ubiquiti", "UniFi Device"

    # Windows

    if 445 in ports and 3389 in ports:
        return "Microsoft", "Windows Workstation"

    # Linux / Network Device

    if 22 in ports and 80 in ports:
        return "Desconocido", "Linux Server / Network Device"

    if 22 in ports:
        return "Desconocido", "SSH Enabled Device"

    if 80 in ports and 443 in ports:
        return "Desconocido", "Web Device"

    return "Desconocido", "Unknown Device"
