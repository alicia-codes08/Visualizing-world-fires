import csv 
from pathlib import Path
from collections import Counter

path = Path("fire_data/world_fires.csv")
lines = path.read_text(encoding="utf-8").splitlines()
reader = csv.reader(lines, delimiter=";")
header_row = next(reader)

# getting index of the elements
for index, element in enumerate(header_row):
    print(index, element) 

# extract data
countries_full = []
for row in reader:
    country = row[3]
    countries_full.append(country)

counts = Counter(countries_full)
countries = []
numbers = []
for country, number in counts.items():
    countries.append(country)
    numbers.append(number)

print(countries)
print(numbers)