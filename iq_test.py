def iq_test(numbers):
    even_odd = list(map(lambda num: int(num) % 2, numbers.split()))
    if 1 == even_odd.count(0):
        return even_odd.index(0) + 1
    return even_odd.index(1) + 1

print(iq_test("1 3 5 2 7 11"))