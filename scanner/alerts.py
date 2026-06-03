from datetime import datetime
import os


ALERT_FILE = (
    "reports/alerts.log"
)


def save_alerts(
    new_devices,
    removed_devices
):

    if (
        not new_devices
        and
        not removed_devices
    ):
        return

    os.makedirs(
        "reports",
        exist_ok=True
    )

    now = datetime.now().strftime(
        "%d/%m/%Y %H:%M:%S"
    )

    with open(
        ALERT_FILE,
        "a",
        encoding="utf-8"
    ) as file:

        file.write(
            f"\n[{now}]\n"
        )

        for ip in new_devices:

            file.write(
                f"NUEVO → {ip}\n"
            )

        for ip in removed_devices:

            file.write(
                f"DESAPARECIDO → {ip}\n"
            )
