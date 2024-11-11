import csv
from datetime import datetime
import sys
from matplotlib import pyplot as plt

print("Welcome to the Sitka Weather Data Viewer!")
print("Please select an option from the menu below:")
print("1. High Temperatures")
print("2. Low Temperatures")
print("3. Exit")

filename = 'sitka_weather_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # Get dates and high temperatures from this file.
    dates, highs, lows = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        dates.append(current_date)
        high = int(row[5])
        low = int(row[6])
        highs.append(high)
        lows.append(low)

while True:
    
        choice = input("\nEnter selection: ")

        # Plot the high temps.
        if choice == '1':
            print("Displaying high temperatures!")
            # Plot the high temperatures.
            #plt.style.use('seaborn')
            fig, ax = plt.subplots()
            ax.plot(dates, highs, c='red')

            # Format plot.
            plt.title("Daily high temperatures - 2018", fontsize=24)
            plt.xlabel('', fontsize=16)
            fig.autofmt_xdate()
            plt.ylabel("Temperature (F)", fontsize=16)
            plt.tick_params(axis='both', which='major', labelsize=16)

            plt.show()

        # Plot the low temps.
        elif choice == '2':
            print("Displaying low temperatures!")
            # Plot the low temperatures>
            fig, ax = plt.subplots()
            ax.plot(dates, lows, c='blue')

            # Formate plot.
            plt.title("Daily Low Temperatures - 2018", fontsize=24)
            plt.xlabel('', fontsize=16)
            fig.autofmt_xdate()
            plt.ylabel("Temperature (F)", fontsize=16)
            plt.tick_params(axis='both', which='major', labelsize=16)
            plt.show()
        
        # Exit program
        elif choice == '3':
            print("Exiting program..\n")
            sys.exit()

        else:
            print("Invalid selection. Please select either 1, 2, or 3.")
