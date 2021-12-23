import csv
from datetime import datetime

import matplotlib.pyplot as plt

filename = 'data/san_francisco_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # Get dates and snowfall from this file.
    dates, snowfall = [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        try:
            snow = float(row[3])
        except ValueError:
            print(f"Missing data for {current_date}")
        else:
            dates.append(current_date)
            snowfall.append(snow)

    # Plot the snowfall.
    plt.style.use('seaborn')
    fig, ax = plt.subplots()
    ax.plot(dates, snowfall, c='blue', alpha=0.5)

    # Format plot.
    ax.set_title("Daily snowfall in San Franscisco, 2018", fontsize=24)
    ax.set_xlabel('', fontsize=16)
    fig.autofmt_xdate()
    ax.set_ylabel("Snowfall (in)", fontsize=16)
    ax.tick_params(axis='both', which='major', labelsize=16)

    plt.show()