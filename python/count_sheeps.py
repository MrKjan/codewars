def count_sheeps(sheep):
    if type(sheep) == list:
        return sheep.count(True)
    return 0