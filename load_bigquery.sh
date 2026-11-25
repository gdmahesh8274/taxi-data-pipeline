#!/usr/bin/env bash
set -e

cd "$(dirname "$0")"

bq --location=us-central1 query --use_legacy_sql=false < load_green_trips.sql
bq --location=us-central1 query --use_legacy_sql=false < load_taxi_zones.sql