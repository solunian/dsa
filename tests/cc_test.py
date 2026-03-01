import a.coin_change as cc

d = [1, 3, 4]

print(cc.greedy_min_number_of_coins(6, d), cc.min_number_of_coins(6, d))


print(cc.is_cannonical(d))


us = [10, 25, 50, 100, 200, 500, 1000, 2000, 10000]
print(cc.get_unproducible_list(us, limit=10000, check_multiples_of=5))
