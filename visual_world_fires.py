from pathlib import Path 
import csv 

path = Path("fire_data/world_fires_day.csv")
lines = path.read_text(encoding="utf-8").splitlines()
reader = csv.reader(lines)
header_row = next(reader)

# get index of the information
for index, element in enumerate(header_row):
    print(index, element) 

# extract data 
lons = [lon[1] for lon in reader]
lats = [lat[0] for lat in reader]
brightness = [bright[2] for bright in reader]

# visualize data