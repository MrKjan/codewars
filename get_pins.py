def get_pins(observed):
    neighbours = {
        1: (1, 2, 4),
        2: (2, 1, 3, 5),
        3: (3, 2, 6),
        4: (4, 1, 5, 7),
        5: (5, 2, 4, 6, 8),
        6: (6, 3, 5, 9),
        7: (7, 4, 8),
        8: (8, 5, 7, 9, 0),
        9: (9, 6, 8),
        0: (0, 8,)
    }

    import itertools as it
    ret_of_lists = list(it.product(*[neighbours[int(i)] for i in observed]))
    ret = [''.join((str(i) for i in to_str)) for to_str in ret_of_lists]
    return ret

print(get_pins('8'))


# ┌───┬───┬───┐
# │ 1 │ 2 │ 3 │
# ├───┼───┼───┤
# │ 4 │ 5 │ 6 │
# ├───┼───┼───┤
# │ 7 │ 8 │ 9 │
# └───┼───┼───┘
#     │ 0 │
#     └───┘