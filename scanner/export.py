import csv
from datetime import datetime


def export_csv(results):

    timestamp = datetime.now().strftime(
        "%Y%m%d_%H%M%S"
    )

    filename = (
        f"reports/scan_{timestamp}.csv"
    )

    with open(
        filename,
        "w",
        newline=""
    ) as file:

        writer = csv.writer(file)

        writer.writerow([
            "IP",
            "HOSTNAME",
            "FABRICANTE",
            "MODELO",
            "CATEGORIA",
            "RIESGO",
            "SERVICIOS"
        ])

        for host in results:

            services = []

            for item in host["services"]:

                services.append(
                    f"{item['service']}:{item['port']}"
                )

            writer.writerow([
                host["ip"],
                host["hostname"],
                host["vendor"],
                host["model"],
                host["category"],
                host["risk"],
                ", ".join(services)
            ])

    return filename
