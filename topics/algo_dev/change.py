def make_change(cents):
    # coins available: 200, 100,
    coins = (200, 100, 50, 20, 10, 5, 2, 1)
    coins_used = []
    coin_counts = 0
    for coin in coins:
        while cents >= coin:
            coins_used.append(coin)
            cents -= coin
            coin_counts += 1
    return coin_counts, coins_used


print(make_change(24))
print(make_change(163))
