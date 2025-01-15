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

    return min_coins(amount)


if __name__ == "__main__":
    print(minCoinChangeTopDown([2, 4, 6], 11))
