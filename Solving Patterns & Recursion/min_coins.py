### Greedy intuition ###
def min_coins(coins, amount):
    coins = sorted(coins)
    n = len(coins)
    result = 0
    for i in range(n-1, -1, -1):
        if amount >= coins[i]:
            cnt = amount // coins[i]
            result += cnt
            amount -= cnt * coins[i]
        if amount == 0:
            break
    return result

coins = [1, 5, 10, 20, 50, 100, 200]
amount = 586
print(min_coins(coins, amount))