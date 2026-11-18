from pathlib import Path
import pyarrow.parquet as pq

file_path = (
    Path(__file__).resolve().parent
    / "data"
    / "green_tripdata_2024-01.parquet"
)

table = pq.read_table(file_path)

print("Rows:", table.num_rows)
print("Columns:", table.num_columns)

print(table.column_names)


sample = table.select(["trip_distance", "fare_amount", "total_amount"])
print(sample.slice(0, 5).to_pydict())

for column in ["trip_distance", "fare_amount", "total_amount"]:
    print(column, "missing values:", table[column].null_count)

import pyarrow.compute as pc

print("Distance range:", pc.min_max(table["trip_distance"]).as_py())

long_trips = pc.greater(table["trip_distance"], 100)
print("Trips over 100 miles:", pc.sum(long_trips).as_py())

unusual_trips = table.filter(long_trips)
print(
    unusual_trips
    .select(["trip_distance", "fare_amount", "total_amount"])
    .slice(0, 5)
    .to_pydict()
)
zero_distance = pc.equal(table["trip_distance"], 0)
print("Trips with zero distance:", pc.sum(zero_distance).as_py())

needs_review = pc.or_(zero_distance, long_trips)
table = table.append_column("distance_needs_review", needs_review)

print("Trips needing review:", pc.sum(needs_review).as_py())

output_path = file_path.parent / "green_tripdata_2024-01_flagged.parquet"
pq.write_table(table, output_path)

print("Saved:", output_path.name)
