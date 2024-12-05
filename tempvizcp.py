from data import collect_data
from figure import show_figure

print("---------")
print("TempVizCP")
print("---------")

intro = ("This program plots the temperature range of two weather stations at "
         "a certain \nperiod of time.")
instruction = ("\nWeather datas are extracted from a .csv file. Make sure that "
               "both files are \nincluded in the 'datas' directory before "
               "continuing.")
print(intro, instruction)

datas = []

ordinal_num = 'first'
while len(datas) != 2:
    file_name = input(f"\nPlease enter the {ordinal_num} "
                      "file name:\n> ").removesuffix('.csv')
    data = collect_data(file_name)
    if not data:
        break
    datas.append(data)
    ordinal_num = 'second'

if len(datas) == 2:
    show_figure(datas)
