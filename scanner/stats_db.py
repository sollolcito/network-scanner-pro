import sqlite3

DB_NAME = "network_inventory.db"


def get_total_scans():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
        SELECT COUNT(DISTINCT scan_date)
        FROM devices
    """)

    total = cursor.fetchone()[0]
    conn.close()

    return total


def get_last_scan_date():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
        SELECT MAX(scan_date)
        FROM devices
    """)

    last_date = cursor.fetchone()[0]
    conn.close()

    return last_date
