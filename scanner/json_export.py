import json
from datetime import datetime


def export_json(results):

    timestamp = datetime.now().strftime(
        "%Y%m%d_%H%M%S"
    )

    filename = (
        f"reports/scan_{timestamp}.json"
    )

    with open(
        filename,
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            results,
            file,
            indent=4,
            ensure_ascii=False
        )

    return filename
