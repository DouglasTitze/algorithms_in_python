def calc_min_coins(num):
    coins = [100, 50, 25, 10, 5, 1]
    coins_used = []

    num *= 100

    for coin in coins:

        # If the current coin is larger than the number then exit and iterate to the next coin
        while coin < num:
            num -= coin
            coins_used.append(f"{coin/100:.02}")

    return f"Number of coins used {len(coins_used)}\n{coins_used}"


print(calc_min_coins(2.78))
