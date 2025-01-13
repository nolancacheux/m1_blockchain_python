# Using Monte-Carlo to calculate PI.

from random import random                                # We need the random package

# Function that returns a random 2D point on the unit square
def rain_drop():
    return random(), random()                            # x = random(), y = random() : we return both

# Function that tests if a 2D point is inside the unit circle
def drop_is_on_disk(rainDrop):
    x, y = rainDrop                                      # We unpack rainDrop to get x and y
    return (x - 0.5) ** 2 + (y - 0.5) ** 2 <= 0.5 ** 2   # Equation of a disk with radius 0.5 centered at (0.5; 0.5)

# Function that calculates PI by simulating N rain drops
def calculate_pi(rainDropCount):
    landedOnDisk = 0                                     # At start, no drop on the unit disk
    for _ in range(rainDropCount):                       # We simulate 'rainDropCount' drops
        rainDrop = rain_drop()                           # Generating a rain drop
        if drop_is_on_disk(rainDrop):                    # We check if the drop lands on the unit disk
            landedOnDisk += 1                            # If yes, increment landedOnDisk
    P = landedOnDisk / rainDropCount                     # We use our results to calculate the probability for a drop to land on the disk
    return 4 * P                                         # We calculate PI with the formula P = 4 * PI