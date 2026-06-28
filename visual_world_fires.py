import csv 
from pathlib import Path
from collections import Counter
import plotly.express as px

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

# visualize data 
title = "World fires 2002-2024"
fig = px.choropleth(locations=countries,
                    locationmode="country names",
                    color=numbers, projection="natural earth",
                    labels={"color":"number of fires"}) 

fig.show() 