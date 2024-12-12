from getdata import collect_data
from showfig import show_figure

print("---------")
print("TempVizCP")
print("---------")

intro = ("This program takes the temperature range of two data sets and plots "
         "them into a figure.")
instruction = ("\nDatas are extracted from a CSV file. Make sure that both "
               "files are included in the datas directory\nbefore "
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
    print("\nProgram ended.")
