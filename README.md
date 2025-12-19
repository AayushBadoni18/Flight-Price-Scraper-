✈️ Flight Prices Scraper (MakeMyTrip – Legacy API)

A Python-based flight price data scraper designed to collect, parse, and export airline fare information over a configurable date range.
This project demonstrates web scraping architecture, data parsing, automation, and CSV-based data pipelines, built around MakeMyTrip’s legacy public endpoints.

⚠️ Note: The original data source has since been secured behind CDN-level bot protection. This repository is preserved for educational and architectural demonstration purposes.

📌 Project Overview

This project was originally built to:

Fetch one-way and round-trip flight pricing data

Parse deeply nested flight JSON structures

Extract fare, duration, airline, and availability details

Store normalized flight data in CSV format

Automate data collection across a date range

It showcases real-world scraping challenges, including:

HTML + JavaScript data extraction

API structure dependency

Handling API deprecations and access restrictions

🧱 Architecture Overview
Flight Scraper
│
├── HTTP Fetch Layer
│   └── URL construction + response handling
│
├── Parsing Layer
│   └── Extracts `flightsData` JSON
│
├── Transformation Layer
│   └── Normalizes nested flight objects
│
├── Storage Layer
│   └── CSV export with schema
│
└── Automation Layer
    └── Date range iteration

🚀 Features

One-way flight price scraping

Round-trip API support (structure included)

Automatic date-range iteration

CSV export for downstream analysis

Clean object-oriented design

Python 3 compatible

🛠️ Tech Stack

Language: Python 3

Libraries:

urllib.request – HTTP requests

json – Parsing nested API responses

python-dateutil – Date range automation

Output Format: CSV

📂 Project Structure
Flight-Prices-Scraper/
│
├── scraper.py        # Main scraper logic
├── buff.csv          # Generated output file
├── README.md         # Project documentation

▶️ How It Works

Constructs MakeMyTrip flight search URLs dynamically

Sends HTTP requests to legacy endpoints

Extracts embedded JavaScript flight data

Parses nested JSON objects

Writes normalized flight details into CSV

📄 CSV Output Schema
Column	Description
Origin	Source airport code
Destination	Destination airport code
Dept_Date	Departure date
Dept_Time	Departure time
Arr_Time	Arrival time
Total_Fare	Total ticket price
Base_Fare	Base fare
Fuel_Fare	Fuel surcharge
Airways	Airline name
Available	Seat availability
Duration	Total flight duration
Class_Type	Travel class
Flight_Number	Flight number
Flight_Code	Airline code
FlightID	Internal flight ID
Hopping	Layover indicator
Taken	Data capture date
⚠️ Current Limitation (Important)

MakeMyTrip has disabled unauthenticated access to its flight search endpoints using CDN-level protections (Akamai).
As a result:

Live scraping no longer works

Requests without browser context are blocked

This behavior is expected and intentional

This repository is therefore best used for:

Learning scraping architecture

Parsing complex JSON responses

Data engineering practice

Academic and resume demonstration

🧠 Key Learnings

Scraping is fragile and source-dependent

APIs evolve and get locked down

Separation of concerns improves maintainability

Data pipelines matter more than raw scraping

Defensive coding is essential for external dependencies

🔮 Possible Extensions

Replace live calls with mocked JSON responses

Integrate public aviation APIs (Amadeus, AviationStack)

Add retry, timeout, and logging layers

Convert into async scraper

Add unit tests for parsers

Visualize price trends using Pandas/Matplotlib

📜 Disclaimer

This project is intended strictly for educational purposes.
No commercial use or live scraping of MakeMyTrip is encouraged or supported.

👤 Author

Aayush Badoni
Computer Science & Engineering Undergraduate
Interests: Data Structures, Python, Web Systems, Data Engineering