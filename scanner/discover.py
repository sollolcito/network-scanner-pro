import socket


SERVICES = {
    22: "SSH",
    80: "HTTP",
    443: "HTTPS",
    445: "SMB",
    554: "RTSP",
    3389: "RDP",
    8080: "HTTP-ALT"
}


def scan_ports(ip):

    detected = []

    for port, service in SERVICES.items():

        try:

            sock = socket.socket(
                socket.AF_INET,
                socket.SOCK_STREAM
            )

            sock.settimeout(
                0.1
            )

            result = sock.connect_ex(
                (
                    ip,
                    port
                )
            )

            sock.close()

            if result == 0:

                detected.append({
                    "port": port,
                    "service": service
                })

        except Exception:

            pass

    return detected


def get_hostname(ip):

    try:

        return socket.gethostbyaddr(
            ip
        )[0]

    except Exception:

        return "Desconocido"
