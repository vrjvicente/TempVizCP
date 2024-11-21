from pathlib import Path
import csv

from fun_stuff import *

path1 = Path('datas/death_valley_2021_full.csv')
lines1 = path1.read_text(encoding='utf-8').splitlines()

reader1 = csv.reader(lines1)
header_row1 = next(reader1)

i_date1 = index_lookup(header_row1, 'DATE')
i_low1 = index_lookup(header_row1, 'TMIN')
i_high1 = index_lookup(header_row1, 'TMAX')

data1 = gather_temperatures(reader1, i_date1, i_low1, i_high1)

path2 = Path('datas/sitka_weather_2021_full.csv')
lines2 = path2.read_text(encoding='utf-8').splitlines()

reader2 = csv.reader(lines2)
header_row2 = next(reader2)

i_date2 = index_lookup(header_row2, 'DATE')
i_low2 = index_lookup(header_row2, 'TMIN')
i_high2 = index_lookup(header_row2, 'TMAX')

data2 = gather_temperatures(reader2, i_date2, i_low2, i_high2)

show_figure(data1, data2)