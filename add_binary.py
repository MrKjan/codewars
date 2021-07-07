def add_binary(a, b):
    def to_binary(val):
        ret = ''
        while 0 != val:
            ret = str(val%2) + ret
            val //= 2
        return ret

    return to_binary(a + b)

print(add_binary(7, 5))
