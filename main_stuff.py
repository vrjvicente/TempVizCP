from pathlib import Path
import csv

import data
import figure

print("---------")
print("TempVizCP")
print("---------")

#path_name = input("Path Name:\n>").removesuffix('.csv')
data1 = data.collect_data('death_valley_2021_full')

data2 = data.collect_data('sitka_weather_2021_full')

if not data1 or not data2:
    print("Error")
else:
    figure.show_figure(data1, data2)