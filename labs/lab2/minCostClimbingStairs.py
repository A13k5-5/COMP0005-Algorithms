def minCostClimbingStairs(stairs):
    if len(stairs) == 0:
        return 0
    if len(stairs) < 2:
        return stairs[-1]

    dp = [0 for _ in stairs]
    dp[0], dp[1] = stairs[0], stairs[1]

    for i in range(2, len(stairs)):
        dp[i] = min(dp[i - 1], dp[i - 2]) + stairs[i]
    return dp[-1]


if __name__ == "__main__":
    print(minCostClimbingStairs([1, 101]))
