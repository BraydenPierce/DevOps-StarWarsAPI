import requests
from concurrent.futures import ThreadPoolExecutor, as_completed

BASE = "https://swapi.info/api"

def fetch_json(url):
    resp = requests.get(url, timeout=10)
    resp.raise_for_status()
    return resp.json()

def get_all_starships():
    url = f"{BASE}/starships/"
    starships = []
    while url:
        data = fetch_json(url)
        if isinstance(data, dict):
            results = data.get("results", []) or []
            next_url = data.get("next")
        elif isinstance(data, list):
            results = data or []
            next_url = None
        else:
            raise RuntimeError(f"Unexpected response type: {type(data)} from {url}")
        starships.extend(results)
        url = next_url
    return starships

def get_name_for(url):
    try:
        data = fetch_json(url)
        return data.get("name") or data.get("title") or url
    except Exception:
        return f"<error fetching {url}>"

def main():
    starships = get_all_starships()
    with ThreadPoolExecutor(max_workers=10) as ex:
        for idx, ship in enumerate(starships, 1):
            name = ship.get("name") or "Unknown"
            model = ship.get("model") or "Unknown model"
            pilot_urls = ship.get("pilots") or []

            print(f"{idx}. {name} — {model}")
            if not pilot_urls:
                print("   Pilots: None\n")
                continue

            futures = {ex.submit(get_name_for, u): u for u in pilot_urls}
            pilot_names = [f.result() for f in as_completed(futures)]
            for p in pilot_names:
                print(f"   - {p}")
            print()

if __name__ == "__main__":
    main()