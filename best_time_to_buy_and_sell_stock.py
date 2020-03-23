prices = [7, 1, 5, 3, 6, 4]


def maxProfit(prices):
    my_map = {}
    for i, v in enumerate(prices):
        my_map[i] = v

    print(my_map)


print(maxProfit(prices))
