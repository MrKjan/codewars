def delete_nth(order, max_e):
    return [elem for elem, idx in zip(order, range(len(order))) if order[:idx].count(elem) < max_e]

# zip() can be enumerate()

print(delete_nth([1, 3, 3, 7, 2, 2, 2, 1, 1, 2], 2))
