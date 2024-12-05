from pathlib import Path
from datetime import datetime
import csv

def collect_data(path_name):
    """Points to the given path and collects the required information
    to return a dictionary.
    """
    path = Path(f'datas/{path_name}.csv')
    # Returns an empty dictionary if the path does not exist in the 'datas'
    # directory.
    if not path_exists(path):
        print(f"\nThe file {path_name}.csv does not exist. \n"
              "Please make sure that the file name is spelled correctly and "
              "is located inside \nthe 'datas' directory.")
        return {}
    
    lines = path.read_text(encoding='utf-8').splitlines()

    reader = csv.reader(lines)
    header_row = next(reader)

    indicies = index_lookup(header_row)
    # Returns an empty dictionary if there's a problem with headers.
    if not indicies_correct(indicies):
        print(f"There is an issue with the header on {path_name}.\n"
              "Please check the file and its headers.")
        return {}
    
    print("\nExtracting data...")
    data = gather_temperatures(reader, indicies)
    return data

def path_exists(path):
    """Returns a boolean whether the given path exists or not."""
    if path.exists():
        return True
    else:
        return False

def index_lookup(header_row):
    """Finds the indicies containing the given keywords and returns them as
    a list.
    """
    keywords = ['NAME', 'DATE', 'TMIN', 'TMAX']
    indicies = []
    indicies = [int(i) for key in keywords
                for i, column_header in enumerate(header_row)
                if column_header == key]
    return indicies

def indicies_correct(indicies):
    """Returns a boolean whether the given indicies list have
    the required four values.
    """
    if len(indicies) != 4:
        return False
    return True

def gather_temperatures(reader, indicies):
    """Collects the names, dates, and temperatures in the reader from
    the given indicies and stores them into a dictionary to return.
    """
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
            print(f"Data is missing for {date.date()} from {name}.")
        else:
            data['name'].append(name)
            data['dates'].append(date)
            data['lows'].append(low_temperature)
            data['highs'].append(high_temperature)
    return data
