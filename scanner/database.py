import sqlite3


DB_NAME = "network_inventory.db"


def init_database():

    conn = sqlite3.connect(
        DB_NAME
    )

    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS devices (

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        scan_date TEXT,

        network TEXT,

        ip TEXT,

        hostname TEXT,

        vendor TEXT,

        model TEXT,

        category TEXT,

        risk TEXT,

        services TEXT
    )
    """)

    conn.commit()

    conn.close()


def save_scan(
    results,
    scan_date,
    network
):

    conn = sqlite3.connect(
        DB_NAME
    )

    cursor = conn.cursor()

    for host in results:

        services = []

        for item in host["services"]:

            services.append(
                f"{item['service']}:{item['port']}"
            )

        cursor.execute(
            """
            INSERT INTO devices(

                scan_date,

                network,

                ip,

                hostname,

                vendor,

                model,

                category,

                risk,

                services

            )

            VALUES(

                ?,?,?,?,?,?,?,?,?
            )
            """,

            (

                scan_date,

                network,

                host["ip"],

                host["hostname"],

                host["vendor"],

                host["model"],

                host["category"],

                host["risk"],

                ", ".join(
                    services
                )

            )
        )

    conn.commit()

    conn.close()
