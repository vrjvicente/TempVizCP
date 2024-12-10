"""This module plots two datas of temperature range.

The dictionaries must include the key-values pairs:
    'name' -- List of names of the station associated with the data.
    'date' -- List of dates asssociated with their temperature range.
    'lows' -- List of the lowest temperatures from their respected dates.
    'highs' -- List of the highest temperatures from their respected dates.
"""
from pathlib import Path

from matplotlib import pyplot as plt

def show_figure(datas):
    """Generates and shows the figure."""
    data1 = datas[0]
    data2 = datas[1]

    data1_name = max(data1['name'])
    data2_name = max(data2['name'])

    fig, ax = plt.subplots(figsize=[11,6], dpi=128)
    ax.plot(data1['dates'], data1['lows'], color='blue', alpha=0.5)
    ax.plot(data1['dates'], data1['highs'], color='red', alpha=0.5)
    ax.plot(data2['dates'], data2['lows'], color='green', alpha=0.5,)
    ax.plot(data2['dates'], data2['highs'], color='#FF7900', alpha=0.5)
    ax.fill_between(data1['dates'], data1['lows'], data1['highs'],
                    facecolor='blue', alpha=0.1, label=data1_name)
    ax.fill_between(data2['dates'], data2['lows'], data2['highs'],
                    facecolor='green', alpha=0.1, label=data2_name)

    ax.set_title("Temperature Data from Two Stations", fontsize=18)
    ax.set_xlabel('Dates', fontsize=14)
    fig.autofmt_xdate()
    ax.set_ylabel("Temperature (\xb0F)", fontsize=14)
    ax.tick_params(labelsize=14)
    ax.set_facecolor('#d9d9d9')
    ax.grid(True, alpha=0.6)
    ax.legend(title='Stations', shadow=True)

    print("\n---------- Generating figure... ----------")
    save_figure()
    print("\n---------- Viewing figure... ----------")
    plt.show()

def save_figure():
    """Asks the user for a name for the file and checks if the file already
    exists in the 'figures' folder.
    """
    print("\nWould you like a copy of the figure? (y/n)")
    action = response()
    while action:
        file_name = input("What do you want to name the saved "
                          "figure as?\n> ")
        path = Path(f'figures/{file_name}.png')
        if path.exists() == True:
            print("That file name already exists. Do you want to "
                  "overwrite it? (y/n)")
            overwrite = response()
        if not overwrite:
            continue

        plt.savefig(f'figures/{file_name}.png', dpi=150)
        print("Figure saved.")
        break

def response():
    """Return a boolean based on the user's response."""
    while True:
        answer = input("> ")
        if answer.lower() == 'y' or answer.lower() == 'yes':
            return True
        elif answer.lower() == 'n' or answer.lower() == 'no':
            return False
        else:
            print("That is an incorrect response. "
                  "Please try again. (y/n)")
