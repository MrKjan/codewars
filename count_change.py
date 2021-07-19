# https://www.codewars.com/kata/541af676b589989aed0009e7/train/python

def count_change(money, coins):
    coins.sort()

    def _get_permutations(head=[]):
        new_heads = [head + [i] for i in coins if sum(head) + i]
        return 

# test.assert_equals(3, count_change(4, [1,2]))
# test.assert_equals(4, count_change(10, [5,2,3]))
# test.assert_equals(0, count_change(11, [5,7]))
