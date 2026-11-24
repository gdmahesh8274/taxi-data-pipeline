CREATE OR REPLACE VIEW `project-72171eeb-108d-4e3b-a4d.taxi_reporting.top_pickup_zones` AS
SELECT
  t.PULocationID AS pickup_zone_id,
  z.Zone AS pickup_area,
  COUNT(*) AS trip_count
FROM `project-72171eeb-108d-4e3b-a4d.taxi_raw.green_trips_2024_01` AS t
LEFT JOIN `project-72171eeb-108d-4e3b-a4d.taxi_raw.taxi_zones` AS z
  ON t.PULocationID = z.LocationID
GROUP BY t.PULocationID, z.Zone
ORDER BY trip_count DESC, pickup_zone_id
LIMIT 5;