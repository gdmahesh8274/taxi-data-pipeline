{{ config(materialized='view') }}

SELECT
    t.PULocationID AS pickup_zone_id,
    z.Zone AS pickup_area,
    COUNT(*) AS trip_count
FROM {{ source('taxi_raw', 'green_trips_2024_01') }} AS t
LEFT JOIN {{ source('taxi_raw', 'taxi_zones') }} AS z
    ON t.PULocationID = z.LocationID
GROUP BY t.PULocationID, z.Zone
ORDER BY trip_count DESC, pickup_zone_id
LIMIT 5