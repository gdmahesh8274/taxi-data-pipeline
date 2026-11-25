from pathlib import Path
import duckdb


file_path = (
    Path(__file__).resolve().parent
    / "data"
    / "green_tripdata_2024-01_flagged.parquet"
)

trips = duckdb.read_parquet(str(file_path))

result = trips.query(
    "trips",
    """
    SELECT
        PULocationID AS pickup_zone_id,
        COUNT(*) AS trip_count
    FROM trips
    GROUP BY PULocationID
    ORDER BY trip_count DESC
    LIMIT 5
    """
)
zone_path = file_path.parent / "taxi_zone_lookup.csv"
zones = duckdb.read_csv(str(zone_path))

zones.limit(5).show()

result.show()

zones.create_view("zones")

report = trips.query(
    "trips",
    """
    SELECT
        t.PULocationID AS pickup_zone_id,
        z.Zone AS pickup_area,
        COUNT(*) AS trip_count
    FROM trips AS t
    LEFT JOIN zones AS z
        ON t.PULocationID = z.LocationID
    GROUP BY t.PULocationID, z.Zone
    ORDER BY trip_count DESC
    LIMIT 5
    """
)

report.show()

report_path = file_path.parent / "top_pickup_zones.csv"
report.write_csv(str(report_path), header=True)

print("Report saved:", report_path.name)

import os
from uuid import uuid4

reports_bucket = os.getenv("REPORTS_BUCKET")

if reports_bucket:
    from google.cloud import storage

    object_name = f"top_pickup_zones_{uuid4().hex}.csv"
    blob = storage.Client().bucket(reports_bucket).blob(object_name)
    blob.upload_from_filename(str(report_path), content_type="text/csv")
    print(f"Report uploaded: gs://{reports_bucket}/{object_name}") 