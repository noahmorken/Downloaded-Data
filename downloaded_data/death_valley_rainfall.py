import csv
from datetime import datetime

import matplotlib.pyplot as plt

filename = 'data/death_valley_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    
    # Get dates and precipitation from this file.
    dates, rain = [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        rainfall = float(row[3])
        dates.append(current_date)
        rain.append(rainfall)

    # Plot the rainfall amounts.
    plt.style.use('seaborn')
    fig, ax = plt.subplots()
    ax.plot(dates, rain, c='blue')

    # Format plot.
    ax.set_title("Daily rainfall in Death Valley, 2018", fontsize=24)
    ax.set_xlabel('', fontsize=16)
    fig.autofmt_xdate()
    ax.set_ylabel("Precipitation (in)", fontsize=16)
    ax.tick_params(axis='both', which='major', labelsize=16)

    plt.show()