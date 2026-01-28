# input: amount, denominations
# output: -1 for none, min number of coins for target amount


def min_number_of_coins(amt: int, denoms: list[int]) -> int:
    dp = [0.0] + [float("inf") for _ in range(amt)]

    for i in range(1, amt + 1):
        for c in denoms:
            if c <= i:
                dp[i] = min(dp[i], 1 + dp[i - c])

    return -1 if dp[amt] == float("inf") else int(dp[amt])
