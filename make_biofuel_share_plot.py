import matplotlib.pyplot as plt
import csv
import numpy as np
    
def convert_to_float(string_list):
    """
    Converts a list of strings to a list of floats.
    """
    float_list = []
    for string in string_list:
        try:
            float_value = float(string)
            float_list.append(float_value)
        except ValueError:
            print(f"Unable to convert '{string}' to float.")
    return float_list
            


# Example data
years = range(2002, 2022)
#values =

with open('/Users/danikamacdonell/Downloads/global-final-energy-demand-for-trucks-and-buses-by-fuel-2000-2021-and-2030-in-the-net-zero-scenario.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        data = row
        numeric_data = convert_to_float(data[19:139])
        print(numeric_data)
        diesel_data = np.asarray(numeric_data[0::6])
        gasoline_data = np.asarray(numeric_data[1::6])
        ngas_data = np.asarray(numeric_data[2::6])
        biofuel_data = np.asarray(numeric_data[3::6])
        elec_data = np.asarray(numeric_data[4::6])
        hy_data = np.asarray(numeric_data[5::6])
        all_data = diesel_data + gasoline_data + ngas_data + biofuel_data + elec_data + hy_data
        biofuel_fraction = np.asarray(biofuel_data) / np.asarray(all_data)
        
        print(biofuel_fraction)

print()

# Create the bar chart
fig = plt.figure(figsize = (14, 7))
plt.plot(years, biofuel_fraction, 'o-', color='green', linewidth=3)
plt.xticks(years[::3], fontsize=28)
plt.yticks(fontsize=28)
plt.grid(axis='y')
plt.ylim(0, 0.04)
#plt.xlabel('Categories')
plt.ylabel('Fuel market share (%)\n', fontsize=34)
plt.title('Fuel market share of biofuels for trucks and buses\n', fontsize=33)
plt.tight_layout()
plt.savefig('biofuels_share.png')
