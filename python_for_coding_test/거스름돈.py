change = int(input())

coins = [500, 100, 50, 10]

n = 0
for coin in coins:
    n += change // coin
    change %= coin

print(n)
