import socket

def get_local_network():

    try:

        s = socket.socket(
            socket.AF_INET,
            socket.SOCK_DGRAM
        )

        s.connect(("8.8.8.8", 80))

        ip = s.getsockname()[0]

        s.close()

        parts = ip.split(".")

        return ".".join(parts[:3])

    except Exception:

        return None
