# https://www.codewars.com/kata/541af676b589989aed0009e7/train/python

# Too hard to use cps, memoization
def count_change_my(money, coins):
    coins = tuple(coin for coin in coins if coin <= money)
    if 0 == money:
        return 1
    if 0 == len(coins):
        return 0
    return sum(count_change_my(money-coin, (c for c in coins if c <= coin)) for coin in coins)

# This is better for cps
def count_change_v2(money, coins):
    coins = tuple(coin for coin in coins if coin <= money)
    if 0 == money:
        return 1
    if 0 == len(coins):
        return 0
    return count_change_v2(money-coins[0], coins) + count_change_v2(money, coins[1:])

# CPS style
def count_change_v2_cc(money, coins):
    def _count_change(money, coins, cc):
        coins = tuple(coin for coin in coins if coin <= money)
        if 0 == money:
            return cc(1)
        if 0 == len(coins):
            return cc(0)
        return _count_change(money,
                             coins[1:],
                             lambda x: _count_change(money-coins[0],
                                                     coins,
                                                     lambda y: cc(x + y)))
    return _count_change(money, coins, lambda x: x)

def count_change_cc_mem(money, coins):
    memory = {}
    def _count_change(money, coins, cc):
        coins = tuple(coin for coin in coins if coin <= money)
        if (money, coins) in memory:
            return cc(memory[(money, coins)])
        if 0 == money:
            return cc(1)
        if 0 == len(coins):
            return cc(0)
        return _count_change(money,
                             coins[1:],
                             lambda x: _count_change(money-coins[0],
                                                     coins,
                                                     lambda y: cc(x + y)))
    return _count_change(money, coins, lambda x: x)

print(count_change_v2_cc(4, (1,2))) # 3
print(count_change_v2_cc(10, (5,2,3))) # 4
print(count_change_v2_cc(11, (5,7))) # 0
