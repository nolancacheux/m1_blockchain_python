# Using Monte-Carlo to estimate the value of PI.

import random  # Importing the random module

# Function to generate a random point within the unit square
def rain_drop():
    return (random.random(), random.random())  # Return a tuple (x, y)

# Function to check if a point lies inside the unit circle
def drop_disk(rainDrop):
    x, y = rainDrop  # Unpack the tuple
    return (x - 0.5) ** 2 + (y - 0.5) ** 2 <= 0.25  # Check if the point is within the circle of radius 0.5 centered at (0.5, 0.5)

# Function to compute PI using Monte-Carlo simulation with N drops
def calculate_pi(rainDropCount):
    hits = 0  # Initialize the count of drops that land on the disk
    for _ in range(rainDropCount):  # Loop over the number of drops
        if drop_disk(rain_drop()):  # Check if the drop is on the disk
            hits += 1  # Increment the count if it is
    return 4 * (hits / rainDropCount)  # Estimate PI using the ratio of hits to total drops
