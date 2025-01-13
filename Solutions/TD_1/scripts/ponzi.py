# Calculating the best possible profit on a time frame
from functools import reduce

# The process is simple :
# - For each price variation (from a day to the next)
#   · If the price goes down, we don't buy, so continue to next day
#   · If the price goes up, we buy at start of the day, and sell at the end of the day, so we calculate by how much this trade multiplied our investment
# - We multiply all trade gains to obtain the total investment multiplier

def best_profit(history):

    # One line solution
    return reduce(lambda x, y: x * y, filter(lambda x: x > 1, map(lambda x: x[1] / x[0], zip(history[:-1], history[1:]))))

    # Traditional solution
    totalProfit = 1
    for i in range(len(history)-1):
        todaysPrice = history[i]
        tomorrowsPrice = history[i+1]
    #for todaysPrice, tomorrowsPrice in zip(history[:-1], history[1:]):
        if tomorrowsPrice > todaysPrice:
            totalProfit *= tomorrowsPrice / todaysPrice
    return totalProfit