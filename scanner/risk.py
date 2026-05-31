def calculate_risk(services):

    ports = []

    for service in services:
        ports.append(service["port"])

    if 445 in ports and 3389 in ports:
        return "CRITICO"

    if 3389 in ports:
        return "ALTO"

    if 445 in ports:
        return "ALTO"

    if 22 in ports and 80 in ports:
        return "MEDIO"

    if 80 in ports:
        return "MEDIO"

    if 443 in ports:
        return "MEDIO"

    if 22 in ports:
        return "BAJO"

    return "DESCONOCIDO"
