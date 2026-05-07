# DevOps-StarWarsAPI

Query the Star Wars API and print every starship along with its pilots.

This project fetches starships from `swapi.info`, then resolves each starship's pilot URLs to readable names.

## Features

- Pulls all starships from the API
- Handles both paginated (`{"results": [...], "next": ...}`) and list-style (`[...]`) responses
- Resolves pilot names concurrently for faster output
- Prints readable standard output grouped by starship
- Includes a Dockerfile for containerized execution

## Prerequisites

- Docker Desktop (or Docker Engine)
- Github account (to pull from GitHub Packages)

## Run with Docker

Pull image:

```powershell
docker pull ghcr.io/braydenpierce/starwars-api:latest
```

Run container:

```powershell
docker run --rm ghcr.io/braydenpierce/starwars-api:latest
```

## Example Output

```text
1. CR90 corvette — CR90 corvette
	 Pilots: None

2. X-wing — T-65 X-wing
	 - Luke Skywalker
	 - Wedge Antilles
	 - Biggs Darklighter
	 - Jek Tono Porkins
```

## Configuration

In `script.py`, the **secure** API base URL is:

```python
BASE = "https://swapi.info/api"
```

If that service is temporarily unavailable, switch to:

```python
BASE = "https://swapi.dev/api"
```
> [!CAUTION]
> This URL base has an expired certificate as of 5/2/2026.


## Troubleshooting

### API shape errors (`'list' object has no attribute 'get'`)

This project already handles both list and dictionary response formats in `get_all_starships()`.

## Notes

- Pilot-name requests are done concurrently to improve performance.
- Order of pilot names for a ship may vary slightly because of concurrent execution.