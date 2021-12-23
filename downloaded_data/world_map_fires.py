import csv
from datetime import datetime

from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

# Explore the structure of the data.
filename = 'data/world_fires_7_day.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    index_num = 0
    
    for item in header_row:
        if item == 'latitude':
            lat_index = index_num
        elif item == 'longitude':
            lon_index = index_num
        elif item == 'bright_ti4':
            bright_index = index_num
        
        index_num += 1

    # Get location and brightness from this file.
    lats, lons, brights = [], [], []
    for row in reader:
        lat = float(row[lat_index])
        lon = float(row[lon_index])
        bright = float(row[bright_index])
        lats.append(lat)
        lons.append(lon)
        brights.append(bright)

# Map the fires.
data = [{
    'type': 'scattergeo',
    'lon': lons,
    'lat': lats,
    'marker': {
        'size': [0.02*bright for bright in brights],
        'color': brights,
        'colorscale': 'Reds',
        'reversescale': True,
        'colorbar': {'title': 'Brightness (K)'},
    },
}]

my_layout = Layout(title='World fires and their brightness over a 7-day period')

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='global_fires.html')