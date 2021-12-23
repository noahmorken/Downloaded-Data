import csv
from datetime import datetime

import matplotlib.pyplot as plt

s_filename = 'data/sitka_weather_2018_simple.csv'
d_filename = 'data/death_valley_2018_simple.csv'
with open(s_filename) as f, open(d_filename) as d:
    s_reader = csv.reader(f)
    s_header_row = next(s_reader)
    d_reader = csv.reader(d)
    d_header_row = next(d_reader)
    
    # Get dates, and high and low temperatures from these files.
    dates, s_highs, s_lows, d_highs, d_lows = [], [], [], [], []
    for row in s_reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        s_high = int(row[5])
        s_low = int(row[6])
        dates.append(current_date)
        s_highs.append(s_high)
        s_lows.append(s_low)

    for row in d_reader:
        try:
            d_high = int(row[4])
            d_low = int(row[5])
        except ValueError:
            print(f"Missing data for {current_date}")
        else:
            d_highs.append(d_high)
            d_lows.append(d_low)

    # Plot the high and low temperatures.
    plt.style.use('seaborn')
    fig, ax = plt.subplots()
    ax.plot(dates, s_highs, c='green', alpha=0.5)
    ax.plot(dates, s_lows, c='purple', alpha=0.5)
    ax.plot(dates, d_highs, c='red', alpha=0.5)
    ax.plot(dates, d_lows, c='yellow', alpha=0.5)
    ax.fill_between(dates, s_highs, s_lows, facecolor='blue', alpha=0.1)
    ax.fill_between(dates, d_highs, d_lows, facecolor='orange', alpha=0.1)

    # Format plot.
    ax.set_title("Daily high and low temperatures, 2018", fontsize=24)
    ax.set_xlabel('', fontsize=16)
    fig.autofmt_xdate()
    ax.set_ylabel("Temperature (F)", fontsize=16)
    ax.tick_params(axis='both', which='major', labelsize=16)

    plt.show()