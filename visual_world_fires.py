from pathlib import Path 
import csv 
import plotly.express as px

path = Path("fire_data/world_fires_day.csv")
lines = path.read_text(encoding="utf-8").splitlines()
reader = csv.reader(lines)
header_row = next(reader)

# get index of the information
for index, element in enumerate(header_row):
    print(index, element) 

# extract data 
lons, lats, brightness = [], [], []
for row in reader:
    lons.append(float(row[1]))
    lats.append(float(row[0]))
    brightness.append(float(row[2]))

# visualize data
title = "World fires 2022-04-03" 
fig = px.scatter_geo(lon=lons, lat=lats, size=brightness, color=brightness,
                    color_continuous_scale='sunset', projection="natural earth",
                    labels={"color":"brightness"}, title=title)
fig.show() 