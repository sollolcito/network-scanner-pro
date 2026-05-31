from datetime import datetime


def export_html(results, stats, elapsed):

    timestamp = datetime.now().strftime(
        "%Y%m%d_%H%M%S"
    )

    filename = (
        f"reports/scan_{timestamp}.html"
    )

    sorted_results = sorted(
        results,
        key=lambda x: (
            x["vendor"],
            x["hostname"]
        )
    )

    html = f"""
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Network Scanner Pro</title>

<style>

body {{
    font-family: Arial, sans-serif;
    margin: 30px;
    background-color: #f5f5f5;
}}

h1 {{
    color: #222;
}}

.dashboard {{
    background: white;
    padding: 15px;
    border-radius: 10px;
    margin-bottom: 20px;
    border: 1px solid #ddd;
}}

table {{
    border-collapse: collapse;
    width: 100%;
    background: white;
}}

th {{
    background: #2c3e50;
    color: white;
    padding: 10px;
}}

td {{
    padding: 8px;
    border: 1px solid #ddd;
}}

tr:hover {{
    background-color: #f0f0f0;
}}

.workstation {{
    background-color: #dbeafe;
}}

.accesspoint {{
    background-color: #dcfce7;
}}

.network {{
    background-color: #fef3c7;
}}

.unknown {{
    background-color: #e5e7eb;
}}

.risk-low {{
    background-color: #dcfce7;
    font-weight: bold;
}}

.risk-medium {{
    background-color: #fef3c7;
    font-weight: bold;
}}

.risk-high {{
    background-color: #fed7aa;
    font-weight: bold;
}}

.risk-critical {{
    background-color: #fecaca;
    font-weight: bold;
}}

</style>

</head>

<body>

<h1>NETWORK SCANNER PRO</h1>

<div class="dashboard">

<p>
<strong>Fecha:</strong>
{datetime.now().strftime("%d/%m/%Y %H:%M:%S")}
</p>

<p>
<strong>Hosts encontrados:</strong>
{len(results)}
</p>

<p>
<strong>Tiempo total:</strong>
{elapsed} segundos
</p>

<h3>Servicios Detectados</h3>

<ul>
"""

    for service, count in stats.items():

        html += (
            f"<li><strong>{service}</strong>: "
            f"{count}</li>"
        )

    html += """
</ul>

</div>

<table>

<tr>
<th>IP</th>
<th>Hostname</th>
<th>Fabricante</th>
<th>Modelo</th>
<th>Categoria</th>
<th>Riesgo</th>
<th>Servicios</th>
</tr>
"""

    for host in sorted_results:

        services = []

        for item in host["services"]:

            services.append(
                f"{item['service']}:{item['port']}"
            )

        category = host["category"].lower()

        css_class = "unknown"

        if "workstation" in category:
            css_class = "workstation"

        elif "access point" in category:
            css_class = "accesspoint"

        elif "network" in category:
            css_class = "network"

        risk = host.get(
            "risk",
            "DESCONOCIDO"
        )

        risk_class = ""

        if risk == "BAJO":
            risk_class = "risk-low"

        elif risk == "MEDIO":
            risk_class = "risk-medium"

        elif risk == "ALTO":
            risk_class = "risk-high"

        elif risk == "CRITICO":
            risk_class = "risk-critical"

        html += f"""
<tr class="{css_class}">
<td>{host['ip']}</td>
<td>{host['hostname']}</td>
<td>{host['vendor']}</td>
<td>{host['model']}</td>
<td>{host['category']}</td>
<td class="{risk_class}">{risk}</td>
<td>{", ".join(services)}</td>
</tr>
"""

    html += """
</table>

</body>
</html>
"""

    with open(
        filename,
        "w",
        encoding="utf-8"
    ) as file:

        file.write(html)

    return filename
