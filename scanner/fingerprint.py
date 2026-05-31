def identify_device(hostname, services):

    hostname = hostname.lower()

    ports = []

    for service in services:
        ports.append(service["port"])

    # ======================
    # UBIQUITI
    # ======================

    if "uap-ac-m-pro" in hostname:
        return (
            "Ubiquiti",
            "UAP-AC-M-Pro",
            "Access Point"
        )

    if "uap" in hostname:
        return (
            "Ubiquiti",
            "UAP Series",
            "Access Point"
        )

    if "u6pro" in hostname:
        return (
            "Ubiquiti",
            "U6 Pro",
            "WiFi 6 Access Point"
        )

    if "unifi" in hostname:
        return (
            "Ubiquiti",
            "UniFi",
            "Network Device"
        )

    # ======================
    # WINDOWS
    # ======================

    if 445 in ports and 3389 in ports:

        return (
            "Microsoft",
            "Windows",
            "Workstation"
        )

    # ======================
    # SERVIDORES
    # ======================

    if 22 in ports and 80 in ports:

        return (
            "Desconocido",
            "Linux",
            "Server / Network Device"
        )

    if 22 in ports:

        return (
            "Desconocido",
            "SSH Device",
            "Network Device"
        )

    if 80 in ports and 443 in ports:

        return (
            "Desconocido",
            "Web Device",
            "Web Service"
        )

    # ======================
    # DEFAULT
    # ======================

    return (
        "Desconocido",
        "Unknown",
        "Unknown Device"
    )
