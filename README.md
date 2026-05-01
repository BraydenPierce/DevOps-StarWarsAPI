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

Choose one of these options:

- Local Python run:
	- Python 3.9+
	- `requests` package
- Docker run:
	- Docker Desktop (or Docker Engine)

## Run Locally

### 1) Create and activate a virtual environment (recommended)

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### 2) Install dependency

```powershell
pip install requests
```

### 3) Run

```powershell
py script.py
```

## Run with Docker

Build image:

```powershell
docker build -t starwars-api .
```

Run container:

```powershell
docker run --rm starwars-api
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

In `script.py`, the API base URL is:

```python
BASE = "https://swapi.info/api"
```

If that service is temporarily unavailable, switch to:

```python
BASE = "https://swapi.dev/api"
```

## Project Structure

```text
.
|-- Dockerfile
|-- README.md
`-- script.py
```

## Troubleshooting

### `ModuleNotFoundError: No module named 'requests'`

- Local run: install dependency with `pip install requests`
- Docker run: rebuild the image after Dockerfile updates:

```powershell
docker build --no-cache -t starwars-api .
```

### API shape errors (`'list' object has no attribute 'get'`)

This project already handles both list and dictionary response formats in `get_all_starships()`.

## Notes

- Pilot-name requests are done concurrently to improve performance.
- Order of pilot names for a ship may vary slightly because of concurrent execution.