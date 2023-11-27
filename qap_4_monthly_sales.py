# This is a program to enter and plot monthly sales.
# Program Author: Steve Sharpe
# Program Date: November 22, 2023

# Import required libraries.

import matplotlib.pyplot as plt
import math
import runpy

# Set up program constants.

# Set up program functions.

# Start the main program.

# writing  a program to enter and plot monthly sales.

# Create a list for x and y axis values, and use a loop to generate the values.

xaxis = [
    "JAN",
    "FEB",
    "MAR",
    "APR",
    "MAY",
    "JUN",
    "JUL",
    "AUG",
    "SEP",
    "OCT",
    "NOV",
    "DEC",
]

yaxis = []

for x in range(0, 12):
    y = input(
        f"Enter the sales in dollars only for {xaxis[x]} (press enter if month has not ended yet): "
    )
    y = int(y) if y else 0
    yaxis.append(y)

# Plot the data.

plt.plot(xaxis, yaxis)

plt.title("Monthly Sales")
plt.scatter(xaxis, yaxis, color="darkblue", marker="x", label="item 1")

plt.xlabel("Month")
plt.ylabel("Sales (dollars)")

plt.grid(True)
plt.legend()

plt.show()

runpy.run_path("qap_4_main_menu.py")
