from datetime import datetime
from matplotlib import pyplot as plt

def index_lookup(header_row):
    """Finds the indicies containing the given keywords and return them as
    a list.
    """
    keywords = ['NAME', 'DATE', 'TMIN', 'TMAX']
    indicies = []
    indicies = [i for key in keywords
                for i, column_header in enumerate(header_row)
                if column_header == key]
    return indicies

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
            print(f"Missing value from {date}.")
        else:
            data['name'].append(name)
            data['dates'].append(date)
            data['lows'].append(low_temperature)
            data['highs'].append(high_temperature)
    return data

def show_figure(data1, data2):
    """Generates the figure."""

    data1_name = set(data1['name']).pop()
    data2_name = set(data2['name']).pop()

    plt.style.use('seaborn-v0_8')
    fig, ax = plt.subplots(figsize=[10,6], dpi=128)
    ax.plot(data1['dates'], data1['lows'], color='red', alpha=0.5)
    ax.plot(data1['dates'], data1['highs'], color='blue', alpha=0.5)
    ax.plot(data2['dates'], data2['lows'], color='fuchsia', alpha=0.5)
    ax.plot(data2['dates'], data2['highs'], color='purple', alpha=0.5)
    ax.fill_between(data1['dates'], data1['lows'], data1['highs'],
                    facecolor='blue', alpha=0.1, label=data1_name)
    ax.fill_between(data2['dates'], data2['lows'], data2['highs'],
                    facecolor='purple', alpha=0.1, label=data2_name)

    ax.set_title("Temperatures", fontsize=24)
    ax.set_xlabel('Dates', fontsize=16)
    fig.autofmt_xdate()
    ax.set_ylabel("Temperature (F)", fontsize=16)
    ax.tick_params(labelsize=16)
    ax.legend()

    save_figure()
    plt.show()

def save_figure():
    """Asks the user if they would like to save the figure, then saves
    the file into the 'figures' directory if so.
    """
    while True:
        print("Would you like a copy of the figure? (y/n)")
        answer = input("> ")
        if answer.lower() == 'y' or answer.lower() == 'yes':
            file_name = input("What do you want to name the saved "
                              "figure as?\n> ")
            plt.savefig(f'figures/{file_name}.png')
            break
        elif answer.lower() == 'n' or answer.lower() == 'no':
            break
        else:
            print("That is an incorrect response.")
