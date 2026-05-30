def calculate_stats(results):

    stats = {
        "SSH": 0,
        "HTTP": 0,
        "HTTPS": 0,
        "SMB": 0,
        "RDP": 0
    }

    for host in results:

        for service in host["services"]:

            name = service["service"]

            if name in stats:
                stats[name] += 1

    return stats
