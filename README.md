# NYC Taxi Data Pipeline

## Purpose
Analyze January 2024 green taxi trips to find busy pickup areas.

## Tools
Python, PyArrow, DuckDB, SQL, and Git.

## Workflow
1. Download trip data and taxi zone names.
2. Inspect data and flag unusual distances.
3. Join trips with zone names using SQL.
4. Export the top five pickup zones to CSV.

## Data quality
Flag trips with zero distance or distance above 100 miles.
These are review flags, not confirmed errors.
Original data is preserved.

## Run locally

Install dependencies:
```powershell
python -m pip install -r requirements.txt
```

Run these scripts in order:
```powershell
python main.py
python inspect_data.py
python query_data.py
```

Output: `data/top_pickup_zones.csv`