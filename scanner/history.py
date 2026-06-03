import sqlite3


DB_NAME = "network_inventory.db"


def get_last_scan(network):

    conn = sqlite3.connect(DB_NAME)

    cursor = conn.cursor()

    cursor.execute("""
        SELECT ip, hostname, vendor, model, category, risk, services
        FROM devices
        WHERE network = ?
        AND scan_date = (
            SELECT MAX(scan_date)
            FROM devices
            WHERE network = ?
        )
    """, (network, network))

    rows = cursor.fetchall()

    conn.close()

    return rows


def compare_scans(
    network,
    previous_scan,
    current_scan
):

    if not previous_scan:

        return (
            [],
            []
        )

    previous_ips = set()

    for row in previous_scan:

        previous_ips.add(
            row[0]
        )

    current_ips = set()

    for host in current_scan:

        current_ips.add(
            host["ip"]
        )

    new_devices = list(
        current_ips - previous_ips
    )

    removed_devices = list(
        previous_ips - current_ips
    )

    return (
        new_devices,
        removed_devices
    )
