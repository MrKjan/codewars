def solution(s):
    from itertools import zip_longest

    ret = []
    for pair in zip_longest(s[::2], s[1::2], fillvalue='_'):
        ret.append(pair[0]+pair[1])
    
    return ret
