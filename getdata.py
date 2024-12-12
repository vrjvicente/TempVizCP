"""Extract temperature data from a CSV file.

When importing, it is recommended to import collect_data, however,
gather_temperatures can also be used if the correct arguments are given.

Note that this module takes the CSV file that is taken from the
NOAA Climate Data Online site. Because of this, index_lookup scans for the
certain header titles to properly locate and retrieve the file's temperature
information. Thus, the header of the file must include 'NAME', 'DATE', 'TMIN',
and 'TMAX'.
"""
import csv
import time
from pathlib import Path
from datetime import datetime

def collect_data(path_name: str) -> dict[str, list] | dict:
    """Return a file's temperature data.
    
    The file is pointed within the datas directory. Before calling the
    function, make sure that the CSV file is located inside the folder.
    """
    path = Path(f'datas/{path_name}.csv')
    if not path_exists(path):
        print(f"\nThe file {path_name}.csv does not exist. \n"
              "Please make sure that the file name is spelled correctly and "
              "is located inside \nthe 'datas' directory.")
        return {}
    
    lines = path.read_text(encoding='utf-8').splitlines()

    reader = csv.reader(lines)
    header_row = next(reader)

    indicies = index_lookup(header_row)
    if not indicies_correct(indicies):
        print(f"There is an issue with the header on {path_name}.\n"
              "Please check the file and its headers.")
        return {}
    
    data = gather_temperatures(reader, indicies)
    return data

def gather_temperatures(
        reader: object, indicies: list[int]) -> dict[str, list]:
    """Return a dictionary of temperature data."""
    print("\nExtracting data...")
    time.sleep(0.5)  # Creates a natural loading time.
    data = {
        'name': [],
        'dates': [],
        'lows': [],
        'highs': [],
        }
    for row in reader:
        name = row[indicies[0]]
        date = datetime.strptime(row[indicies[1]], '%Y-%m-%d')
        try:
            low_temperature = int(row[indicies[2]])
            high_temperature = int(row[indicies[3]])
        except ValueError:
            print(f"Missing data for {date.date()} from {name}.")
        else:
            data['name'].append(name)
            data['dates'].append(date)
            data['lows'].append(low_temperature)
            data['highs'].append(high_temperature)
    print("Data extracted.")
    return data

def index_lookup(header_row: list[str]) -> list[int]:
    """Scan the header for keywords and return their indicies."""
    keywords = ['NAME', 'DATE', 'TMIN', 'TMAX']
    indicies = []
    indicies = [int(i) for key in keywords
                for i, column_header in enumerate(header_row)
                if column_header == key]
    return indicies

def indicies_correct(indicies: list[int]) -> bool:
    """Check if the list has four elements."""
    if len(indicies) != 4:
        return False
    return True

def path_exists(path: Path) -> bool:
    """Check path existence."""
    if path.exists():
        return True
    else:
        return False
