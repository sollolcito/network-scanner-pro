from concurrent.futures import ThreadPoolExecutor

def run_threads(function, items, workers=20):
    results = []

    with ThreadPoolExecutor(max_workers=workers) as executor:
        futures = executor.map(function, items)

        for result in futures:
            if result:
                results.append(result)

    return results
