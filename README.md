# 🚀 Flight Price Scraper

[![Python](https://img.shields.io/badge/python-3.8%2B-blue)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](./LICENSE)
[![Build Status](https://img.shields.io/badge/build-passing-brightgreen)]()
[![Stars](https://img.shields.io/badge/stars-✨-yellow)]()

A lightweight, configurable scraper to track and log flight prices across airlines and aggregators. Designed to be easy to run locally, scheduleable for periodic checks, and simple to extend for additional sites.

---

## ✨ Highlights

- Simple configuration-driven scrapes (origin, destination, dates)
- Outputs results to CSV / JSON and optionally to sqlite
- Built with maintainability in mind — modular scrapers per site
- Ready for automation (cron, GitHub Actions, or Docker)

---

## 📦 Features

- Multi-site scraping support
- Rate-limiting and retry logic
- Support for headless browser (optional) or fast HTTP mode
- Export formats: CSV, JSON, SQLite
- Example notebooks / scripts for analysis and visualization

---

## ⚙️ Tech Stack

- Language: Python 3.8+
- Libraries: requests, BeautifulSoup4, (optional) Selenium / Playwright for JS-heavy sites
- Storage: CSV / JSON / SQLite

---

## 🔧 Quick Start

1. Clone the repo
   ```
   git clone https://github.com/AayushBadoni18/Flight-Price-Scraper-.git
   cd Flight-Price-Scraper-
   ```

2. Create and activate a virtual environment (recommended)
   ```
   python -m venv .venv
   source .venv/bin/activate   # macOS / Linux
   .venv\Scripts\activate      # Windows
   ```

3. Install dependencies
   ```
   pip install -r requirements.txt
   ```

4. Copy the example config and edit your search parameters
   ```
   cp config.example.yaml config.yaml
   # Edit config.yaml: set origin, destination, depart_date, return_date, output settings...
   ```

5. Run a single scrape
   ```
   python run_scraper.py --config config.yaml
   ```

6. View results
   - Check `output/` for CSV/JSON files or open the configured SQLite DB.

---

## 🧩 Configuration

The project uses a YAML config (config.yaml). Typical keys:

- origin: IATA code (e.g., "JFK")
- destination: IATA code (e.g., "LHR")
- depart_date: YYYY-MM-DD
- return_date: YYYY-MM-DD (optional)
- sites: list of site scrapers to run
- output:
  - format: csv | json | sqlite
  - path: ./output/results.csv

See `config.example.yaml` for a full sample.

---

## 💡 Example output (CSV)

origin,destination,depart_date,return_date,airline,price,currency,timestamp,source
JFK,LHR,2026-01-10,2026-01-20,British Airways,542,USD,2025-12-19T12:34:56Z,britishairways

---

## 🧪 Tests & Linting

- Run tests:
  ```
  pytest tests/
  ```
- Lint:
  ```
  flake8
  ```

---

## 🐳 Docker (optional)

Build:
```
docker build -t flight-scraper:latest .
```

Run (with bind mount for output and config):
```
docker run --rm -v $(pwd)/output:/app/output -v $(pwd)/config.yaml:/app/config.yaml flight-scraper:latest
```

---

## ⏰ Scheduling

- Cron example (runs daily at 02:00):
  ```
  0 2 * * * cd /path/to/Flight-Price-Scraper- && . .venv/bin/activate && python run_scraper.py --config config.yaml >> /var/log/flight-scraper.log 2>&1
  ```
- Or use GitHub Actions to run on a schedule and push results to a repository or an artifact.

---

## 🙌 Contributing

Contributions welcome! A simple guide:
1. Fork the repo
2. Create a feature branch
3. Add tests for new behavior
4. Open a PR with a clear description and screenshots / sample output if relevant

Please follow the code style in the existing codebase.

---

## 📄 License

MIT — see [LICENSE](./LICENSE) for details.

---

## 📬 Contact

Created by AayushBadoni18 