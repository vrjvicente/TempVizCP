from pathlib import Path
import csv

from fun_stuff import *

path1 = Path('datas/death_valley_2021_full.csv')
lines1 = path1.read_text(encoding='utf-8').splitlines()

reader1 = csv.reader(lines1)
header_row1 = next(reader1)

indicies1 = index_lookup(header_row1)

data1 = gather_temperatures(reader1, indicies1)

path2 = Path('datas/sitka_weather_2021_full.csv')
lines2 = path2.read_text(encoding='utf-8').splitlines()

reader2 = csv.reader(lines2)
header_row2 = next(reader2)

indicies2 = index_lookup(header_row2)

data2 = gather_temperatures(reader2, indicies2)

show_figure(data1, data2)