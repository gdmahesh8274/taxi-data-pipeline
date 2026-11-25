LOAD DATA OVERWRITE
  `project-72171eeb-108d-4e3b-a4d.taxi_raw.green_trips_2024_01`
FROM FILES (
  format = 'PARQUET',
  uris = ['gs://taxi-raw-72171eeb-108d/green_tripdata_2024-01.parquet']
);