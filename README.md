# European Unemployment Analysis (2025–2026)

## Project Description
This project analyzes unemployment data across European countries using Eurostat data.

## ETL Process

### Extract
Data is extracted from the Eurostat Statistics API.

### Transform
JSON data is transformed into structured datasets and CSV files.

### Load
The transformed data is loaded into CSV files for analysis in Power BI.

## Files

- extract.py
- transform.py
- load.py
- fact_table.py
- countries_dimension.csv
- time_dimension.csv

## Data Source

Eurostat Statistics API

https://ec.europa.eu/eurostat/

## Tools Used

- Python
- Pandas
- Requests
- Power BI