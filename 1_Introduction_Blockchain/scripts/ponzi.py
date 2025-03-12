from functools import reduce

def best_profit(history):
    # Using reduce and filter to calculate the best possible profit
    profit_factors = map(lambda x: x[1] / x[0], zip(history[:-1], history[1:]))
    profitable_trades = filter(lambda x: x > 1, profit_factors)
    total_profit = reduce(lambda x, y: x * y, profitable_trades, 1)
    return total_profit

    # Traditional approach to calculate the best possible profit
    total_profit = 1
    for i in range(len(history) - 1):
        current_price = history[i]
        next_price = history[i + 1]
        if next_price > current_price:
            total_profit *= next_price / current_price
    return total_profit
