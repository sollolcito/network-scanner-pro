import socket

SERVICES = {
    22: "SSH",
    80: "HTTP",
    443: "HTTPS",
    445: "SMB",
    3389: "RDP"
}

def scan_ports(ip):

    detected_services = []

    for port, service in SERVICES.items():

        try:

            sock = socket.socket(
                socket.AF_INET,
                socket.SOCK_STREAM
            )

            sock.settimeout(0.1)

            result = sock.connect_ex((ip, port))

            sock.close()

            if result == 0:

                detected_services.append({
                    "port": port,
                    "service": service
                })

        except Exception:
            pass

    return detected_services


def get_hostname(ip):

    try:
        hostname = socket.gethostbyaddr(ip)[0]
        return hostname

    except Exception:
        return "Desconocido"
