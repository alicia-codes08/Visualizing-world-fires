import csv 
from pathlib import Path

path = Path("fire_data/world_fires.csv")
lines = path.read_text(encoding="utf-8").splitlines()
reader = csv.reader(lines, delimiter=";")
header_row = next(reader)

for index, element in enumerate(header_row):
    print(index, element) 