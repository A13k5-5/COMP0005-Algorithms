def minCoinChangeTopDown(coins, amount):
    coins.sort()
    memo = {0: 0}

    def min_coins(amt):
        if amt in memo:
            return memo[amt]

        minn = float("inf")
        for coin in coins:
            diff = amt - coin
            if diff < 0:
                break
            minn = min(minn, 1 + min_coins(diff))

        memo[amt] = minn
        return minn

    result = min_coins(amount)
    if result < float("inf"):
        return result
    else:
        return -1


def minCoinChangeBottomUp(coins, amount):
    coins.sort()
    dp = [0] * (amount + 1)

    for i in range(1, amount + 1):
        minn = float("inf")

        for coin in coins:
            diff = i - coin
            if diff < 0:
                break
            minn = min(minn, 1 + dp[diff])

        dp[i] = minn
    return dp[amount]


if __name__ == "__main__":
    coins = [1, 2, 5, 10, 20, 50]
    amount = 7
    print(minCoinChangeTopDown(coins, amount))
