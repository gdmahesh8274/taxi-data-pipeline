from pathlib import Path
from urllib.request import urlretrieve

data_folder = Path(__file__).resolve().parent / "data"
data_folder.mkdir(exist_ok=True)

url = "https://d37ci6vzurychx.cloudfront.net/trip-data/green_tripdata_2024-01.parquet"
file_path = data_folder / "green_tripdata_2024-01.parquet"

print("Downloading...")
urlretrieve(url, file_path)
print("Download complete!")

zone_url = "https://d37ci6vzurychx.cloudfront.net/misc/taxi_zone_lookup.csv"
zone_path = data_folder / "taxi_zone_lookup.csv"

urlretrieve(zone_url, zone_path)
print("Zone lookup downloaded!")