from pathlib import Path
import csv

import fun_stuff

path1 = Path('datas/death_valley_2021_full.csv')
lines1 = path1.read_text(encoding='utf-8').splitlines()

reader1 = csv.reader(lines1)
header_row1 = next(reader1)

path2 = Path('datas/sitka_weather_2021_full.csv')
lines2 = path2.read_text(encoding='utf-8').splitlines()

reader2 = csv.reader(lines2)
header_row2 = next(reader2)