import timeit

def find_coins_greedy(amount):
    coins = [50, 25, 10, 5, 2, 1]
    result = {}
    for coin in coins:
        if amount // coin > 0:
            result[coin] = amount // coin
            amount = amount % coin
    return result

def find_min_coins(amount):
    coins = [50, 25, 10, 5, 2, 1]
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    coin_used = [0] * (amount + 1)
    
    for coin in coins:
        for i in range(coin, amount + 1):
            if dp[i - coin] + 1 < dp[i]:
                dp[i] = dp[i - coin] + 1
                coin_used[i] = coin

    result = {}
    if dp[amount] == float('inf'):
        return "No solution"
  
    while amount > 0:
        coin = coin_used[amount]
        if coin in result:
            result[coin] += 1
        else:
            result[coin] = 1
        amount -= coin

    return result


amounts = [50, 99, 243, 555]

print("Жадібний алгоритм:")
for amount in amounts:
    start_time = timeit.default_timer()
    result_greedy = find_coins_greedy(amount)
    elapsed = timeit.default_timer() - start_time
    print(f"Сума: {amount}, Результат: {result_greedy}, Час: {elapsed:.6f} сек")

print("\Алгоритм динамічного програмування:")
for amount in amounts:
    start_time = timeit.default_timer()
    result_dp = find_min_coins(amount)
    elapsed = timeit.default_timer() - start_time
    print(f"Сума: {amount}, Результат: {result_dp}, Час: {elapsed:.6f} сек")