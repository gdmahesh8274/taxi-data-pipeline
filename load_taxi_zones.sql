LOAD DATA OVERWRITE
  `project-72171eeb-108d-4e3b-a4d.taxi_raw.taxi_zones`
(
  LocationID INT64,
  Borough STRING,
  Zone STRING,
  service_zone STRING
)
FROM FILES (
  format = 'CSV',
  uris = ['gs://taxi-raw-72171eeb-108d/taxi_zone_lookup.csv'],
  skip_leading_rows = 1
);