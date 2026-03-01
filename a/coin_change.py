import math

# input: amount, denominations
# output: -1 for none, min number of coins for target amount


# dp solution
def get_coin_dp(amt: int, denoms: list[int]) -> list:
    dp = [0.0] + [float("inf") for _ in range(amt)]

    for i in range(1, amt + 1):
        for c in denoms:
            if c <= i:
                dp[i] = min(dp[i], 1 + dp[i - c])
    return dp


def min_number_of_coins(amt: int, denoms: list[int]) -> int:
    dp = [0.0] + [float("inf") for _ in range(amt)]

    for i in range(1, amt + 1):
        for c in denoms:
            if c <= i:
                dp[i] = min(dp[i], 1 + dp[i - c])

    return -1 if dp[amt] == float("inf") else int(dp[amt])


# greedy solution
def greedy_min_number_of_coins(amt: int, denoms: list[int]) -> int:
    num_coins = 0
    for denom in sorted(denoms, reverse=True):
        if amt >= denom:
            num_coins += amt // denom
            amt %= denom

    return -1 if amt != 0 else num_coins


# coin systems must be in the form {1, c2, ...}
# any coin system with {1, c2} is guaranteed to be cannonical
def is_cannonical(denoms: list[int]) -> bool:
    sorted_denoms = sorted(
        list(set(denoms))
    )  # removed duplicates and sort in increasing order

    if not sorted_denoms:
        raise ValueError("denoms is empty")
    if sorted_denoms[0] != 1:
        raise ValueError("not canonical: must be in the form of {1, c2, ...}")
    if len(denoms) <= 2:
        return True

    # kozen zaks coin change bounds for the smallest possible counterexample
    lower, upper = sorted_denoms[2] + 1, sorted_denoms[-1] + sorted_denoms[-2]
    dp = get_coin_dp(upper - 1, sorted_denoms)

    for i in range(lower + 1, upper):
        greedy_sol = greedy_min_number_of_coins(i, sorted_denoms)
        if dp[i] != greedy_sol:
            print(f"fails for {i}: dp={dp[i]}, greedy={greedy_sol}")
            return False
    return True


# for non-standard systems, may not have {1, c2, ...}, can be simply any {c1, c2, ...}
# by the chicken mcnugget theorem (frobenius coin problem)
# div reduces set by rounding down to the multiples of
def get_unproducible_list(nums: list[int], limit=None, check_multiples_of=1) -> list:
    def is_coprime(x, y):
        return math.gcd(x, y) == 1

    # find frobenius number for each coprime number pair
    # for coprimes x, y: max not producible is x * y - x - y
    max_not_producible = -1
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            x, y = nums[i], nums[j]
            if is_coprime(x, y):
                max_not_producible = max(max_not_producible, x * y - x - y)

    # infinitely many can be made if none are coprime
    if max_not_producible == -1 and not limit:
        return [float("inf")]

    dp = []
    if limit:
        dp = get_coin_dp(limit, nums)
    else:
        dp = get_coin_dp(max_not_producible, nums)

    unproducible = set()
    for i in range(len(dp)):
        curr = i // check_multiples_of * check_multiples_of
        if dp[curr] == float("inf"):
            unproducible.add(curr)

    return sorted(list(unproducible))
